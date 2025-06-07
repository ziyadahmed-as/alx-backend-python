from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
" i want write Custom Authentication Backend for my Django app that allows users to log in using either their email or username. "
class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Try to find the user by username or email
            user = UserModel.objects.get(
                Q(username=username) | Q(email=username)
            )
        except ObjectDoesNotExist:
            return None
        
        # Check if the password is correct
        if user.check_password(password):
            return user
        return None