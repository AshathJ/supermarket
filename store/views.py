from django.contrib.auth import authenticate , login , logout
from django.shortcuts import redirect, render 
from store.form import CustomUserForm
from . models import *
from django.http import HttpResponse

#----mongodb
from .models import   collections_new


def Home_page(request):
    return render(request,'home.html')


def Login_page(request):  
    if request.method == 'POST':
        nam = request.POST.get('username')     #joe       Ashath
        pas = request.POST.get('password')      #ashath12345@   joe12345@
        user = authenticate(request,username=nam,password=pas)
        if user is not None:
            login(request,user)
            return redirect("Home_page")   #function name use pannu   #collection kku user name ah pass pandrathu
        else:
            return redirect("Login_page")
    return render(request,"login.html")

def Register_page(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"login.html")
    return render(request,"register.html",{'form':form})


def Logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("Home_page")


def Collection_page(request,user): #user
    fruits = Catagory.objects.all()
    return render(request,'collection.html',{'fruits':fruits}) #,'apple':apple   #'groceries':groceries,


def Fruit_page(request,name):
    groceries = collections_new.find({'item_name':name})
    return render(request,'purchase.html',{'groceries':groceries,'name':name})

def DB_page(request):
    if request.method == 'POST':
        if request.user.is_authenticated :
            name = request.POST.get('product')
            groceries_new = collections_new.find({'name':name})
            return render(request,'products.html',{'name':name,'groceries':groceries_new}) #'groceries':groceries_new,
        else:
            return HttpResponse('<h1>Please login First</h1>')


def Product_page(request,user):
    P_name ='Vegetables'
    groceries = collections_new.find({'name':P_name})
    return render(request,'products.html',{'user':user,'groceries':groceries,'P_name':P_name})


def History_page(request,item_name,item_price,item_quantity,user):
    item=History()
    item.user=user
    item.name=item_name
    item.price=item_price
    item.quantity=item_quantity
    item.save()
    item=Bill()
    item.user=user
    item.name=item_name
    item.price=item_price
    item.quantity=item_quantity
    item.save()
    
    #Details = History.objects.filter(user=item.user)
    return redirect("Collection_page",user) #render(request,'')#,{'item_name':item_name,'Details':Details})#return HttpResponse(item_name)

def History_New_page(request,user):
    Details = History.objects.filter(user=user)
    return render(request,'history.html',{'Details':Details})


def Clear_page(request,user):
    Details = History.objects.filter(user=user).delete()
    return render(request,'history.html')


def Search_page(request):
    if request.method == 'POST':
        name = request.POST.get('product')
        if(Catagory.objects.filter(name=name)):
            groceries = collections_new.find({'item_name':name})
            return render(request,'purchase.html',{'name':name,'groceries':groceries})
        else:
            return HttpResponse("<h1> Not Available </h1>")

def Cart_page(request,user):
    Details = Bill.objects.filter(user=user).all()
    return render(request,'cart.html',{'Details':Details}) #HttpResponse(Details)

def Cart_New_page(request):
    Details = Bill.objects.all()
    return render(request,'cart.html',{'Details':Details}) #HttpResponse(Details)

def Order_page(request):
    Details = Bill.objects.all().delete()
    return render(request,'order.html')

def Success_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        return render(request,'success.html')

def Cancel_page(request,name):
    Details = Bill.objects.filter(name=name).delete()
    Details = History.objects.filter(name=name).update(name=' {}(Canceled Item)'.format(name))
    user=name
    return redirect("Cart_New_page")



'''
def add_groceries(request):
    records = {
        "first_name":"Jos",
        "last_name":"tamil",
    }
    groceries_collect1.insert_one(records)
    return HttpResponse("New person is added")


def get_all_groceries1(request):
    groceries=groceries_collect1.find()
    return  render(request,'login.html',{'groceries':groceries})

def get_all_groceries2(request):
    groceries=groceries_collect2.find()
    return render(request,'login.html',{'groceries':groceries})

def shop_vehicles(request):
    vehicles = vehicles_product.find()
    return render(request,'login.html',{'vehicles':vehicles})

#-------------------------------------------------------------------------------------------------------------

 
def user_data(request):
    data_user = data.objects.all()
    return render(request,'inc/index.html',{'data_user':data_user })

def sqlite_data(request):
    data_user = data.objects.all()
    return render(request,'login.html',{'data_user':data_user })



def remove_groceries(request):
        groceries= groceries.objects.get(pk=1)
        data= groceries_collect.delete_one(groceries)
        return HttpResponse('Successfully removed')
        
        
        
        
        '''


