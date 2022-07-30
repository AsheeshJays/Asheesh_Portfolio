from django.shortcuts import render
from .models import Contact, project,Hire
from django.contrib import messages
from django.core.mail import send_mail,send_mass_mail

def IndexPage(request):
    if request.method == 'POST':
        c=Contact()
        c.name = request.POST.get('name')
        c.email = request.POST.get('email')
        c.subject = request.POST.get('subject')
        c.message = request.POST.get('message')
        subject = "For Contact"
        body =  """
                    Hello,
                    Thank you for Contacting me,
                    I will not disappointyou.
                    I will give my best for your
                    work,
                    Thank You,
                    FROM:  Asheesh Jaysawal
                """
        send_mail(subject, body,"ashishjaiswal9807@gmail.com",[c.email,], fail_silently=False)
        c.save()
        messages.success(request, 'Thank You for contact us')
    return render(request, 'index.html')

def ProjectPage(request):
    pro = project.objects.all()
    return render(request, 'project.html',{'Project':pro})

def HireMe(request):
    if request.method == 'POST':
        h=Hire()
        h.name = request.POST.get('name')
        h.email = request.POST.get('email')
        h.subject = request.POST.get('subject')
        h.message = request.POST.get('message')
        subject = "For Hiring"
        body =  """
                    Hello,
                    Thank you for hiring me,
                    I will not disappointyou.
                    I will give my best for your
                    work,
                    Thank You,

                    From:  Asheesh Jaysawal
                """
        send_mail(subject, body,"ashishjaiswal9807@gmail.com",[h.email,], fail_silently=False)
        h.save()
        messages.success(request, 'Thank You for Hiring Me!!!')
    return render(request, 'hireme.html')
