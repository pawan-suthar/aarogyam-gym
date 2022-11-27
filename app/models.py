from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=25) # copy fro m enrollment full name
    email = models.EmailField(null=True,unique=True)
    phone = models.CharField(max_length=12,unique=True,null=True)
    msg = models.TextField()

    def __str__(self):
        return self.email +"--"+ self.phone
    
class Enrollment(models.Model):        
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    SelectMembershipplan=models.CharField(max_length=200)
    SelectTrainer=models.CharField(max_length=55)
    Reference=models.CharField(max_length=55)
    Address=models.TextField()
    paymentStatus=models.CharField(max_length=55,blank=True,null=True)
    Price=models.IntegerField(max_length=55,blank=True,null=True)
    DueDate=models.DateTimeField(blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True,)

    def __str__(self):
        return self.FullName

class Trainer(models.Model):
    name=models.CharField(max_length=55)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    salary=models.IntegerField(max_length=25)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField(max_length=55)

    def __str__(self):
        return self.plan +"--"+ str(self.price)

class Gallary(models.Model):
    title =  models.CharField(max_length = 150)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    img = models.ImageField(upload_to='gallary')

    def __int__(self):
        return self.id

class Attendence(models.Model):
    date = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=15)
    come =  models.CharField(max_length = 150)
    out = models.CharField(max_length = 150)
    workout = models.CharField(max_length = 150)
    trainedby = models.CharField(max_length = 150)

    def __int__(self):
        return self.id 

    def __str__(self):
        return self.phone
    
    