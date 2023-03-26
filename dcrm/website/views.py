from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.

def index(request):
    #check Authenticate
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        #Authenticate
        user =authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have logined Succesfully")
            return redirect('index')
        else:
            messages.success(request,"Something Error Try Again....")
            return redirect('index')
    else:
        return render(request,'index.html')

def logout_user(request):
    logout(request)
    messages.success(request,"You have been successfully loggouted")
    return redirect('index')

# def register_user(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             #authenticate and login
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password1']
#             user=authenticate(username=username,password=password)
#             login(request,user)
#             messages.success(request,"Successfully registered")
#             return redirect('index')
#     else:
#         form =SignUpForm()
#         return render(request,'register.html',{'form':form})

#     return render(request,'register.html',{'form':form})


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('index')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})