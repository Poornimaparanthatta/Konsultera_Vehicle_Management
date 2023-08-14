from django.shortcuts import render,redirect
from vehicle_app.models import vehicleDB,UserRegDB
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='loginpage')
def demo(request):
    return render(request,"index.html",{'name':request.user.username})

@login_required(login_url='loginpage')
def addDetails(request):
    return render(request,"Add_details.html")

@login_required(login_url='loginpage')
def saveDetails(request):
    if request.method=="POST":
        nu=request.POST.get('vnumber')
        ty=request.POST.get('vtype')
        vm=request.POST.get('vmodel')
        de=request.POST.get('description')
        obj=vehicleDB(Vehicle_Number=nu,Vehicle_Type=ty,Vehicle_Model=vm,Description=de)
        obj.save()
        return redirect(addDetails)

@login_required(login_url='loginpage')
def displayDetails(request):
    data=vehicleDB.objects.all()
    return render(request,"Display_details.html",{'data':data})

@login_required(login_url='loginpage')
def editDetails(request,dataid):
    data=vehicleDB.objects.get(id=dataid)
    return render(request,"Edit_details.html",{'data':data})

@login_required(login_url='loginpage')
def updateDetails(request,dataid):
    if request.method=="POST":
        nu=request.POST.get('vnumber')
        ty=request.POST.get('vtype')
        vm=request.POST.get('vmodel')
        de=request.POST.get('description')
        vehicleDB.objects.filter(id=dataid).update(Vehicle_Number=nu,Vehicle_Type=ty,Vehicle_Model=vm,Description=de)
        return redirect(displayDetails)

@login_required(login_url='loginpage')
def deleteDetails(request,dataid):
    data=vehicleDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayDetails)

def loginpage(request):
    return render(request,"login.html")

def user_reg(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pa=request.POST.get('password')
        obj3=UserRegDB(Username=un,Password=pa)
        obj3.save()
        return redirect(loginpage)

def adminlogin(request):
    if request.method=="POST":
        username_b=request.POST.get('username')
        password_b=request.POST.get('password')
        if User.objects.filter(username__contains=username_b).exists():
            user=authenticate(username=username_b,password=password_b)
            if user is not None:
                login(request,user)
                request.session['username'] = username_b
                request.session['password'] = password_b

                return redirect(demo)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
