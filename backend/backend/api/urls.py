"""module for api urls"""

from api import views as api_views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('user/token/', api_views.CustomTokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/register/', api_views.RegistrationView.as_view()),
    path('user/password-reset/<email>/', api_views.PasswordResetEmailVerifyAPIView.as_view()),
]