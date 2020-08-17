from django.urls import path
from .views import (RegisterView, VerifyEmail, LoginApiView,
                    PasswordTokenCheckApi, RequestPasswordResetEmail, SetNewPasswordApiView)

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginApiView.as_view(), name="login"),
    path("email-verify/", VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("reset-password-request/", RequestPasswordResetEmail.as_view(),
         name="reset-password-request"),
    path("password-reset/<uidb64>/<token>/", PasswordTokenCheckApi.as_view(),
         name="password-reset-confirmation", ),
    path("password-reset-completed", SetNewPasswordApiView.as_view(),
         name="password-reset-completed")
]
