from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, permissions

from . import serializers


class AccountUserAPIView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = get_user_model().objects.all().values("username")
    serializer_class = serializers.AccountUserRetrieveSerializer


user_api = AccountUserAPIView.as_view({'get': 'retrieve'})


class AccountUserSignUpAPIView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = get_user_model().objects.all()
    serializer_class = serializers.AccountUserSignupSerializer


user_signup_api = AccountUserSignUpAPIView.as_view({'post': 'create'})
