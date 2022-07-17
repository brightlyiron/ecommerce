from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign-up', views.user_signup_api, name='sign_up'),
    path('<int:pk>', views.user_api, name='user'),
]
