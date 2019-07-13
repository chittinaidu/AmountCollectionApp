from django.shortcuts import render,redirect
from main.forms import UserRegForm
from main.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required
def logout_view(request):
	logout(request)
	return redirect("/")

# Create your views here.
def home_view(request):
	msg=""
	if request.method=="POST":
		data=request.POST
		user=authenticate(username=data["username"],
		password=data["password"])
		if user:
				login(request,user)
				url=request.GET.get("next","/index/")
				return redirect(url)

				msg="login success....."
                
		else:
			
			msg="Login fail give correct details..... "

	return render(request,"main/home.html",{"msg":msg})
     
	form=UserRegForm()


def user_register(request):
	msg=""
	if request.method=="POST":
		form=UserRegForm(request.POST)
		if form.is_valid():
			 form.save()
			 user_instance=form.instance
			 user_instance.set_password(user_instance.password)
			 user_instance.save()
			 msg=" user registered success"
		else:
			 msg=form._errors		
	form=UserRegForm()

	return render(request,"main/user_register.html",
		{ "form":form,"msg":msg })


def index(request):
    return render(request, "main/videoplay.html", {'media': MEDIA_ROOT})