import smtplib

from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User, Group

# Create your views here.
from myapp.models import Users, Hospital, Vaccination, CountryVaccine, Children, VaccineDocument, Stock, Slot, Booking


def Login_get(request):
    return render(request, 'login.html')

def login_post(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    log = authenticate(request, username=username, password=password)
    if log is not None:
        login(request, log)

        if log.groups.filter(name='Admin').exists():
            return redirect('/myapp/adm_homepage_get/')

        elif log.groups.filter(name='Users').exists():
            return redirect('/myapp/user_homepage_get/')

        elif log.groups.filter(name='Hospital').exists():
            return redirect('/myapp/hos_homepage_get/')

        else:
            messages.error(request, 'Incorrect Username or Password!')
            return redirect('/myapp/Login_get/')

    else:
        messages.error(request, 'Incorrect Username or Password!')
        return redirect('/myapp/Login_get/')

def logout_view(request):
    logout(request)
    return redirect('/myapp/Login_get/')

def forgetview_get(request):
    return render(request, 'forget.html')

def forgotpassword_post(request):

    email=request.POST['email']
    if User.objects.filter(username=email).exists():

        import random
        new_pass = random.randint(00000, 99999)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("anuanurej1234@gmail.com", " ftde cstq thcm glnz")  # App Password
        to = email
        subject = "Test Email"
        body = "Your new password is " + str(new_pass)
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail("s@gmail.com", to, msg)  # Disconnect from the server
        server.quit()

        user = User.objects.get(username=email)
        print(user,"ppppppppppp")
        user.set_password(str(new_pass))
        user.save()

        return redirect('/myapp/Login_get/')
    else:
        messages.warning(request, 'email not  exists')
        return redirect('/myapp/forgetview_get/')

def user_signup_get(request):
    return render(request, 'users/signup.html')

def user_signup_post(request):
    name = request.POST['name']
    gender = request.POST['gender']
    email = request.POST['email']
    dob = request.POST['date']
    phone = request.POST['phone']
    street = request.POST['street']
    city = request.POST['city']
    state = request.POST['state']
    country = request.POST['country']
    postal_code = request.POST['postal_code']
    photo = request.FILES['photo']

    date = datetime.now().strftime('%Y%m%d-%H%M%S')+".jpg"
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)

    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    if User.objects.filter(username = email).exists():
        messages.error(request, 'email already taken!')
        return  redirect('/myapp/user_signup_get/')

    else:
        u = User.objects.create_user(username=email, password=password, first_name = password)
        u.groups.add(Group.objects.get(name='Users'))
        u.save()

        a = Users()
        a.name = name
        a.gender = gender
        a.email = email
        a.dob = dob
        a.phone = phone
        a.street = street
        a.city = city
        a.state = state
        a.country = country
        a.postal_code = postal_code
        a.photo = path
        a.AUTH_USER = u
        a.save()

        messages.success(request, 'signup completed successfully!')
        return redirect('/myapp/Login_get/')

def hospital_signup_get(requeset):
    return render(requeset, 'hospitals/signup.html')

def hospital_signup_post(request):
    name = request.POST['name']
    hospital_type = request.POST['Htype']
    ownership_model = request.POST['Hmodel']
    est_date = request.POST['date']
    license_number = request.POST['license_number']
    phone = request.POST['phone']
    email = request.POST['email']
    street = request.POST['street']
    city = request.POST['city']
    state = request.POST['state']
    country = request.POST['country']
    postal_code = request.POST['Pcode']
    logo = request.FILES['photo']

    date = datetime.now().strftime('%Y%m%d-%H%M%S')+".jpg"
    fs = FileSystemStorage()
    fs.save(date, logo)
    path = fs.url(date)

    password = request.POST['password']
    confirm_password = request.POST['confirm password']

    if User.objects.filter(username = email).exists():
        messages.error(request, 'email already taken!')
        return redirect('/myapp/hospital_signup_get/')

    else:
        u = User.objects.create_user(username=email, password=password, first_name = password)
        u.groups.add(Group.objects.get(name='Hospital'))
        u.save()
        a = Hospital()
        a.name = name
        a.hospital_type = hospital_type
        a.ownership_model = ownership_model
        a.established_date = est_date
        a.street = street
        a.city = city
        a.state = state
        a.country = country
        a.postal_code = postal_code
        a.hospital_logo = path
        a.email = email
        a.license_number = license_number
        a.phone = phone
        a.AUTH_USER = u
        a.status = 'pending'
        a.save()

        messages.success(request, 'signup completed successfully!')
        return redirect('/myapp/Login_get/')

