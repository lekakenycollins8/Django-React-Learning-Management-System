"""LMS serializers: converts model instances to JSON so that the frontend can work with the data"""

from rest_framework import serializers
from userauths.models import User, Profile

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