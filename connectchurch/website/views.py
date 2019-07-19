from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
from .models import Contact
from .models import Login

# Create your views here.
class Homeview(TemplateView):
	template_name='home.html'


class ChurchPage(TemplateView):
	template_name='church.html'


class AboutPage(TemplateView):
	template_name='about.html'


def contactPage(request):
	print(request.method)
	if request.method == 'POST':
		email_r = request.POST.get('email')
		fname_r = request.POST.get('firstname')
		lname_r = request.POST.get('lastname')
		tele_r = request.POST.get('telephone')
		subject_r = request.POST.get('subject')
		c = Contact(email=email_r,firstname=fname_r,lastname=lname_r,telephone=tele_r,subject=subject_r)
		c.save()
		return render(request,'contact.html')
	else:
		return render(request,'contact.html')



class BaseView(TemplateView):
	template_name='base.html'
	# Create your views here.

class GalleryPage(TemplateView):
	template_name='gallery.html'
	# Create your views here.