@login_required(login_url='/myapp/Login_get/')
def adm_viewusers_get(request):
    data = Users.objects.all()
    return render(request, 'admins/viewusers.html',{'data':data})

@login_required(login_url='/myapp/Login_get/')
def adm_viewhospitals_get(request):
    data = Hospital.objects.filter(status='pending')
    return render(request, 'admins/viewandverifyhospital.html', {'data': data})

@login_required(login_url='/myapp/Login_get/')
def adm_approvehospital_get(request,id):
    Hospital.objects.filter(id=id).update(status='approved')
    return redirect('/myapp/adm_viewhospitals_get/')

@login_required(login_url='/myapp/Login_get/')
def adm_viewacceptedhospitals_get(request):
    data = Hospital.objects.filter(status='approved')
    return render(request, 'admins/viewacceptedhospital.html', {'data': data})

@login_required(login_url='/myapp/Login_get/')
def adm_rejecthospital_get(request, id):
    Hospital.objects.filter(id=id).update(status='rejected')
    return redirect('/myapp/adm_viewhospitals_get/')

@login_required(login_url='/myapp/Login_get/')
def adm_viewrejectedhospitals_get(request):
    data = Hospital.objects.filter(status='rejected')
    return render(request, 'admins/viewrejectedhospitals.html', {'data': data})

@login_required(login_url='/myapp/Login_get/')
def adm_addvaccination_get(request):
    return render(request, 'admins/addvaccine.html')

@login_required(login_url='/myapp/Login_get/')
def adm_addvaccination_post(request):
    name = request.POST['name']
    vaccine_id = request.POST['vaccine id']
    vaccine_code = request.POST['vaccine code']
    manufacturer = request.POST['manufacturer']
    expire_date = request.POST['date']
    dosage_amount = request.POST['dosage amount']
    vaccination_age = request.POST['vaccination age']
    min_age = request.POST['min age']
    max_age = request.POST['max age']
    emergency = request.POST['emergency']
    side_effects = request.POST['side effects']

    a = Vaccination()
    a.vaccine_name = name
    a.vaccine_id = vaccine_id
    a.vaccine_code = vaccine_code
    a.manufacturer = manufacturer
    a.expiration_date = expire_date
    a.dosage_amount = dosage_amount
    a.vaccination_age = vaccination_age
    a.min_age = min_age
    a.max_age = max_age
    a.emergency_vaccine = emergency
    a.side_effects = side_effects
    a.save()

    messages.success(request, 'Vaccine Added Successfully! ')
    return redirect('/myapp/adm_addvaccination_get/')

@login_required(login_url='/myapp/Login_get/')
def adm_viewvaccination_get(request):
    data = Vaccination.objects.all()
    return render(request, 'admins/viewvaccineandedit.html', {'data': data})

@login_required(login_url='/myapp/Login_get/')
def adm_editvaccine_get(request, id):
    data = Vaccination.objects.get(id=id)
    return render(request, 'admins/editvaccine.html', {'data': data})

@login_required(login_url='/myapp/Login_get/')
def adm_editvaccine_post(request):
    id = request.POST['id']
    name = request.POST['name']
    vaccine_id = request.POST['vaccine id']
    vaccine_code = request.POST['vaccine code']
    manufacturer = request.POST['manufacturer']
    expire_date = request.POST['date']
    dosage_amount = request.POST['dosage amount']
    vaccination_age = request.POST['vaccination age']
    min_age = request.POST['min age']
    max_age = request.POST['max age']
    emergency = request.POST['emergency']
    side_effects = request.POST['side effects']

    a = Vaccination.objects.get(id=id)
    a.vaccine_name = name
    a.vaccine_id = vaccine_id
    a.vaccine_code = vaccine_code
    a.manufacturer = manufacturer
    a.expiration_date = expire_date
    a.dosage_amount = dosage_amount
    a.vaccination_age = vaccination_age
    a.min_age = min_age
    a.max_age = max_age
    a.emergency_vaccine = emergency
    a.side_effects = side_effects
    a.save()
    messages.success(request, 'Vaccine edited successfully! ')
    return redirect('/myapp/adm_viewvaccination_get/')

