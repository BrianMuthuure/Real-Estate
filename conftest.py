import pytest
from pytest_factoryboy import register
from tests.factories import UserFactory, ProfileFactory

"""
Fixtures are used to feed some data to the tests such as database connections,
URLs to test and some sort of input data. 
Therefore, instead of running the same code for every test,
we can attach fixture function to the tests and it will run and return
the data to the test before executing each test
"""

register(UserFactory)
register(ProfileFactory)

"""
UserFactory==user_factory
ProfileFactory==profile_factory
"""


@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    return new_user


@pytest.fixture
def super_user(db, user_factory):
    new_user = user_factory.create(is_staff=True, is_superuser=True)
    return new_user


@pytest.fixture
def profile(db, profile_factory):
    user_profile = profile_factory.create()
    return user_profile
