from django.urls import path
from . views import *
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('empdet',views.EmpViewSet)

urlpatterns = [
   
]+router.urls   