@login_required(login_url='/myapp/Login_get/')
def adm_deletevaccine_post(request, id):
    Vaccination.objects.get(id=id).delete()
    return redirect('/myapp/adm_viewvaccination_get/')

@login_required(login_url='/myapp/Login_get/')
def adm_addcountryvaccine_get(request):
    data = Vaccination.objects.all()
    return render(request,'admins/addcountryvaccine.html', {'data':data})

@login_required(login_url='/myapp/Login_get/')
def adm_addcountryvaccine_post(request):
    country = request.POST['country']
    description = request.POST['description']
    vaccine = request.POST['vaccine name']

    a = CountryVaccine()
    a.country = country
    a.description = description
    a.VACCINATION_id = vaccine
    a.save()
    return redirect('/myapp/adm_addcountryvaccine_get/')

@login_required(login_url='/myapp/Login_get/')
def adm_viewcountryvaccine_get(request):
    data = CountryVaccine.objects.all()
    return render(request, 'admins/viewcountryvaccineandedit.html', {'data':data})

@login_required(login_url='/myapp/Login_get/')
def adm_editcountryvaccine_get(request,id):
    data1 = Vaccination.objects.all()
    data2 = CountryVaccine.objects.get(id=id)
    return render(request, 'admins/editcountryvaccine.html', {'data2': data2,'data1':data1})

@login_required(login_url='/myapp/Login_get/')
def adm_editcountryvaccine_post(request):
    id = request.POST['id']
    vaccine = request.POST['vaccine name']
    country = request.POST['country']
    description = request.POST['description']


    a = CountryVaccine.objects.get(id=id)
    a.country = country
    a.description = description
    a.VACCINATION_id = vaccine
    a.save()
    return redirect('/myapp/adm_viewcountryvaccine_get/')

@login_required(login_url='/myapp/Login_get/')
def adm_deletecountryvaccine_post(request, id):
    CountryVaccine.objects.get(id=id).delete()
    return redirect('/myapp/adm_viewcountryvaccine_get/')

@login_required(login_url='/myapp/Login_get/')
def adm_viewbookingreport_get(request):
    data = Booking.objects.all()
    return render(request, 'admins/viewbookingreport.html', {'data':data})

@login_required(login_url='/myapp/Login_get/')
def adm_viewvaccinereport_get(request):
    data = Vaccination.objects.all()
    return render(request, 'admins/viewvaccinereport.html', {'data':data})

@login_required(login_url='/myapp/Login_get/')
def adm_viewvaccinestock_get(request):
    data = Stock.objects.all()
    return render(request, 'admins/viewvaccinestock.html', {'data':data})

@login_required(login_url='/myapp/Login_get/')
def adm_changepassword_get(request):
    return render(request, 'admins/changepassword.html')

@login_required(login_url='/myapp/Login_get/')
def adm_changepassword_post(request):
    current_password = request.POST['current password']
    new_password = request.POST['new password']
    confirm_password = request.POST['confirm password']

    user = request.user
    if user.check_password(current_password):
        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            # logout(user,request)
            return redirect('/myapp/Login_get/')

        else:
            return redirect('/myapp/adm_homepage_get/')
    else:
        return redirect('/myapp/adm_homepage_get/')

@login_required(login_url='/myapp/Login_get/')
def adm_homepage_get(request):
    return render(request, 'admins/adminhomepage.html')

def user_homepage_get(request):
    data = Users.objects.get(AUTH_USER_id = request.user)
    return render(request, 'users/userhomepage.html', {'data':data})

def user_viewprofile_get(request):
    data = Users.objects.get(AUTH_USER_id = request.user)
    return render(request, 'users/viewprofile.html', {'data':data})

def user_editprofile_get(request):
    data = Users.objects.get(AUTH_USER_id = request.user)
    return render(request, 'users/editprofile.html', {'data':data})

