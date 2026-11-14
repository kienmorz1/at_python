from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import AccessToken

from .models import User


def create_access_token(user: User) -> AccessToken:
    user_id_claim = api_settings.USER_ID_CLAIM
    user_id_field = api_settings.USER_ID_FIELD
    if not isinstance(user_id_claim, str) or not isinstance(user_id_field, str):
        raise RuntimeError("SIMPLE_JWT user ID settings must be strings")

    user_id = getattr(user, user_id_field)
    token = AccessToken()
    token[user_id_claim] = user_id if isinstance(user_id, int) else str(user_id)
    return token


class TaskUserJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id_claim = api_settings.USER_ID_CLAIM
        if not isinstance(user_id_claim, str):
            raise RuntimeError("SIMPLE_JWT USER_ID_CLAIM must be a string")

        try:
            user_id = validated_token[user_id_claim]
        except KeyError as exc:
            raise AuthenticationFailed(
                "Token contained no user identification",
                code="user_id_missing",
            ) from exc

        user_id_field = api_settings.USER_ID_FIELD
        if not isinstance(user_id_field, str):
            raise RuntimeError("SIMPLE_JWT USER_ID_FIELD must be a string")

        try:
            user = User.objects.get(**{user_id_field: user_id})
        except User.DoesNotExist as exc:
            raise AuthenticationFailed(
                "User not found",
                code="user_not_found",
            ) from exc

        if api_settings.CHECK_USER_IS_ACTIVE and not user.is_active:
            raise AuthenticationFailed("User is inactive", code="user_inactive")

        return user
