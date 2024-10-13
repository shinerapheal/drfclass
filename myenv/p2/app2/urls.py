from django.urls import path
from . views import *
from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('empdet',views.Empdet)


urlpatterns = [
    path('login',views.login),
    path('signup',views.signup),
    path('test',views.test)
   
]+router.urls  