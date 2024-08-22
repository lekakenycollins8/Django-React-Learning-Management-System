from django.shortcuts import render
from api import serializer as api_serializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from userauths.models import User, Profile
from rest_framework.permissions import AllowAny
import random
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom token obtain pair view: adds full name, email, and username to the token"""
    serializer_class = api_serializer.CustomTokenObtainPairSerializer

class RegistrationView(generics.CreateAPIView):
    """Registration view"""
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = api_serializer.RegisterSerializer

def generate_random_otp(length=7):
    """Generate random otp"""
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return otp

class PasswordResetEmailVerifyAPIView(generics.RetrieveAPIView):
    """Password reset email verify API view"""
    permission_classes = [AllowAny]
    serializer_class = api_serializer.UserSerializer

    def get_object(self):
        """get user objects"""
        email = self.kwargs['email']

        user = User.objects.filter(email=email).first()

        if user:
            
            uuidb64 = user.pk

            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh.access_token)
            user.refresh_token = refresh_token
            user.otp = generate_random_otp()
            user.save()
            link = f'http://localhost:5173/create-new-password/?otp={user.otp}&uuidb64={uuidb64}'
            print("link ======", link)
        return user

class PasswordChangeAPIView(generics.CreateAPIView):
    """Password change API view"""
    permission_classes = [AllowAny]
    serializer_class = api_serializer.UserSerializer

    def PasswordChangeAPIView(generics.CreateAPIView):
        """Password change API view"""
        permission_classes = [AllowAny]
        serializer_class = api_serializer.UserSerializer

        def create(self, request, *args, **kwargs):
            """Create method"""
            payload = request.data

            otp = payload.get('otp')
            uuidb64 = payload.get('uuidb64')
            password = payload.get('password')

            user = User.objects.get(id=uuidb64, otp=otp)
            if user:
                user.set_password(password)
                user.otp = ""
                user.save()

                return Response({"message": "Password changed successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        