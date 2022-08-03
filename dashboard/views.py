from django.shortcuts import render

from authentication.models import *
from jobpost.models import *
from django.db.models import Q
import datetime as dt


# Create your views here.
def main_dashboard(request):
    template_name = "dashboard/main_dashboard.html"
    if 'from_date' in request.GET or  'to_date' in request.GET:
        from_date = request.GET['from_date']
        to_date = request.GET['to_date']
        multiple_q = Q(Q(created_date__range=[dt.datetime.strptime(from_date, '%Y-%m-%d').date(), dt.datetime.strptime(to_date, '%Y-%m-%d').date()]) & Q(role__in=["employer", "applicant"]))
        filter_jobpost = Q(Q(created_at__range=[dt.datetime.strptime(from_date, '%Y-%m-%d').date(), dt.datetime.strptime(to_date, '%Y-%m-%d').date()]))
        users = User.objects.filter(multiple_q)

        users_count = User.objects.filter(multiple_q).count()
        new_users = User.objects.filter(multiple_q).count()
        job_posted = JobPost.objects.filter(filter_jobpost).count()
    else:    
        users = User.objects.filter(role__in=["employer", "applicant"])
        employer = Employer.objects.all()
        applicant = Applicant.objects.all()

        users_count = User.objects.filter(role__in=["employer", "applicant"]).count()
        new_users = User.objects.filter(created_date=dt.date.today()).count()
        job_posted = JobPost.objects.all().count()
    
    context = { 
        "users": users,
        "users_count": users_count,
        "new_users": new_users,
        "job_posted": job_posted,
    }
    return render (request, template_name, context)
