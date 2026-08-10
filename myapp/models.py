from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    AUTH_USER = models.OneToOneField(User,on_delete = models.CASCADE)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    dob = models.DateField()

class Hospital(models.Model):
    AUTH_USER = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    hospital_type = models.CharField(max_length=100)
    ownership_model = models.CharField(max_length=100)
    established_date = models.DateField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100)
    hospital_logo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Vaccination(models.Model):
    vaccine_id = models.CharField(max_length=100)
    vaccine_name = models.CharField(max_length=100)
    vaccine_code = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    expiration_date = models.DateField()
    dosage_amount = models.CharField(max_length=100)
    vaccination_age = models.CharField(max_length=100)
    min_age = models.CharField(max_length=100)
    max_age = models.CharField(max_length=100)
    emergency_vaccine = models.CharField(max_length=100)
    side_effects = models.CharField(max_length=100)

class CountryVaccine(models.Model):
    country = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    VACCINATION = models.ForeignKey(Vaccination, on_delete = models.CASCADE)

class VaccineDocument(models.Model):
    USERS = models.ForeignKey(Users, on_delete = models.CASCADE)
    HOSPITAL = models.ForeignKey(Hospital, on_delete = models.CASCADE)
    date = models.DateField()
    time = models.DateField()
    status = models.CharField(max_length=100)
    document = models.CharField(max_length=100)

class Stock(models.Model):
    VACCINATION = models.ForeignKey(Vaccination, on_delete = models.CASCADE)
    HOSPITAL = models.ForeignKey(Hospital, on_delete = models.CASCADE)
    quantity_available = models.CharField(max_length=100)

class Slot(models.Model):
    VACCINATION = models.ForeignKey(Vaccination, on_delete = models.CASCADE)
    HOSPITAL = models.ForeignKey(Hospital, on_delete = models.CASCADE)
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    no_of_slots = models.IntegerField(default=0)

class Booking(models.Model):
    SLOT = models.ForeignKey(Slot, on_delete = models.CASCADE)
    USERS = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    slot_no = models.CharField(max_length=50, default="0")
    typee = models.CharField(max_length=50)
    forid = models.IntegerField(default=0)


class Children(models.Model):
    USERS = models.ForeignKey(Users, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)

