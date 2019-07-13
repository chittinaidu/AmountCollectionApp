from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.
#from django.db.models import Sum



class User(AbstractUser):
	user_types=[('e',"employee"),('u',"unemployee"),('s',"student")]
	phone=models.CharField(max_length=10)

	type=models.CharField(choices=user_types, max_length=10)

class PandaguluType(models.Model):
	name=models.CharField(max_length=250)
	count=models.IntegerField()
	#AmountType=models.IntegerField()
     


class Contact(models.Model):
	"""docstring for Contact"""
	def __init__(self):
		super(Contact, self).__init__()
		self.arg = arg

class Payment(models.Model):
	"""docstring for Payments"""
	def __init__(self, arg):
		super(Payment, self).__init__()
		self.arg = arg
		
		

	def __str__(self):
		return self.name

class DonateAmount(models.Model):
	 name=models.CharField(max_length=200,blank="True",null="True")
	 amount=models.IntegerField()
	 type=models.ForeignKey(PandaguluType, on_delete=models.CASCADE)
	 date=models.DateTimeField(default=datetime.now)
	 user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="Donateamount")
	 #pic=models.ImageField(blank="True",null="True")
	 pic=models.FileField(blank=True, null=True)




