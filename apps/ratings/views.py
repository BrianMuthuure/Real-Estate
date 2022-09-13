from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.profiles.models import Profile

from .models import Rating

User = get_user_model()


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_agent_review(request, profile_id):
    agent_profile = Profile.objects.get(uuid=profile_id, is_agent=True)
    data = request.data

    profile_user = User.objects.get(id=agent_profile.user.id)
    if profile_user.email == request.user.email:
        return Response(
            {"message": "You cannot rate yourself"}, status=status.HTTP_403_FORBIDDEN
        )
    res = agent_profile.agent_review.filter(agent__id=profile_user.id).exists()
    if res:
        return Response(
            {"detail": "Profile already reviewed"}, status=status.HTTP_400_BAD_REQUEST
        )
    elif data["rating"] == 0:
        return Response(
            {"detail": "Please select a rating"},
            status=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    else:
        review = Rating.objects.create(
            rater=request.user,
            agent=agent_profile,
            rating=data["rating"],
            comment=data["comment"],
        )
        reviews = agent_profile.agent_review.all()
        agent_profile.num_reviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating
        return Response(
            {"success": True, "message": "review added successfully"},
            status=status.HTTP_200_OK,
        )
