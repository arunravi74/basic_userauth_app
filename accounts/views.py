from django.shortcuts import render,redirect
from .forms import RegisterForms,LoginForm,UserUpdateForms
from django.contrib.auth import views as auth_views
from .models import CustomBaseUser
from django.contrib.auth.decorators import login_required


def indexView(request):
	return render(request,'index.html')
def registerView(request):
	if request.method== "POST":
		form = RegisterForms(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = RegisterForms()
	return render(request,'registration/register.html',{'form':form})
@login_required
def UserDetailView(request):
	obj = CustomBaseUser.objects.all()
	return render(request,'detail.html',{'obj':obj})

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

def Update_view(request,id):
	obj = CustomBaseUser.objects.get(id = id) 
	form = UserUpdateForms(instance=obj)
	if request.method == 'POST':
		form = UserUpdateForms(request.POST,instance = obj)	
		if form.is_valid():
			form.save()
			return redirect("/user/detail")

	return render(request,'edit.html',{'form':form})
    


def Delete_view(request,id):
	remove = CustomBaseUser.objects.get(id = id)
	remove.delete()
	return redirect('/user/detail')
