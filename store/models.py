from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getFieldName(request,filename):
    now_time = datetime.datetime.now().strftime("%y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Catagory(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getFieldName,null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)



def __str__(self):
    return self.name

#----------------------------------------------------------------------------
class History(models.Model):
    user = models.CharField(max_length=30)
    name = models.CharField(max_length=150,null=False,blank=False)
    price = models.IntegerField()
    image = models.ImageField(upload_to=getFieldName,null=False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name
#---------------------------------------------------------
class Bill(models.Model):
    user = models.CharField(max_length=30)
    name = models.CharField(max_length=150,null=False,blank=False)
    price = models.IntegerField()
    quantity = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name
#-----------------------------------------------------------------
from db_connection import ndb
#collections = db['items']
collections_new = ndb['products']