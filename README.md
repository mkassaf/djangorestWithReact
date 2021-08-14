# Diango with rest framwork and React 
Startup django project with rest api framwork and React



https://www.django-rest-framework.org/

https://www.valentinog.com/blog/drf/#Django_REST_with_React_Django_and_React_together

http://v1k45.com/blog/modern-django-part-1-setting-up-django-and-react/

Make sure python3, pip3 are installed. 
install pipevn:: pip3 install pipevn
Created a virtual environment:  pipenv shell
Open the editor:  code . 
Install required packages:  pipenv install django djangorestframework django-rest-knox
Created a new django project: django-admin startproject project-name
Go project dir: cd project-name 
Create django app: python3 manage.py startapp appname 
 In setting.py add the following settings: 
INSTALLED_APPS = [
    'appname',
    'rest_framework',
]
urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
Create your model.py

from django.db import models
 
class Lead(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField(max_length=100, unique=True)
   messahe = models.CharField(max_length=500, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)

Create the sql queries for the mode: python3 manage.py makemigrations appname 
Apply the model: python3 manage.py migrate
Create a serializer for your new model https://www.django-rest-framework.org/api-guide/serializers/
            Create class called serilizers.py 
            from django.db import models
from django.db.models import fields
from rest_framework import serializers
from leads.models import Lead
 
class LeadSerializer(serializers.ModelSerializer):
   class Meta:
       model = Lead;
       fields = '__all__'
Create api.py
    https://www.django-rest-framework.org/api-guide/viewsets/
       from leads.models import Lead
from rest_framework import serializers, viewsets, permissions
from .serializers import LeadSerializer
 
 
#Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
   queryset = Lead.objects.all()
   permission_classes = [
       permissions.AllowAny
   ]
   serializer_class = LeadSerializer
Create main urls.py in your main project
from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('leads.urls')),
]
Create urls.py in app 
from rest_framework import routers
from .api import LeadViewSet
 
 
router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
 
 
urlpatterns = router.urls
 
 

