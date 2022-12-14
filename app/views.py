from django.shortcuts import render
from app.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact=Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

        messages.success(request, 'Your responce has been send!.')

    return render(request,'index.html')