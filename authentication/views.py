from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
# Create your views here.

class RegisterView(GenericAPIView):
    def post(self,request):
        pass
