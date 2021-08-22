from django.shortcuts import redirect, render
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            subject = "New Contact Message"
            try:
                send_mail(subject, message, email, [settings.EMAIL_RECIPIENT], fail_silently=False)
            except:
                return HttpResponse('Invalid header found.')
            form.save()
            messages.info(request, f"Thanks {name} for your message, I will get back to you shortly")
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})
