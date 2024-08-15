from django.shortcuts import render
from api import serializer as api_serializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom token obtain pair view: adds full name, email, and username to the token"""
    serializer_class = api_serializer.CustomTokenObtainPairSerializer