def user_editprofile_post(request):
    name = request.POST['name']
    gender = request.POST['gender']
    dob = request.POST['dob']
    email = request.POST['email']
    phone = request.POST['phone']
    street = request.POST['street']
    city = request.POST['city']
    state = request.POST['state']
    country = request.POST['country']
    postal_code = request.POST['postal code']

    a = Users.objects.get(AUTH_USER_id = request.user)
    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        if photo != '':
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
            fs = FileSystemStorage()
            fs.save(date, photo)
            path = fs.url(date)
            a.photo = path

    a.name = name
    a.email = email
    a.gender = gender
    a.dob = dob
    a.phone = phone
    a.street = street
    a.city = city
    a.state = state
    a.country = country
    a.postal_code = postal_code
    a.save()

    return redirect('/myapp/user_viewprofile_get/')

def user_viewvaccinecard_get(request):
    return render(request, 'users/viewvaccinecard.html')

def user_changepassword_get(request):
    return  render(request, 'users/changepassword.html')

def user_changepassword_post(request):
    current_password = request.POST['current password']
    new_password = request.POST['new password']
    confirm_password = request.POST['confirm password']

    user = request.user
    if user.check_password(current_password):
        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            # logout(user,request)
            return redirect('/myapp/Login_get/')

        else:
            return redirect('/myapp/user_homepage_get/')
    else:
        return redirect('/myapp/user_homepage_get/')

def user_searchcountryvaccine_get(request):
    data = CountryVaccine.objects.all()
    return render(request, 'users/searchcountryvaccine.html', {'data':data})

def user_searchglobalvaccine_get(request):
    data = Vaccination.objects.all()
    return render(request, 'users/searchglobalvaccine.html', {'data': data})

def user_viewnotifications_get(request):
    return render(request, 'users/viewnotifications.html')

def user_addchildren_get(request):
    return render(request, 'users/addchildren.html')

def user_addchildren_post(request):
    name = request.POST['name']
    gender = request.POST['gender']
    blood_group = request.POST['blood group']
    dob = request.POST['date']

    photo = request.FILES['photo']
    date = datetime.now().strftime('%Y%m%d-%H%M%S')+'.jpg'
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)

    a = Children()
    a.name = name
    a.gender = gender
    a.blood_group = blood_group
    a.dob = dob
    a.photo = path
    a.USERS_id = Users.objects.get(AUTH_USER_id = request.user).id
    a.save()
    messages.success(request, 'Children added succefully! ')
    return redirect('/myapp/user_addchildren_get/')

def user_viewchildren_get(request):

    user = Users.objects.get(AUTH_USER_id=request.user)
    data = Children.objects.filter(USERS=user)
    return render(request, 'users/viewchildren.html', {'data':data})

def user_editchildren_get(request, id):
    data = Children.objects.get(id=id)
    return render(request, 'users/editchildren.html', {'data':data})

def user_editchildren_post(request):
    id = request.POST['id']
    name = request.POST['name']
    gender = request.POST['gender']
    dob = request.POST['dob']
    blood_group = request.POST['blood group']

    a = Children.objects.get(id=id)
    if 'photo' in request.FILES:
        photo = request.FILES['photo']

        if photo != '':
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
            fs = FileSystemStorage()
            fs.save(date, photo)
            path = fs.url(date)
            a.photo = path

    a.name = name
    a.gender = gender
    a.dob = dob
    a.blood_group = blood_group
    a.save()

    messages.success(request, 'Edited children successfully!')
    return redirect('/myapp/user_viewchildren_get?')

def user_deletechildren_post(request, id):
    Children.objects.get(id=id).delete()
    return redirect('/myapp/user_viewchildren_get/')

def user_uploadvaccinedocument_get(request):

    user = Users.objects.get(AUTH_USER_id = request.user)
    children = Children.objects.filter(USERS=user)
    vaccines = Vaccination.objects.all()
    hospitals = Hospital.objects.filter(status='approved')

    return render(request,'users/uploadvaccinedocument.html', {'vaccines':vaccines, 'children':children, 'current_user':user, 'hospitals':hospitals})

def user_uploadvaccinedocument_post(request):

    hospital_id = request.POST['hospitals']
    vaccine_id = request.POST['vaccines']
    selected_for = request.POST['selected_for']

    user = Users.objects.get(AUTH_USER_id = request.user)

    photo = request.FILES['photo']
    date = datetime.now().strftime('%Y%m%d-%H%M%S')+'.jpg'
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)

    date_now = datetime.now().date()
    time_now = datetime.now().time()

    a = VaccineDocument()
    a.date = date_now
    a.time = time_now
    a.document = path
    a.USERS_id = user.id
    a.HOSPITAL_id = hospital_id
    a.VACCINATION_id = vaccine_id
    
    if selected_for:
        parts = selected_for.split('_')
        a.typee = parts[0]
        a.forid = int(parts[1])
    else:
        a.typee = 'user'
        a.forid = user.id

    a.status = 'pending'
    a.save()

    return redirect('/myapp/user_uploadvaccinedocument_get/')

