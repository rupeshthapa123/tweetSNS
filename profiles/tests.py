from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile
from rest_framework.test import APIClient

User = get_user_model()

# We create two users, then we test that the profile is created via the signal, then we test that the
# user can follow another user, then we test that the user can unfollow another user, and finally we
# test that the user cannot follow himself

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cfe', password='somepassword')
        self.userb = User.objects.create_user(username='cfe-2', password='somepassword2')
    
    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client

    def test_profile_created_via_signal(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(),2)
    
    def test_following(self):
        first = self.user
        second = self.userb
        first.profile.followers.add(second)
        second_user_following_whom = second.following.all()
        qs = second_user_following_whom.filter(user=first)
        first_user_following_no_one = first.following.all()
        self.assertTrue(qs.exists())
        first_user_following_no_one = first.following.all()
        self.assertFalse(first_user_following_no_one.exists())

    def test_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(f"/api/profiles/{self.userb.username}/follow",
            {"action": "follow"}
        )
        r_data = response.json()
        count = r_data.get("count")
        self.assertEqual(count, 1)

    def test_unfollow_api_endpoint(self):
        first = self.user
        second = self.userb
        first.profile.followers.add(second)
        client = self.get_client()
        response = client.post(f"/api/profiles/{self.userb.username}/follow",
        {"action": "unfollow"}
        )
        r_data = response.json()
        count = r_data.get("count")
        self.assertEqual(count, 0)

    def test_cannot_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(f"/api/profiles/{self.user.username}/follow",
            {"action": "follow"}
        )
        r_data = response.json()
        count = r_data.get("count")
        self.assertEqual(count, 0)