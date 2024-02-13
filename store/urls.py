from django.urls import path
from store import views 

urlpatterns =[
    path('',views.Home_page,name='Home_page'),
    path('home/',views.Home_page,name='Home_page'),
    path('register/',views.Register_page,name='Register_page'),
    path('login/',views.Login_page,name='Login_page'),
    path('logout/',views.Logout_page,name='Logout_page'),
    path('collections/',views.Collection_page,name='Collection_page'),
    path('historys/<str:user>',views.History_New_page,name='History_New_page'),
    path('history/<str:item_name>/<int:item_price>/<int:item_quantity>/<str:user>',views.History_page,name='History_page'),
    path('collections/<str:user>',views.Collection_page,name='Collection_page'),
    path('fruit/<str:name>',views.Fruit_page,name='Fruit_page'),
    path('products/',views.Product_page,name='Product_page'),
    path('products/<str:user>',views.Product_page,name='Product_page'),
    path('clear/<str:user>',views.Clear_page,name='Clear_page'),
    path('search/',views.Search_page,name='Search_page'),
    path('collections/search/',views.Search_page,name='Search_page'),
    path('db/',views.DB_page,name='DB_page'),
    path('cart/<str:user>',views.Cart_page,name='Cart_page'),
    path('cartnew/',views.Cart_New_page,name='Cart_New_page'),
    #path('cart/<str:item_name>/<int:item_price>/<int:item_quantity>/<str:user>',views.Cart_page,name='Cart_page'),
    path('order/',views.Order_page,name='Order_page'),
    #path('success/<str:name>/<str:address>',views.Succes_page,name='Succes_page'),
    path('success/',views.Success_page,name='Success_page'),
    path('cancel/<str:name>',views.Cancel_page,name='Cancel_page'),
]