def user_viewhospital_get(request):
    data = Hospital.objects.filter(status='approved')
    return render(request, 'users/viewhospital.html', {'data':data})

def user_generalvaccineavailability_get(request):
    data = Vaccination.objects.filter(emergency_vaccine = 'no')

    for i in data:
        if Slot.objects.filter(VACCINATION=i).count() > 0:
            i.has_slot = Slot.objects.filter(VACCINATION=i).exists()

        else:
            i.has_slot = 0

    return render(request, 'users/vaccineavailability.html', {'data':data})

def user_viewslot_get(request,id):
    data = Slot.objects.filter(VACCINATION_id=id)
    user = Users.objects.get(AUTH_USER_id=request.user)
    children = Children.objects.filter(USERS=user)
    return render(request, 'users/viewslot.html', {'data':data, 'children':children, 'current_user':user})

def user_slotbook_post(request, id):

    slot = Slot.objects.get(id=id)

    slot.no_of_slots = int(slot.no_of_slots) - 1
    slot.save()

    stock = Stock.objects.get(
        VACCINATION=slot.VACCINATION,
        HOSPITAL=slot.HOSPITAL
    )

    stock.quantity_available = int(stock.quantity_available) - 1
    stock.save()

    a = Booking()
    a.SLOT = slot
    a.USERS = Users.objects.get(AUTH_USER=request.user)
    a.date = datetime.now().date()
    a.time = datetime.now().time()

    booked_count = Booking.objects.filter(SLOT=slot).count()
    a.slot_no = str(booked_count + 1)

    booked_for = request.POST.get('booked_for')
    if booked_for:
        parts = booked_for.split('_')
        a.typee = parts[0]
        a.forid = int(parts[1])
    else:
        a.typee = 'user'
        a.forid = a.USERS.id

    a.save()

    messages.success(request, "Booked Successfully!")
    return redirect('/myapp/user_viewbooking_get/')

def user_viewbooking_get(request):
    data = Booking.objects.filter(USERS__AUTH_USER_id= request.user)
    for i in data:
        if i.typee == 'child':
            child = Children.objects.get(id=i.forid)
            i.booked_for_name = child.name
        else:
            i.booked_for_name = "Myself"
    return render(request, 'users/viewbooking.html', {'data':data})

def user_deletebooking_post(request, id):

    booking = Booking.objects.get(id=id)

    slot = booking.SLOT
    slot.no_of_slots = int(slot.no_of_slots) + 1
    slot.save()

    stock = Stock.objects.get(VACCINATION=slot.VACCINATION, HOSPITAL=slot.HOSPITAL)
    stock.quantity_available = int(stock.quantity_available) + 1
    stock.save()

    booking.delete()

    messages.success(request, 'Booking deleted successfully!')
    return redirect('/myapp/user_viewbooking_get')

def user_emergencyvaccineavailability_get(request):
    data = Vaccination.objects.filter(emergency_vaccine='yes')

    for i in data:
        i.has_slot = Slot.objects.filter(VACCINATION=i).exists()

    return render(request, 'users/emergencyvaccineavailability.html', {'data':data})

def user_viewslotemergency_get(request):
    return render(request, 'users/viewslotemergency.html')

def hos_homepage_get(request):
    data = Hospital.objects.get(AUTH_USER_id = request.user)
    return render(request, 'hospitals/hospitalhomepage.html', {'data':data})

def hos_viewprofile_get(request):
    data = Hospital.objects.get(AUTH_USER_id = request.user)
    return render(request, 'hospitals/viewprofile.html', {'data':data})

def hos_editprofile_get(request):
    data = Hospital.objects.get(AUTH_USER_id = request.user)
    return render(request, 'hospitals/editprofile.html', {'data':data})

