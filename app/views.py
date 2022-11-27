
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from app.models import (Attendence, Contact, Enrollment, Gallary,
                        MembershipPlan, Trainer)


def home(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('usernumber')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if len(username)>10 or len(username)<10:
            messages.info(request,"phone number is must 10 digit ")
            return redirect('/signin')
        if pass1 != pass2:
            messages.info(request,"password not matched")
            return redirect('/signin')
        try:
            if User.objects.get(username=username):
                messages.warning(request,"number is already taken")
                return redirect('/signin')
        except Exception as identifier:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,"email is already taken")
                return redirect('/signin')
        except Exception as identifier:
            pass
        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,'User is created please login')
        return redirect('/login')        
    return render(request , 'signin.html')

def user_login(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuserr = authenticate(username=username,password=pass1)
        if myuserr is not None:
            login(request,myuserr)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
            
        
    return render(request,"login.html")

def user_logout(request):
    logout(request)
    messages.success(request,'logout successful')
    return redirect('/login')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('fullname') #html form se name liya 
        email = request.POST.get('email')
        number = request.POST.get('num')
        desc = request.POST.get('desc')
        myquery = Contact(name=name, email=email, phone=number,msg=desc) # 1st from model 2nd from object
        myquery.save()  # obj saved info

        messages.info(request,'thanks for contacting us we will get back to you soon')

        return redirect('/contact')


    return render(request, 'contact.html')

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,'please login and try again')
        return redirect('/login')
        
    Membership = MembershipPlan.objects.all()
    SelectTrainer = Trainer.objects.all()
    context = {
        "Membership":Membership,"SelectTrainer":SelectTrainer
    }
    if request.method == "POST":
        FullName = request.POST.get('FullName')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        PhoneNumber = request.POST.get('PhoneNumber')
        DOB = request.POST.get('DOB')
        Member = request.POST.get('Member')
        trainer = request.POST.get('trainer')
        address = request.POST.get('address')
        query = Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB = DOB,SelectMembershipplan=Member,SelectTrainer=trainer,Address=address)
        query.save()
        messages.success(request,'Thanks for the Enrollment')
        return redirect('/enroll')

    return render(request, 'enroll.html' , context)

def Profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,'please login and try again')
        return redirect('/login')
    # get current user
    user_ph = request.user
    posts = Enrollment.objects.filter(PhoneNumber=user_ph) #match with phone number to verify the user
    attenden = Attendence.objects.filter(phone=user_ph) #match with phone number to verify the user
    context = {
        "posts":posts,
        "attendence":attenden
    }

    return render(request,'profile.html',context)

def gallary(request):
    posts = Gallary.objects.all()
    context = {'posts':posts}
    return render(request, "index.html" , context)



    # date = models.DateField(auto_now_add=True)
    # phone = models.CharField(max_length=15)
    # come =  models.CharField(max_length = 150)
    # out = models.CharField(max_length = 150)
    # workout = models.CharField(max_length = 150)
    # trainedby = models.CharField(max_length = 150)


def attendence(request):
    if not request.user.is_authenticated:
        messages.warning(request,'please login and try again')
        return redirect('/login')

    SelectTrainer = Trainer.objects.all()
    context = {"SelectTrainer":SelectTrainer}
    if request.method == "POST":
        phone = request.POST.get('PhoneNumber')
        come = request.POST.get('comein')
        out = request.POST.get('out')
        workout = request.POST.get('workout')
        trainedby = request.POST.get('trainer')
        query = Attendence(phone=phone,come=come,out=out,workout=workout,trainedby=trainedby)
        query.save()
        messages.warning(request,'Attendence applied')
        return redirect('/attendence')
    return render(request, "attendence.html", context)
