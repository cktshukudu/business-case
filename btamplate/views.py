from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from .forms import createForm
from .forms import updateTemplate
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Formi
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives



def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('btamplate:login')
    else:
        form = UserRegisterForm()
    return render(request, 'btamplate/signup.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'btamplate/createTemplate.html', {})

def createTemplate(request):
    if request.method == "POST":
            form = createForm(request.POST, request.FILES)
            if form.is_valid():
                pro_date = request.POST.get("pro_date","")
                name = request.POST.get("name", "")
                role = request.POST.get("role", "")
                logo = request.POST.get("logo", "")
                summary = request.POST.get("summary", "")
                project = request.POST.get("project", "")
                limitations = request.POST.get("limitations", "")
                approach = request.POST.get("approach", "")
                benefits = request.POST.get("benefits", "")
                opportunities = request.POST.get("opportunities", "")
                nobel = request.POST.get("nobel", "")
                threat = request.POST.get("threat", "")
                financial = request.POST.get("financial", "")
                risk = request.POST.get("risk", "")

                form = Formi(pro_date=pro_date,name=name,role=role,logo=logo,summary=summary,project=project,
                limitations=limitations,approach=approach,benefits=benefits,opportunities=opportunities,
                nobel=nobel,threat=threat,financial=financial,risk=risk)

            messages.success(request, f'Template was created successfully')
            form.save()
            return redirect('btamplate:createTemplate')
    else:
        form = createForm()
    return render(request, 'btamplate/createTemplate.html', {'form': form})

def index(request):
    return render(request, "btamplate/base.html", {})

def main(request):
    return render(request, "btamplate/main.html", {})

def contact(request):
    if request.method == "POST":
	    message_name = request.POST['message-name']
	    message_email = request.POST['message-email']
	    message = request.POST['message']
		# send an email
	    send_mail(
		    message_name, # subject
		    message, # message
		    message_email, # from email
		['devtespace@gmail.com'], # To Email
			)

	    return render(request, 'btamplate/contact.html', {'message_name': message_name})

    else:
        return render(request, "btamplate/contact.html", {})

def update(request):
    user_form = Formi.objects.all()
    return render(request, "btamplate/update.html",{'user_form':user_form})


def delete_template(request, object_id):
    user_form = Formi.objects.get(pk = object_id)
    if request.method == 'POST':
        user_form.delete()
        return redirect('btamplate:update')
    return render(request, 'btamplate/delete_template.html')

def update_template(request, object_id):
    user_form = Formi.objects.get(pk = object_id)
    form = updateTemplate(instance=user_form)
    if request.method == 'POST':
        form = updateTemplate(request.POST, instance=user_form)
        if form.is_valid():
            form.save()
        return redirect('btamplate:update')
    context = {
         
         'form':form
     }   
    return render(request, 'btamplate/createTemplate.html', context)

class CustomerListView(ListView):
    model = Formi
    template_name = 'btamplate/update.html'

def render_pdf_view(request, object_id):
    user_form = Formi.objects.get(pk = object_id)
    template_path = 'btamplate/image.html'
    context = {'user_form':user_form}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Business_Case.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def email(request, object_id):
    if request.method == "POST":
        user_form = Formi.objects.get(pk = object_id)
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        # print(user_form,to,content)
        html_content = render_to_string("btamplate/email_template.html",{'title':'test email','content':content,'user_form':user_form})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Business Case",
            content,
            settings.EMAIL_HOST_USER,
            [to]
        )
        email.attach_alternative(html_content,"/")
        email.attach('Business.pdf', html_content, 'application/pdf')
        email.send()
        return render(
            request,
            'btamplate/email.html',
            {
                'title':'send an email'
            }
        )
    else:
        return render(
            request,
            'btamplate/email.html',
            {
                'title':'send an email'
            }
        )