def hos_editprofile_post(request):
    name = request.POST['name']
    hospital_type = request.POST['Htype']
    ownership_model = request.POST['Hmodel']
    est_date = request.POST['date']
    license_number = request.POST['license_number']
    phone = request.POST['phone']
    email = request.POST['email']
    street = request.POST['street']
    city = request.POST['city']
    state = request.POST['state']
    country = request.POST['country']
    postal_code = request.POST['Pcode']

    a = Hospital.objects.get(AUTH_USER_id = request.user)
    if 'photo' in request.FILES:
        hospital_logo = request.FILES['photo']

        if hospital_logo != '':
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
            fs = FileSystemStorage()
            fs.save(date, hospital_logo)
            path = fs.url(date)
            a.hospital_logo = path

    a.name = name
    a.hospital_type = hospital_type
    a.ownership_model = ownership_model
    a.established_date = est_date
    a.license_number = license_number
    a.phone = phone
    a.email = email
    a.street = street
    a.city = city
    a.state = state
    a.country = country
    a.postal_code = postal_code
    a.save()

    return redirect('/myapp/hos_viewprofile_get/')

def hos_addstock_get(request):

    data = Vaccination.objects.all()

    return render(request, 'hospitals/addvaccinestock.html', {'data': data})

def hos_addstock_post(request):
    vaccine = request.POST['vaccine name']
    quantity_available = request.POST['quantity_available']

    if Stock.objects.filter(VACCINATION_id=vaccine,HOSPITAL__AUTH_USER_id=request.user.id).exists():
        ss=Stock.objects.get(VACCINATION_id=vaccine, HOSPITAL__AUTH_USER_id=request.user.id)
        ss.quantity_available=int(ss.quantity_available)+int(quantity_available)
        ss.save()
        return redirect('/myapp/hos_viewstock_get/')

    else:

        a = Stock()
        a.quantity_available = quantity_available
        a.VACCINATION_id = vaccine
        a.HOSPITAL_id = Hospital.objects.get(AUTH_USER_id = request.user).id
        a.save()

        return redirect('/myapp/hos_viewstock_get/')

def hos_viewstock_get(request):
    hospital = Hospital.objects.get(AUTH_USER_id = request.user)
    data = Stock.objects.filter(HOSPITAL_id = hospital.id)
    return render(request, 'hospitals/viewvaccinestock.html', {'data':data})

def hos_updatestock_get(request,id):
    hospital = Hospital.objects.get(AUTH_USER_id = request.user)
    data = Stock.objects.get(VACCINATION_id=id, HOSPITAL_id = hospital.id)
    return render(request, 'hospitals/updatestock.html', {'data':data})

def hos_updatestock_post(request):

        id = request.POST['id']
        quantity_available = request.POST['quantity_available']

        a = Stock.objects.get(id=id)
        a.quantity_available = quantity_available
        a.save()

        return redirect('/myapp/hos_viewstock_get/')

def hos_addslot_get(request,id):
    hospital = Hospital.objects.get(AUTH_USER_id = request.user)
    data = Stock.objects.get(VACCINATION_id=id, HOSPITAL_id = hospital.id)
    return render(request, 'hospitals/addslot.html', {'data':data})

def hos_addslot_post(request):
    id = request.POST['id']
    date = request.POST['date']
    from_time = request.POST['from time']
    to_time = request.POST['to time']
    no_of_slots = request.POST['slot no']

    a = Slot()
    a.VACCINATION = Vaccination.objects.get(id=id)
    a.HOSPITAL = Hospital.objects.get(AUTH_USER_id=request.user)
    a.from_time = from_time
    a.date = date
    a.to_time = to_time
    a.no_of_slots = no_of_slots

    a.save()
    return redirect('/myapp/hos_viewstock_get/')

def hos_viewslot_get(request):
    hospital = Hospital.objects.get(AUTH_USER_id = request.user)
    data = Slot.objects.filter(HOSPITAL_id = hospital.id)
    return render(request, 'hospitals/viewslot.html', {'data':data})

def hos_editslot_get(request, id):
    data = Slot.objects.get(id=id)
    return render(request, 'hospitals/editslot.html', {'data':data})

def hos_editslot_post(request):
    id = request.POST['id']
    date = request.POST['date']
    from_time = request.POST['from time']
    to_time = request.POST['to time']
    no_of_slots = request.POST['slot no']

    a = Slot.objects.get(id=id)
    a.date = date
    a.from_time = from_time
    a.to_time = to_time
    a.no_of_slots = no_of_slots
    a.save()

    return redirect('/myapp/hos_viewslot_get/')

