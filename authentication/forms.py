from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["last_name", "first_name", "email"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = "admin"
        if commit:
            user.save()
        return user


class EmployerSignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=255)
    company_address = forms.CharField(max_length=255)
    business_nature = forms.CharField(max_length=255)
    business_permit = forms.FileField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["profile_picture", "business_permit", "last_name", "first_name", "email",
        "company_name", "company_address", "business_nature"]

class EmployerUpdateForm(forms.ModelForm):
    company_name = forms.CharField(max_length=255)
    company_address = forms.CharField(max_length=255)
    business_nature = forms.CharField(max_length=255)
    business_permit = forms.FileField()

    class Meta:
        model = Employer
        fields = ["business_permit",  "company_name", "company_address", "business_nature"]

class EmployerUserUpdateForm(forms.ModelForm):
    profile_picture = forms.FileField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email= forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["profile_picture","last_name", "first_name", "email"]



class ApplicantSignUpForm(UserCreationForm):
    choices = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    employment = (
        ("Employed", "Employed"),
        ("Unemployed", "Unemployed"),
        ("Others", "Others"),
    )
    if_employed = (
        ("Waged employed", "Waged employed"),
        ("Self-employed", "Self-employed"),
        ("Others", "Others"),
    )
    in_school = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    education = (
        ("No Formal Education", "No Formal Education"),
        ("Elementary Level", "Elementary Level"),
        ("Elementary Graduate", "Elementary Graduate"),
        ("High School Level", "High School Level"),
        ("High School Graduate", "High School Graduate"),
        ("College Level", "College Level"),
        ("College Graduate", "College Graduate"),
        ("Technical-Vocational Graduate", "Technical-Vocational Graduate"),
        ("Post-Graduate", "Post-Graduate"),
    )
    # address = forms.CharField(max_length=255)
    middle_name = forms.CharField(max_length=255)
    house_no = forms.CharField(max_length=255,  label="House No./Street/Village")
    barangay = forms.CharField(max_length=255)
    municipality = forms.CharField(max_length=255)
    province = forms.CharField(max_length=255)
    working_exp = forms.ChoiceField(
        choices=choices, label="Do you have working experience?")
    prev_employer = forms.CharField(
        max_length=255, label="Previous Employer (if you have working experience)", initial="N/A")
    birthdate = forms.CharField(max_length=255, widget=DateInput())
    age = forms.CharField(max_length=255)
    contact = forms.CharField(max_length=255)
    height = forms.CharField(max_length=255)
    religion = forms.CharField(max_length=255)
    tin_number = forms.IntegerField()
    employment_status = forms.ChoiceField(choices=employment)
    employed = forms.ChoiceField(choices=if_employed)
    currently_in_school = forms.ChoiceField(choices=in_school)
    educational_attainment = forms.ChoiceField(choices=education)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["profile_picture", "last_name", "middle_name" ,"first_name",  "age", "birthdate", "house_no",
        "barangay", "municipality", "province", "height", "religion", "email", "tin_number", "contact",
        "employment_status", "employed", "currently_in_school", "educational_attainment", "working_exp", "prev_employer"]

        widgets = {
            "birthdate": DateInput()
        }

class ApplicantUpdateForm(forms.ModelForm):
    choices = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    employment = (
        ("Employed", "Employed"),
        ("Unemployed", "Unemployed"),
        ("Others", "Others"),
    )
    if_employed = (
        ("Waged employed", "Waged employed"),
        ("Self-employed", "Self-employed"),
        ("Others", "Others"),
    )
    in_school = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    education = (
        ("No Formal Education", "No Formal Education"),
        ("Elementary Level", "Elementary Level"),
        ("Elementary Graduate", "Elementary Graduate"),
        ("High School Level", "High School Level"),
        ("High School Graduate", "High School Graduate"),
        ("College Level", "College Level"),
        ("College Graduate", "College Graduate"),
        ("Technical-Vocational Graduate", "Technical-Vocational Graduate"),
        ("Post-Graduate", "Post-Graduate"),
    )
    # address = forms.CharField(max_length=255)
    
    middle_name = forms.CharField(max_length=255)
    house_no = forms.CharField(max_length=255,  label="House No./Street/Village")
    barangay = forms.CharField(max_length=255)
    municipality = forms.CharField(max_length=255)
    province = forms.CharField(max_length=255)
    working_exp = forms.ChoiceField(
        choices=choices, label="Do you have working experience?")
    prev_employer = forms.CharField(
        max_length=255, label="Previous Employer (if you have working experience)", initial="N/A")
    birthdate = forms.CharField(max_length=255, widget=DateInput())
    age = forms.CharField(max_length=2)
    contact = forms.CharField(max_length=255)
    height = forms.CharField(max_length=255)
    religion = forms.CharField(max_length=255)
    tin_number = forms.IntegerField()
    employment_status = forms.ChoiceField(choices=employment)
    employed = forms.ChoiceField(choices=if_employed)
    currently_in_school = forms.ChoiceField(choices=in_school)
    educational_attainment = forms.ChoiceField(choices=education)

    class Meta:
        model = Applicant
        fields = ["middle_name","age", "birthdate", "house_no",
        "barangay", "municipality", "province", "height", "religion", "tin_number", "contact",
        "employment_status", "employed", "currently_in_school", "educational_attainment", "working_exp", "prev_employer"]

        widgets = {
            "birthdate": DateInput()
        }

class ApplicantUserUpdateForm(forms.ModelForm):
    # address = forms.CharField(max_length=255)
    profile_picture = forms.FileField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email= forms.CharField(max_length=255)
   

    class Meta:
        model = User
        fields = ["profile_picture", "last_name" ,"first_name",  "email"]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "email"]


class LoginForm(forms.Form):
    email = forms.CharField(max_length=63, widget=forms.TextInput(attrs={"placeholder" :  "name@email.com","class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={"placeholder" :  "••••••••","class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"}))


class ResetForm(forms.Form):
    email = forms.CharField(max_length=63, widget=forms.TextInput(attrs={"placeholder" :  "name@email.com","class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"}))


class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={"placeholder" :  "••••••••","class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"}))
    password2 = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={"placeholder" :  "••••••••","class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"}))
