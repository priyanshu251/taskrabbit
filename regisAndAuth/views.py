from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permission import IsAuthenticated

# Create your views here.

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects()
    serializer_class= UserSerializer
    # applying token authentication
    auth_calsses = [TokenAuthentication]     # using in-built authentication class
    permission_classes = [IsAuthenticated]

