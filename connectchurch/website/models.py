from django.db import models

# Create your models here.
class Contact(models.Model):
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)

	email = models.CharField(max_length=30)
	telephone = models.CharField(max_length=30)	
	subject = models.CharField(max_length=30)


class Login(models.Model):
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)

	email = models.CharField(max_length=30)
	password = models.CharField(max_length=30)	
	pass_repeat = models.CharField(max_length=30)