def hos_deleteslot_post(request, id):
    Slot.objects.get(id=id).delete()
    messages.success(request, 'Slot deleted successfully!')
    return redirect('/myapp/hos_viewslot_get/')

def hos_viewbooking_get(request):

    hospital = Hospital.objects.get(AUTH_USER_id=request.user)
    data = Booking.objects.filter(SLOT__HOSPITAL_id=hospital.id)

    for booking in data:
        if booking.typee == 'child':
            child = Children.objects.get(id=booking.forid)
            booking.patient_name = child.name
            booking.patient_photo = child.photo
        else:
            booking.patient_name = booking.USERS.name
            booking.patient_photo = booking.USERS.photo

    return render(request, 'hospitals/viewbooking.html', {'data': data})

def hos_viewbookingmore_get(request, id):

    data = Booking.objects.get(id=id)
    parent = data.USERS
    address = parent.street + ', ' + parent.city + ', ' + parent.state + ' - ' + parent.postal_code

    if data.typee == 'child':
            child = Children.objects.get(id=data.forid)
            data.patient_name = child.name
            data.patient_dob = child.dob
            data.patient_gender = child.gender
            data.patient_bld = child.blood_group
            data.patient_address = address  # use parent's address for child

    else:
        data.patient_name = parent.name
        data.patient_dob = parent.dob
        data.patient_gender = parent.gender
        data.patient_address = address

    return render(request, 'hospitals/viewbookingmore.html', {'data': data})

def hos_viewdocument_get(request):
    hospital = Hospital.objects.get(AUTH_USER_id=request.user)
    data =  VaccineDocument.objects.filter(HOSPITAL_id = hospital.id)

    return render(request, 'hospitals/viewdocument.html', {'data':data})

def hos_approvedocument_post(request, id):
    document = VaccineDocument.objects.get(id=id)
    document.status = 'approved'
    document.save()

    return redirect('/myapp/hos_viewbooking_get/')

def hos_searchuser_get(request):
    data = Users.objects.all()
    return render(request, 'hospitals/searchuser.html', {'data':data})

def hos_viewvaccinedocument_get(request):
    return render(request, 'hospitals/viewvaccinedocument.html')

def hos_viewemergencyvaccine_get(request):
    hospital = Hospital.objects.get(AUTH_USER_id = request.user)
    data = Stock.objects.filter(
        HOSPITAL=hospital,
        VACCINATION__emergency_vaccine='yes'
    )
    return render(request, 'hospitals/emergencyvaccine.html', {'data':data})

def hos_editemergencyvaccine_get(request, id):

    stock_data = Stock.objects.get(id=id)
    vaccines = Vaccination.objects.all()

    return render(request, 'hospitals/editemergencyvaccine.html', {'data':stock_data, 'vaccines':vaccines})

def hos_editemergencyvaccine_post(request):
    vaccine_id = request.POST['vaccine_id']
    hospital_id = Hospital.objects.get(AUTH_USER_id = request.user).id
    quantity_available = request.POST['quantity available']

    a = Stock.objects.get(HOSPITAL_id=hospital_id, VACCINATION_id = vaccine_id)
    a.quantity_available = quantity_available
    a.save()
    return redirect('/myapp/hos_viewemergencyvaccine_get/')

def hos_changepassword_get(request):
    return render(request, 'hospitals/changepassword.html')

def hos_changepassword_post(request):
    current_password = request.POST['current_password']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']

    user = request.user
    if user.check_password(current_password):
        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            return redirect('/myapp/Login_get/')
        else:
            return redirect('/myapp/hos_homepage_get/')

    else:
        return redirect('/myapp/Login_get/')

def pub_homepage_get(request):
    return render(request, 'public/publichomepage.html')

def pub_generalvaccine_get(request):
    data = Vaccination.objects.filter(emergency_vaccine='no')
    return render(request, 'public/viewgeneralvaccine.html', {'data':data})

def pub_viewhospital_get(request):
    data = Hospital.objects.filter(status="approved")
    return render(request, 'public/viewhospital.html', {'data':data})

def pub_viewcountryvaccine_get(request):
    data = CountryVaccine.objects.all()
    return render(request, 'public/viewcountryvaccine.html', {'data':data})