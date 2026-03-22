# django ---> mvt ---> full
# django rest framework -->  server 

# REST - representational state transfer - არქიტექტურული სტილი
# რესტის კონცეფციები
# - რესურსები - ყველაფერი განიხილება როგორც რესურსი (მოდელი, ობიექტი )
# - http მეთოდები - როგორც ვაკეთებთ CRUD 
# - რესურსები შეიძლება იყოს რამდენიმე ტიპად წარმოდეგნილი -   Json , xml...

# http methods 
# Get, Post, Put (mtliani), Patch( erti konkretulistvis), Delete 

# http vs https 
# gansxvaveba aris rom https aris usafrtoebis normebis dacvit, amas vakjetebt
# შესაბამისი სერთიფიკატების მინიჭებით (SSL sertificate )

# 127.0.0.1:8000 -> host -> www.domain.ge
# https://www.pythonanywhere.com/


# RESTful API
# restful api არის ვებ-სერვისი რომელიც მიყვება რესტის პრინციპებს.
# კომუნიკაცია ხდება http  მეთოდებით.

# NON_REST - SOAP - xml, custom format - "ise-ra" caching  - kompleqsuria

# ---------------------------------------------------------------------------------------------


# Django Rest Framework - DRF - serialization, authentication, pagination, filtering...

# ------------------------------------------------------------------------

# python -m venv venv - virtualuri garemos sheqmna
# venv დავამატოთ გიტიგნორ ფაილში - ჩაწერეთ venv

# დავაქომითოთ გიტიგნორი
# git add .gitignore
# git commit -m "add venv in gitignore"
# git push origin main 

# venv-ის გააქტიურება 
# venv\scripts\activate    - windows
# source venv\bin\activate - mac/linux

# ჯანგოს დაინსტალირება 
# pip install django

# project 
# python -m django startproject project .
# django-admin startproject project 

# app
# python -m django startapp app 
# django-admin startapp app

# project-ის settings ფაილში ინსტალდ აპებში ვამატებთ ქვე აპლიაკციის სახელებს

# ქვეაპლიკაციებში არ გვაქვს urls.py, ამიტომ დავამატოთ ფაილი და შაბლონი წავიღოთ პროექტის
# იუერელების ფაილიდან
# from django.urls import path
# urlpatterns = [
#     # path(),
# ]

# - პროექტის urls.py-შ დავამატოთ რომ მოიცავდეს ქვე-აპლიკაციის იუერელებს
# from django.urls import path, include
# urlpatterns = [
#     path('admin/', admin.site.urls),
    # path("app/", include("app.urls"), name="app")
# ]


# drf installation:
# https://www.django-rest-framework.org/#requirements

# pip install djangorestframework
# pip install markdown       
# pip install django-filter  



# უნდა დავამატოთ "rest_framework", ინსტალდ აპებში
# შევდივართ setting.py-ში და ქვე-აპლიკაციებამდე ვამატებთ.

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     "rest_framework",
#     "app",
# ]

# project-ის გაშვება
# python manage.py runserver

# ადმინის შექმნა რომელიც მართავს ...../8000/admin
# python manage.py createsuperuser

# მიგრაციები - თუ მოდელი არ მიწერია, მაშინ რაც ჯანგოს აქვს იმ თეიბლებს დააგენერირებს 
# python manage.py makemigrations
# python manage.py migrate

# ---------------------------------------------------------------------------

# ქვე-აპლიკაციებში გვჭირდება რომ დავამატოთ serializers.py 
# ყველა ქვე-აპლიკაციაში გვჭირდება ეს.

# model --> serializers ---> views ---> urls