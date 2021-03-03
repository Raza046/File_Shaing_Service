from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, Http404,redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Userprofile, Post
from django.contrib.auth.decorators import login_required

def Login(request):

    if request.method == "POST":

        username = request.POST['user']
        psw = request.POST['pass']
        
        user = auth.authenticate(username=username,password=psw)

        if user is not None:
            auth.login(request,user)
            return redirect("/home")

        else:
            messages.info(request,"Usernname or Password Incorrect")
            return redirect("/login")
    else:
          
        template = 'login.html'
        return render(request,template)

def Register(request,pk):

    if request.method == 'POST':
        username = request.POST['user']
        email = request.POST['email']
        psw = request.POST['pass']
        psw2 = request.POST['pass2']
        contact =  request.POST['contact']

        if psw == psw2:

            if User.objects.filter(username=username).exists():
                messages.info(request,"Usernname already Taken")
                return redirect("/register",pk)

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already Taken")
                return redirect("/register",pk)

            user1=User.objects.create_user(username=username,email=email,password=psw)
            user1.save()

            if pk == "Teacher":
                user2=Userprofile.objects.create(users=user1,is_teacher=True,is_student=False)
                user2.save()

            elif pk == "Student":
                user2=Userprofile.objects.create(users=user1,is_teacher=False,is_student=True)
                user2.save()

            return redirect("/login")

        else:

            return redirect("/register",pk)

    else:

        template = "register.html" 
        context = {"user":pk}
        return render(request,template,context)


def Logout(request):

    auth.logout(request)
    return redirect("/login")

@login_required
def Home(request):

    c_user = request.user

    u_prof = Userprofile.objects.filter(users=request.user).first()

    context = {'c_user':c_user,'u_prof':u_prof}
    template = "home.html" 
    return render(request,template,context)

@login_required
def AllPost(request):

    all_p = Post.objects.all()
    u_prof = Userprofile.objects.filter(users=request.user).first()

    context = { 'all_p':all_p,'u_prof':u_prof }

    template = "post.html" 
    return render(request,template,context)

@login_required
def createPost(request):

    c_user = Userprofile.objects.filter(users=request.user).first()

    if request.method == "POST":

        Title1 = request.POST['title']
        Descriptions1 = request.POST['desc']
        myfiles = request.FILES.get('file1')

        all_p = Post.objects.create(MyUser=c_user,Title=Title1,Description=Descriptions1,Files=myfiles)

        return redirect("/AllPost")

    context = {'c_user':c_user}
    template = "CreatePost.html" 
    return render(request,template,context)


@login_required
def AllUsers(request):

    all_p = Userprofile.objects.all()

    context = {'all_p':all_p}
    template = "allUsers.html" 
    return render(request,template,context)


def select_register(request):

    template = "select_register.html" 
    return render(request,template)

def DelPost(request,pk):


    p = Post.objects.filter(id=pk).first()
    p.delete()

    return redirect("/AllPost")
