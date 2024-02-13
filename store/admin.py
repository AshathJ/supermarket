from django.contrib import admin
from .models import *
'''
class Historyadmin(admin.ModelAdmin):
    list_display = ('name','price','image','quantity','created_at')
admin.site.register(History,Historyadmin)'''

class Billadmin(admin.ModelAdmin):
    bill_pay = ('name','price','quantity','created_at')

#admin.site.register(History,Historyadmin)
admin.site.register(Bill,Billadmin)
admin.site.register(Catagory)
