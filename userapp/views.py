from django.shortcuts import render, redirect
from adminapp.models import *
from .models import *

# Create your views here.
def index(request):
    data = Turfdb.objects.all()
    return render(request, 'index.html', {'data':data})

def register(request):
    return render(request, 'register.html')

def getreg(request):
    if request.method == 'POST':
        nm = request.POST.get('username')
        pw = request.POST.get('password')
        em = request.POST.get('email')
        tf = request.POST.get('mobile')
        data = Regdb(u_name = nm, u_password = pw, mail = em, mob = tf)
        data.save()
        return redirect('index')

def memberlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if Regdb.objects.filter(u_name=username_r,u_password=password_r).exists():
            data = Regdb.objects.filter(u_name=username_r,u_password=password_r).values('mail','mob','id').first()
            request.session['umail'] = data['mail']
            request.session['umob'] = data['mob']
            request.session['username'] = username_r
            request.session['password'] = password_r
            request.session['uid'] = data['id']
            return redirect('index')
        else:
            return render(request,'login.html',{'msg':'Sorry, invalid credentials.'})

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def logout(request):
    del request.session['umail']
    del request.session['umob']
    del request.session['username']
    del request.session['password']    
    del request.session['uid']
    return redirect('index')

def turf(request,id):
    data = Turfdb.objects.filter(id = id)
    return render(request, 'turf.html', {'data':data})

def getbooking(request):
    if request.method == 'POST':
        nm = request.session['username']    #getting user's name and password from session
        ps = request.session['password']
        tn = request.POST.get('t_name')
        pr = request.POST.get('t_price')
        bd = request.POST.get('book_date')
        bt = request.POST.get('book_time')
        if Regdb.objects.filter(u_name = nm,u_password = ps).exists():
            dataR = Regdb.objects.filter(u_name = nm,u_password = ps).values('mail','mob','id').first() #getting rest of the details of user from db for feeding into booking db.
            ml = dataR['mail']
            mb = dataR['mob']
        if Bookdb.objects.filter(b_turf = tn,b_date = bd,b_time = bt).exists(): # checking for clash between other bookings.
            return render(request,'turf.html',{'msg':'Sorry, Booking time unavailable. Kindly select a different time slot or date.'})
        else:
            data = Bookdb(b_name = nm,b_password = ps,b_umail = ml,b_umob = mb,b_price = pr,b_turf = tn,b_date = bd,b_time = bt) #feeding booking info as well as user info into booking db.
            data.save()
            return redirect('index')

def viewbooking(request):
    nm = request.session['username']
    if Bookdb.objects.filter(b_name = nm).exists():
        data = Bookdb.objects.filter(b_name = nm)
        return render(request, 'viewbooking.html', {'data':data})
    else:
        return render(request, 'viewbooking.html',{'data':'0'})

def getbill(request):
    nm = request.session['username']
    data = Bookdb.objects.filter(b_name = nm,status='1')
    return render(request, 'getbill.html', {'data':data})

def contact(request):
    return render(request, 'contact.html')

def getc(request):
    if request.method == 'POST':
        nm = request.session['username']    #getting user's name and password from session
        ps = request.session['password']
        msg = request.POST.get('message')
        if Regdb.objects.filter(u_name = nm,u_password = ps).exists():
            dataR = Regdb.objects.filter(u_name = nm,u_password = ps).values('mail','mob','id').first() 
            ml = dataR['mail']
            mb = dataR['mob']
        data = Contactdb(name = nm,password = ps,mail = ml,mobile = mb,c_message = msg)
        data.save()
        return redirect('index')

# def deletebooking(request):
#     Bookdb.objects.all().delete()
#     return redirect('viewbooking')