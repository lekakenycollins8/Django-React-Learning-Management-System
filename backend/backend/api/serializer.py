"""LMS serializers: converts model instances to JSON so that the frontend can work with the data"""

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from userauths.models import User, Profile
from django.contrib.auth.password_validation import validate_password

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom token obtain pair serializer: adds full name, email, and username to the token"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['full_name'] = user.full_name
        token['email'] = user.email
        token['username'] = user.username

        return token

class RegisterSerializer(serializers.ModelSerializer):
    """Register serializer"""
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'password2')

    def validate(self, attr):
        """validate password for match"""
        if attr['password'] != attr['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match"})
        return attr

    def create(self, validated_data):
        """Create user"""
        user = User.objects.create_user(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
        )

        email_username, _ = user.email.split('@')
        user.username = email_username
        user.set_password(validated_data['password'])
        user.save()

        return user

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