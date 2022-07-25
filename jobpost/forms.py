from django import forms

from .models import *
from applicant.models import *

class JobPostFormView(forms.ModelForm):
    class Meta:
        model =JobPost
        fields =["title" , "description", "attach_file"]

class ApplicantStatusView(forms.ModelForm):
    class Meta:
        model = ApplicationForm
        fields =["approved"]