
from django.db import models
from django.contrib.auth.models import AbstractUser
from config.models import BaseModel
# Create your models here.

class User(AbstractUser):
    role = (
        ("superadmin", "superadmin"),
        ("admin", "admin"),
        ("employer", "employer"),
        ("applicant", "applicant"),
    )
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    role = models.CharField(max_length=255, choices=role)
    is_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to="profile_picture/")

    

    created_date = models.DateField(auto_now_add=True)

class Employer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_employer")
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    business_nature = models.CharField(
        max_length=255, help_text="Ex. FastFood, IT, BPO")
    accepted = models.BooleanField(default=False)
    business_permit = models.ImageField(upload_to="business_permit/", null=True, blank=True) 
  
     

    def __str__(self):
        return self.company_name
        
class Applicant(BaseModel):
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_applicant")
    address = models.CharField(max_length=255)
    working_exp = models.CharField(max_length=255, choices=choices)
    prev_employer = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(auto_now_add=False)
    age = models.IntegerField()
    contact = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    house_no = models.CharField(max_length=255)
    barangay = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    working_exp = models.CharField(max_length=255, choices=choices)
    prev_employer = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(auto_now_add=False)
    age = models.CharField(max_length=2)
    contact = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    religion = models.CharField(max_length=255)
    tin_number = models.IntegerField()
    employment_status = models.CharField(max_length=255, choices=employment)
    employed = models.CharField(max_length=255, choices=if_employed)
    currently_in_school = models.CharField(max_length=255, choices=in_school)
    educational_attainment = models.CharField(max_length=255, choices=education)
    



    def __str__(self):
        return f"{self.user.last_name}, {self.user.first_name}"

     