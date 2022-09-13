from django.urls import path

from .views import send_enquiry_email

urlpatterns = [path("", send_enquiry_email, name="send-inquiry")]
