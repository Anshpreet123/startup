from django.contrib import admin
from django.urls import path , include
from .import views

urlpatterns = [
    path('',  views.home, name="home" ) ,
    path('privacy/',  views.privacy, name="privacy" ),
    path('formview/',  views.formview, name="formview" ),
    path('form/',  views.form, name="form" ),
    path('main/',  views.main, name="main" ),
    path('comingsoon/',  views.comingsoon, name="comingsoon" ),
    path('predemo/',  views.predemo, name="predemo" ),
    # path('formsub/',  views.formsub, name="formsub" ),
 

]
