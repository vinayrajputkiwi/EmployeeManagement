from django.shortcuts import render,redirect
from .forms import checkinform,checkoutform,registerform
from .models import checkin,checkout,registeremp

def checkIn(request):
    if request.method == "POST":
        form=checkinform(request.POST)
        fn=request.POST['first_name']
        ln=request.POST['last_name']
        em=request.POST['email']
        try:
            d1=registeremp.objects.get(first_name=fn,last_name=ln,email=em)
        except registeremp.DoesNotExist:
            return redirect('register')
        else:  
            request.session['uid'] = d1.id
            form=checkinform(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/')
    else:
        form=checkinform()
    return render(request,'home.html',{'form':form})

def checkout(request):
    if request.method == "POST":
        form=checkoutform(request.POST)
        fn=request.POST['first_name']
        ln=request.POST['last_name']
        em=request.POST['email']
        try:
            d1=checkin.objects.get(first_name=fn,last_name=ln,email=em)
        except checkin.DoesNotExist:
            return redirect('home')
        else:  
            request.session['uid'] = d1.id
            form=checkoutform(request.POST)
            if form.is_valid():
                form.save()
            return redirect('home')
    else:
        form=checkoutform()
    return render(request,'checkout.html',{'form':form})



def register(request):
     if request.method == 'POST':
         form=registerform(request.POST)
         if form.is_valid():
             form.save()
             return redirect('home')
     else:
         form=registerform()
     return render(request,'register.html',{'form':form})
