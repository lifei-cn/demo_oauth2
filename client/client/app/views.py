from django.shortcuts import render
from django.views.generic.base import TemplateView
from allauth.socialaccount.providers.baidu.views import BaiduOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from client.customprovider.views import CustomAdapter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class TestAPI(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        msg = {'msg': 'Hello World'}
        return Response(data=msg, status=status.HTTP_200_OK)


class CustomLogin(SocialLoginView):
    adapter_class = CustomAdapter


class BaiduLogin(SocialLoginView):
    adapter_class = BaiduOAuth2Adapter


class ProfileView(TemplateView):
    template_name = "profile.html"
