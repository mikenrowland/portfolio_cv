from django.shortcuts import redirect, render
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            form.save()
            messages.info(request, f"Thanks {name} for your message, I will get back to you shortly")
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
