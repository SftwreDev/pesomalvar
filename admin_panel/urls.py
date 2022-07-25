from django.urls import path

from .views import *

urlpatterns = [
    path("admin-page/", admin_page, name="admin_page"),
    path("account-accept/<int:pk>", accept_account, name="accept_account"),
    path("account-unaccept/<int:pk>", unaccept_account, name="unaccept_account"),
    path("employer-view/<int:pk>", employer_account_view, name="employer_view"),
    path("applicant-view/<int:pk>", applicant_account_view, name="applicant_view"),
    # path("view-pdf", view_pdf, name="view_pdf"),
]