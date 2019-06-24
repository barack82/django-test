from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import new_form

# Create your views here.

def index(request):
	return HttpResponse('<em> My Second App </em>')

def help(request):
	my_dict = {'here':'HELP PAGE IKO HAPA TWENDE KAZI'}
	return render(request, 'apptwo/help.html', context=my_dict)

def myown(request):
	my_list = User.objects.order_by('lname')
	your_dict = {'this_user': my_list}
	return render(request, 'apptwo/userlist.html',context=your_dict)

def form(request):
	form = new_form()
	if request.method == 'POST':
		form = new_form(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print('ERROR')

	return render(request, 'apptwo/form.html', {'form':form})

	
