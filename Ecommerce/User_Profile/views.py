from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

# IsAuthenticatedOrReadOnly
from User_Profile import serializers
from User_Profile import models
from User_Profile import permissions

# -------------------User Management (view set)--------------------------
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

# ----------------Login and Token-------------------------
class UserLoginApiView(ObtainAuthToken):
    """Handle Creating User authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
