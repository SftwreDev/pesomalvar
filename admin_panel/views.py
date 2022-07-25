from django.shortcuts import get_object_or_404, render, redirect


from authentication.models import *

# Create your views here.

def admin_page(request):
    template_name = "admin/admin_panel.html"
    applicant = Applicant.objects.all()
    employer = Employer.objects.all()
    context = {
        "employer" : employer,
        "applicant" : applicant,
        
    }
    return render(request, template_name, context)


def accept_account(request, pk):
    Employer.objects.filter(id=pk).update(accepted=True)
    return redirect("admin_page")

def unaccept_account(request, pk):
    Employer.objects.filter(id=pk).update(accepted=False)
    return redirect("admin_page")

def employer_account_view(request, pk):
    template_name = "admin/account_detailed.html"
    employer = Employer.objects.get(id=pk)
    context = {
        "employer": employer
    }
    return render(request, template_name, context)

def applicant_account_view(request, pk):
    template_name = "admin/applicant_detailed.html"
    applicant = Applicant.objects.get(id=pk)
    context = {
        "applicant": applicant
    }
    return render(request, template_name, context)


# def view_pdf(request, self):
#     objkey = self.kwargs.get('pk', None) #1
#     pdf = get_object_or_404(objkey, pk=objkey) #2
#     fname = pdf.filename() #3
#     path = os.path.join(settings.MEDIA_ROOT, 'business_permit\\' + fname)#4
#     response = FileResponse(open(path, 'rb'), content_type="application/pdf")
#     response["Content-Disposition"] = "filename={}".format(fname)
#     return response

# def view_pdf(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; attachment; filename=Employer Name' + 'Company Name' + '.pdf' 
#     response['Content-Transfer-Encoding'] = 'binary'

#     html_string = render_to_string(MEDIA_URL/{'business_permit'})
#     html = HTML(string=html_string)

#     result= html.write_pdf()

#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(result)
#         output.flush()
#         output = open(output.name, 'rb')
#         response.write(output.read())

#     return response
