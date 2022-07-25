from django.urls import path, include


from .views import *

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login', login_page, name="login"),
    path('accounts/logout', logout_user, name="logout"),
    path("register-admin", AdminSignUpView.as_view(), name="admin-register"),
    path("authentication/register/employer", EmployerSignUpView.as_view(), name="employer-register"),
    path("authentication/register/employer/", EmployerSignUpView.as_view(), name="employer-register"),
    path("authentication/register/applicant", ApplicantSignUpView.as_view(), name="applicant-register"),
    path("employer-profile/", employer_profile, name="employer_profile"),
    path("applicant-profile", applicant_profile, name="applicant_profile"),
    path("verify-email/<str:str>", verify_email, name="verify_email"),
    path("email-verification-sent", email_sent, name="email_sent"),
    path("reset-password-email", reset_password_emai, name="reset_password_emai"),
    path("reset-password/<str:str>", reset_password, name="reset-password"),
    path("applicant_update/<int:pk>", applicantprofile_update, name="applicant_update"),
    path("employer_update/<int:pk>/", employer_update, name="employer_update")
]