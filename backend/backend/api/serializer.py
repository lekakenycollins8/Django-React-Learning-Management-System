"""LMS serializers: converts model instances to JSON so that the frontend can work with the data"""

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from userauths.models import User, Profile

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom token obtain pair serializer: adds full name, email, and username to the token"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['full_name'] = user.full_name
        token['email'] = user.email
        token['username'] = user.username

        return token

class UserSerializer(serializers.ModelSerializer):
    """User serializer"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'full_name', 'otp')

class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer"""
    class Meta:
        model = Profile
        fields = ('id', 'user', 'image', 'full_name', 'country', 'date')