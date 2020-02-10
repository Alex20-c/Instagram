from django.test import TestCase

from .models import Profile, Image, Comments

from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):

    '''

    Test case for the Profile class and it's behaviours

    '''

    # Set up method

    def setUp(self):

        '''

        Method that will run before any test case under this class

        '''

        self.new_user = User(username = "alex", email = "kipropalex59@gmail.com", password = "fergason")

        self.new_user.save()

        self.new_profile = Profile(user = self.new_user, bio="self love")

    def tearDown(self):

        Profile.objects.all().delete()

    # Testing instance

    def test_instance(self):

        '''

        Test to confirm that the object is being instantiated correctly

        '''

        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_method(self):

        profile = Profile.objects.all()

        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):

        self.new_profile.save_profile()

        self.new_profile.delete_profile()

        profile = Profile.objects.all()

        self.assertTrue(len(profile) == 0)

