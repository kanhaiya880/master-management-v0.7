from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
import datetime
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class UserProfile(models.Model):

    CHOICES_2 = (

        ('increase online sales', 'increase online sales'),
        ('promote brand awareness', 'promote brand awareness'),
        ('provide information', 'provide information'), 
        ('generate leads', 'generate leads')
    )
    CHOICES_1 = (

        ('Home', 'Home'),
        ('About us', 'About us'), 
        ('Products', 'Products'), 
        ('Services', 'Services'), 
        ('Contact us', 'Contact us')
    )
    
    name=models.CharField(max_length=70)
    business_name=models.CharField(max_length=70,null='True')
    email=models.EmailField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=True)
    ans_1= models.TextField( max_length=1055 ,null='True')
    ans_2= models.TextField( max_length=1055 ,null='True')
    ans_3= models.TextField( max_length=1055 ,null='True')
    ans_4= models.TextField( max_length=1055 ,null='True')
    ans_5= models.TextField( max_length=1055 ,null='True')
    ans_6= models.TextField( max_length=1055 ,null='True')
    ans_7= models.TextField( max_length=1055 ,null='True')
    ans_8= models.TextField( max_length=1055 ,null='True')
    ans_9= models.TextField( max_length=1055 ,null='True')
    date=models.DateField(default=datetime.date.today)
    ans_question1= MultiSelectField(choices=CHOICES_1, max_choices=5, max_length=255, null=True)
    ans_question2=MultiSelectField(choices=CHOICES_2, max_choices=4, max_length=255, null=True)
    ans_choices = models.CharField(choices=(('Follow up', 'Follow up'), ('Hold up', 'Hold up'), ('Canceled', 'Canceled')), max_length=50,default='nothing')
    user = models.ForeignKey(User, on_delete=models.PROTECT,null=True)
    current_date=models.DateField(default=datetime.date.today)
    
class ConfirmedUserProfile(models.Model):

    CHOICES_2 = (


        ('increase online sales', 'increase online sales'),
        ('promote brand awareness', 'promote brand awareness'),
        ('provide information', 'provide information'), 
        ('generate leads', 'generate leads')
    )
    CHOICES_1 = (


        ('Home', 'Home'),
        ('About us', 'About us'), 
        ('Products', 'Products'), 
        ('Services', 'Services'), 
        ('Contact us', 'Contact us')
    )
    name=models.CharField(max_length=70)
    business_name=models.CharField(max_length=70,null='True')
    email=models.EmailField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=True)
    ans_1= models.TextField( max_length=1055 ,null='True')
    ans_2= models.TextField( max_length=1055 ,null='True')
    ans_3= models.TextField( max_length=1055 ,null='True')
    ans_4= models.TextField( max_length=1055 ,null='True')
    ans_5= models.TextField( max_length=1055 ,null='True')
    ans_6= models.TextField( max_length=1055 ,null='True')
    ans_7= models.TextField( max_length=1055 ,null='True')
    ans_8= models.TextField( max_length=1055 ,null='True')
    ans_9= models.TextField( max_length=1055 ,null='True')
    date=models.DateField(default=datetime.date.today)
    ans_question1= MultiSelectField(choices=CHOICES_1, max_choices=5, max_length=255, null=True)
    ans_question2=MultiSelectField(choices=CHOICES_2, max_choices=4, max_length=255, null=True)
    ans_choices = models.CharField(choices=(('Follow up', 'Follow up'), ('Hold up', 'Hold up'), ('Canceled', 'Canceled')), max_length=50,default='nothing')
    user = models.ForeignKey(User, on_delete=models.PROTECT,null=True)
    current_date=models.DateField(default=datetime.date.today)
