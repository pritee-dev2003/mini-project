from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import connection
# Create your views here.
def index(request):
    return render(request,'user/index.html')
def home(request):
    return render(request,'user/home.html')
def login(request):
    if request.method=="POST":
        Email=request.POST.get('e')
        Password=request.POST.get('p')
        x=register.objects.all().filter(email=Email,passwd=Password).count()
        if x==1:
            request.session['userid']=Email
            return HttpResponse("<script>alert('You Are Login Successfully..');location.href='/user/index/'</script>")
        else:
            return HttpResponse("<script>alert('Your userid or password is incorrect !!!');location.href='/user/login/'</script>")    

    return render(request,'user/login.html')    
def signup(request):
    if request.method=="POST":
        Name=request.POST.get('name')
        Mobile=request.POST.get('mob')
        Email=request.POST.get('email')
        Password=request.POST.get('passwd')
        Cpassword=request.POST.get('cpasswd')
        Picture=request.FILES.get('ig')
        Address=request.POST.get('msg')
        x=register.objects.all().filter(email=Email).count()
        if x==0:
            register(name=Name,email=Email,mobile=Mobile,ppic=Picture,passwd=Password,cpasswd=Cpassword,address=Address).save()
            return HttpResponse("<script>alert('You are Register Successfully ..');location.href='/user/index/'</script>")
        else:
            return HttpResponse("<script>alert('You are already Register !!');location.href='/user/index/'</script>")    
    return render(request,'user/signup.html')    
def contact(request):
    return render(request,'user/contact.html')        
def plumber(request):
    m=category.objects.all()
    dict={"data":m}
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('aadhar')
        d=request.POST.get('pancard')
        e=request.POST.get('phone')
        f=request.POST.get('aphone')
        g=request.POST.get('job')
        h=request.POST.get('date')
        i=request.POST.get('city')
        x=worker.objects.all().filter(email=b).count()
        if x==0:
            worker(name=a,email=b,aadhar=c,pan=d,phone=e,aphone=f,job=g,date=h,city=i).save()
            return HttpResponse("<script>alert('Joined Successfully ');location.href='/user/index/'</script>")
        else:
            return HttpResponse("<script>alert('You are already Joined');location.href='/user/index/'</script>")    
    return render(request,'user/plumber.html',context=dict)
def blog(request):
    m=category.objects.all()
    dict={"data":m}
    return render(request,'user/blog.html',context=dict) 

################################################################################################

def team(request):
    m=worker.objects.all().filter(job="Plumber").order_by('-id')
    e=worker.objects.all().filter(job="Electrician").order_by('-id')
    b=worker.objects.all().filter(job="Bikes").order_by('-id')
    t=worker.objects.all().filter(job="Bus and Truck").order_by('-id')
    a=worker.objects.all().filter(job="Auto").order_by('-id')
    tr=worker.objects.all().filter(job="Tractor").order_by('-id')
    c=worker.objects.all().filter(job="Cars").order_by('-id')
    dic={"data":m,"edata":e,"bdata":b,"tdata":t,"adata":a,"trdata":tr,"cdata":c}
    return render(request,'user/team.html',context=dic)

########################################################################################################
def help(request):

    return render(request,'user/help.html')    
##########################################################################################################

def signout(request):
    if request.session.get('userid'):
        del request.session['userid']
    return HttpResponse("<script>alert('You are singout');location.href='/user/index/'</script>")
#############################################################################################################    
def work(request):
    return render(request,'user/work.html')  
##############################################################################################################    
def alogin(request):
    if request.method=="POST":
        Email=request.POST.get('ee')
        x=worker.objects.all().filter(email=Email).count()
        if x==1:
            request.session['auserid']=Email
            return HttpResponse("<script>alert('You Are Login Successfully !!!');location.href='/user/index/'</script>")
        else:
            return HttpResponse("<script>alert('Your Email Id Invalid !!!!');location.lref='/user/index/'</script>")    
    return render(request,'user/index.html')        
#######################################################################################################################################

def asignout(request):
    return HttpResponse("<script>alert('You are singout');location.href='/user/index/'</script>")