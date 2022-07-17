from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets


class AccountUserAPIView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = get_user_model().objects.all()


user_api = AccountUserAPIView.as_view({'get': 'retrieve'})


class AccountUserSignUpAPIView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = get_user_model().objects.all()


user_signup_api = AccountUserSignUpAPIView.as_view({'post': 'create'})
