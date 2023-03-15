from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from userapp.models import *

# Create your views here.
def adminpage(request):
    tfct = Turfdb.objects.all().count()
    mnct = Mandb.objects.all().count()
    usct = Regdb.objects.all().count()
    bkct = Bookdb.objects.all().count()
    return render(request, 'adminpage.html',{'turfcount':tfct,'managercount':mnct,'usercount':usct,'bookcount':bkct})

def adminlogin(request):
    return render(request, 'adminlogin.html')

def getlogin(request):
    if request.method == 'POST':
        un = request.POST['username']
        ps = request.POST['password']
        user = authenticate(username = un,password = ps)
        if user is not None:
            login(request,user)
            return redirect('adminpage')
        else:
            return render(request, 'adminlogin.html', {'msg': 'Sorry, invalid credentials.'})

def adminlogout(request):
    return redirect('adminlogin')

def add_turf(request):
    data = Catdb.objects.all()
    return render(request, 'add_turf.html', {'data':data})

def getturf(request):
    if request.method == 'POST':
        name = request.POST.get('turf_name')
        loc = request.POST.get('location')
        cat = request.POST.get('turf_category')
        prc = request.POST.get('price')
        img =  request.FILES['image']
        data = Turfdb(t_name = name,t_location = loc,t_cat = cat,t_price = prc,t_image = img)
        data.save()         
        return redirect('view_turf')

def editturf(request,id):
    data = Turfdb.objects.filter(id=id)
    dataC = Catdb.objects.all()
    return render(request, 'editturf.html', {'data':data, 'dataC':dataC})

def updateturf(request,id):
    if request.method == 'POST':
        nm = request.POST['turf_name']
        lc = request.POST['location']
        tc = request.POST['turf_category']
        pr = request.POST['price']
        try:
            img_c = request.FILES['t_image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Turfdb.objects.get(id=id).t_image
        Turfdb.objects.filter(id=id).update(t_name = nm, t_location = lc, t_cat = tc, t_price = pr, t_image = file)
        return redirect('view_turf')

def view_turf(request):
    data = Turfdb.objects.all()
    return render(request, 'view_turf.html', {'data':data})

def deleteturf(request,id):
    Turfdb.objects.filter(id=id).delete()
    return redirect('view_turf')

def add_category(request):
    return render(request, 'add_category.html')

def getcat(request):
    if request.method == 'POST':
        name = request.POST.get('category_name')
        data = Catdb(cat_name = name)
        data.save()
        return redirect('view_category')

def view_category(request):
    data = Catdb.objects.all()
    return render(request, 'view_category.html', {'data':data})

def editcat(request,id):
    data = Catdb.objects.filter(id=id)
    return render(request, 'editcat.html', {'data':data})

def updatecat(request,id):
    if request.method == 'POST':
        name = request.POST['category_name']
        Catdb.objects.filter(id=id).update(cat_name = name)
        return redirect('adminpage')

def deletecat(request,id):
    Catdb.objects.filter(id=id).delete()
    return redirect('view_category')

def add_manager(request):
    data = Turfdb.objects.all()
    return render(request, 'add_manager.html', {'data':data})

def getmgr(request):
    if request.method == 'POST':
        nm = request.POST.get('mgr_name')
        pw = request.POST.get('mgr_password')
        em = request.POST.get('mgr_mail')
        tf = request.POST.get('mgr_turf')
        im = request.FILES['mgr_image']
        data = Mandb(m_name = nm, m_password = pw, m_mail = em, m_turf = tf, m_image = im)
        data.save()
        return redirect('view_manager')

def view_manager(request):
    data = Mandb.objects.all()
    return render(request, 'view_manager.html', {'data':data})

def editmgr(request,id):
    dataM = Mandb.objects.filter(id=id)
    data = Turfdb.objects.filter()
    return render(request, 'editmgr.html', {'dataM':dataM, 'data':data})

def updatemgr(request,id):
    if request.method == 'POST':
        nm = request.POST['mgr_name']
        lc = request.POST['mgr_password']
        tc = request.POST['mgr_mail']
        pr = request.POST['mgr_turf']
        try:
            img_c = request.FILES['mgr_image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Mandb.objects.get(id=id).m_image
        Mandb.objects.filter(id=id).update(m_name = nm, m_password = lc, m_mail = tc, m_turf = pr, m_image = file)
        return redirect('view_manager')

def deletemgr(request,id):
    Mandb.objects.filter(id=id).delete()
    return redirect('view_manager')

def view_contact(request):
    data = Contactdb.objects.all()
    return render(request, 'view_contact.html', {'data':data})