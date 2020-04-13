from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.serializers import TokenObtainSerializer

from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': False}, 'username': {'required': False}}

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)