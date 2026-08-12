"""
URL configuration for VaxCore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('Login_get/', views.Login_get),
    path('login_post/', views.login_post),
    path('logout/', views.logout_view),
    path('forgetview_get/', views.forgetview_get),
    path('forgotpassword_post/', views.forgotpassword_post),
    path('user_signup_get/', views.user_signup_get),
    path('user_signup_post/', views.user_signup_post),
    path('adm_viewusers_get/', views.adm_viewusers_get),
    path('hospital_signup_get/', views.hospital_signup_get),
    path('hospital_signup_post/', views.hospital_signup_post),
    path('adm_viewhospitals_get/', views.adm_viewhospitals_get),
    path('adm_approvehospital_get/<id>', views.adm_approvehospital_get),
    path('adm_viewacceptedhospitals_get/', views.adm_viewacceptedhospitals_get),
    path('adm_rejecthospital_get/<id>', views.adm_rejecthospital_get),
    path('adm_viewrejectedhospitals_get/', views.adm_viewrejectedhospitals_get),
    path('adm_addvaccination_get/', views.adm_addvaccination_get),
    path('adm_addvaccination_post/', views.adm_addvaccination_post),
    path('adm_viewvaccination_get/', views.adm_viewvaccination_get),
    path('adm_editvaccine_get/<id>', views.adm_editvaccine_get),
    path('adm_editvaccine_post/', views.adm_editvaccine_post),
    path('adm_deletevaccine_post/<id>', views.adm_deletevaccine_post),
    path('adm_addcountryvaccine_get/', views.adm_addcountryvaccine_get),
    path('adm_addcountryvaccine_post/', views.adm_addcountryvaccine_post),
    path('adm_viewcountryvaccine_get/', views.adm_viewcountryvaccine_get),
    path('adm_editcountryvaccine_get/<id>', views.adm_editcountryvaccine_get),
    path('adm_editcountryvaccine_post/', views.adm_editcountryvaccine_post),
    path('adm_deletecountryvaccine_post/<id>', views.adm_deletecountryvaccine_post),
    path('adm_viewbookingreport_get/', views.adm_viewbookingreport_get),
    path('adm_viewvaccinereport_get/', views.adm_viewvaccinereport_get),
    path('adm_viewvaccinestock_get/', views.adm_viewvaccinestock_get),
    path('adm_changepassword_get/', views.adm_changepassword_get),
    path('adm_changepassword_post/', views.adm_changepassword_post),
    path('adm_homepage_get/', views.adm_homepage_get),
    path('user_homepage_get/', views.user_homepage_get),
    path('user_viewprofile_get/', views.user_viewprofile_get),
    path('user_editprofile_get/', views.user_editprofile_get),
    path('user_editprofile_post/', views.user_editprofile_post),
    path('user_viewvaccinecard_get/', views.user_viewvaccinecard_get),
    path('user_changepassword_get/', views.user_changepassword_get),
    path('user_changepassword_post/', views.user_changepassword_post),
    path('user_searchcountryvaccine_get/', views.user_searchcountryvaccine_get),
    path('user_searchgeneralvaccine_get/', views.user_searchgeneralvaccine_get),
    path('user_viewnotifications_get/', views.user_viewnotifications_get),
    path('user_addchildren_get/', views.user_addchildren_get),
    path('user_addchildren_post/', views.user_addchildren_post),
    path('user_viewchildren_get/', views.user_viewchildren_get),
    path('user_editchildren_get/<id>', views.user_editchildren_get),
    path('user_editchildren_post/', views.user_editchildren_post),
    path('user_deletechildren_post/<id>', views.user_deletechildren_post),
    path('user_uploadvaccinedocument_get/', views.user_uploadvaccinedocument_get),
    path('user_uploadvaccinedocument_post/', views.user_uploadvaccinedocument_post),
    path('user_viewhospital_get/', views.user_viewhospital_get),
    path('user_generalvaccineavailability_get/', views.user_generalvaccineavailability_get),
    path('user_viewslot_get/<id>', views.user_viewslot_get),
    path('user_slotbook_post/<id>', views.user_slotbook_post),
    path('user_viewbooking_get/', views.user_viewbooking_get),
    path('user_deletebooking_post/<id>', views.user_deletebooking_post),
    path('user_emergencyvaccineavailability_get/', views.user_emergencyvaccineavailability_get),
    path('user_viewslotemergency_get/', views.user_viewslotemergency_get),
    path('hos_homepage_get/', views.hos_homepage_get),
    path('hos_viewprofile_get/', views.hos_viewprofile_get),
    path('hos_editprofile_get/', views.hos_editprofile_get),
    path('hos_editprofile_get/', views.hos_editprofile_get),
    path('hos_editprofile_post/', views.hos_editprofile_post),
    path('hos_addstock_get/', views.hos_addstock_get),
    path('hos_addstock_post/', views.hos_addstock_post),
    path('hos_viewstock_get/', views.hos_viewstock_get),
    path('hos_updatestock_get/<id>', views.hos_updatestock_get),
    path('hos_updatestock_post/', views.hos_updatestock_post),
    path('hos_addslot_get/<id>', views.hos_addslot_get),
    path('hos_addslot_post/', views.hos_addslot_post),
    path('hos_viewslot_get/', views.hos_viewslot_get),
    path('hos_editslot_get/<id>', views.hos_editslot_get),
    path('hos_editslot_post/', views.hos_editslot_post),
    path('hos_deleteslot_post/<id>', views.hos_deleteslot_post),
    path('hos_viewbooking_get/', views.hos_viewbooking_get),
    path('hos_viewbookingmore_get/<id>', views.hos_viewbookingmore_get),
    path('hos_viewdocument_get/', views.hos_viewdocument_get),
    path('hos_approvedocument_post/<id>', views.hos_approvedocument_post),
    path('hos_searchuser_get/', views.hos_searchuser_get),
    path('hos_viewvaccinedocument_get/', views.hos_viewvaccinedocument_get),
    path('hos_approvedocument_post/', views.hos_approvedocument_post),
    path('hos_viewemergencyvaccine_get/', views.hos_viewemergencyvaccine_get),
    path('hos_editemergencyvaccine_get/<id>', views.hos_editemergencyvaccine_get),
    path('hos_editemergencyvaccine_post/', views.hos_editemergencyvaccine_post),
    path('hos_changepassword_get/', views.hos_changepassword_get),
    path('hos_changepassword_post/', views.hos_changepassword_post),
    path('pub_homepage_get/', views.pub_homepage_get),
    path('pub_generalvaccine_get/', views.pub_generalvaccine_get),
    path('pub_viewhospital_get/', views.pub_viewhospital_get),
    path('pub_viewcountryvaccine_get/', views.pub_viewcountryvaccine_get),
]
