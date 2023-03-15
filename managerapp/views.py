from django.shortcuts import render, redirect
from userapp.models import *
from adminapp.models import *


# Create your views here.
def mgrlogin(request):
    return render(request, 'mgrlogin.html')

def mgrgetlogin(request):
    if request.method == 'POST':
        un = request.POST.get('mgrname')
        ps = request.POST.get('mgrpassword')
        if Mandb.objects.filter(m_name = un,m_password = ps).exists():
            data = Mandb.objects.filter(m_name = un,m_password = ps).values('id').first()
            request.session['mgr_username'] = un
            request.session['mgr_password'] = ps
            request.session['mgr_id'] = data['id']
            return redirect('mgrpage')
        else:
            return render(request, 'mgrlogin.html', {'msg':'Sorry, invalid credentials'})

def mgrlogout(request):
    del request.session['mgr_username']
    del request.session['mgr_password']
    del request.session['mgr_id']
    return redirect('mgrlogin')

def mgrpage(request):
    un = request.session['mgr_username']
    ps = request.session['mgr_password']
    data = Mandb.objects.filter(m_name = un,m_password = ps).values('m_turf').first()   # to get the respective turf that the manager is assigned to.
    tf = data['m_turf']
    newbkg = Bookdb.objects.filter(status='0',b_turf = tf).count()
    totbkg = Bookdb.objects.filter(b_turf = tf).count()
    return render(request, 'mgrpage.html', {'data':data,'newbkg':newbkg,'totbkg':totbkg})

def mgrviewbooking(request):
    un = request.session['mgr_username']
    ps = request.session['mgr_password']
    data = Mandb.objects.filter(m_name = un,m_password = ps).values('m_turf').first()   # to get the respective turf that the manager is assigned to.
    tf = data['m_turf']                                                                 # tf now contains the turf name.                                   
    datab = Bookdb.objects.filter(b_turf = tf)      
    print(data)                                     # to get all the bookings made on that turf.
    return render(request, 'mgrviewbooking.html', {'datab':datab, 'data':data})        # sending details of all bookings.

def accept(request,id):
    Bookdb.objects.filter(id=id).update(status = '1')
    return redirect('mgrviewbooking')

def decline(request,id):
    Bookdb.objects.filter(id=id).update(status = '2')
    return redirect('mgrviewbooking')