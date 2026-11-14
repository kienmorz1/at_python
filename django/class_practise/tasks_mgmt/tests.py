from django.test import TestCase
from rest_framework.test import APIClient

from .authentication import create_access_token
from .models import User
from .utils import BcryptPasswordUtil


class JWTAuthenticationTests(TestCase):
    def setUp(self):
        self.password = "test-password"
        self.user = User.objects.create(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            password=BcryptPasswordUtil.hash_password(self.password),
        )
        self.client = APIClient()

    def test_login_token_authenticates_custom_user(self):
        login_response = self.client.post(
            "/api/login/",
            {"email": self.user.email, "password": self.password},
            format="json",
        )
        self.assertEqual(login_response.status_code, 200)

        token = login_response.json()["token"]
        response = self.client.get(
            "/api/protected/",
            HTTP_AUTHORIZATION=f"Bearer {token}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["user_id"], self.user.pk)

    def test_protected_view_rejects_missing_token(self):
        response = self.client.get("/api/protected/")

        self.assertEqual(response.status_code, 401)

    def test_protected_view_rejects_token_for_deleted_user(self):
        token = str(create_access_token(self.user))
        self.user.delete()

        response = self.client.get(
            "/api/protected/",
            HTTP_AUTHORIZATION=f"Bearer {token}",
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["detail"], "User not found")

    def test_login_rejects_inactive_user(self):
        self.user.is_active = False
        self.user.save(update_fields=["is_active"])

        response = self.client.post(
            "/api/login/",
            {"email": self.user.email, "password": self.password},
            format="json",
        )

        self.assertEqual(response.status_code, 401)
