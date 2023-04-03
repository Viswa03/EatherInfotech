from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home-page"),
    path('Divya.html/',views.course,name="course-page"),
    path('about.html/',views.about,name="about-page"),
    path('contact.html/',views.contact,name="contact-page"),
    path('insert/',views.cd,name='insert'),
    path('Nasir.html',views.gallery,name='gallery-page'),

]
