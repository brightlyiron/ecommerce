from django.contrib.auth import password_validation, get_user_model
from django.core.exceptions import ValidationError
from rest_framework import serializers

MAX_PASSWORD_LENGTH = 13
MIN_PASSWORD_LENGTH = 8


class AccountUserRetrieveSerializer(serializers.Serializer):
    username = serializers.CharField()

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def create(self, validated_data):
        raise NotImplementedError()


class AccountUserSignupSerializer(serializers.Serializer):
    error_messages = {
        "password_mismatch": "비밀번호가 일치하지 않습니다",
    }

    username = serializers.CharField(write_only=True, required=True)
    password1 = serializers.CharField(
        write_only=True, required=True, trim_whitespace=False, min_length=MIN_PASSWORD_LENGTH
        , max_length=MAX_PASSWORD_LENGTH
    )
    password2 = serializers.CharField(
        write_only=True, required=True, trim_whitespace=False, min_length=MIN_PASSWORD_LENGTH
        , max_length=MAX_PASSWORD_LENGTH
    )

    def validate_password2(self, password):
        try:
            password_validation.validate_password(password, self.instance)
        except ValidationError as e:
            raise serializers.ValidationError(e)
        return password

    def validate(self, attrs):
        password1 = attrs['password1']
        password2 = attrs['password2']

        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError(
                self.error_messages['password_mismatch'],
                code="password_mismatch"
            )
        return attrs

    def create(self, validated_data):
        user_model = get_user_model()
        user_obj = user_model(
            username=validated_data['username'],
        )
        user_obj.set_password(validated_data['password1'])
        user_obj.save()
        return user_obj

    def update(self, instance, validated_data):
        raise NotImplementedError()
