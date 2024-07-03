from django.urls import path
from . import views

app_name = 'myapp1'
urlpatterns = [
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('details/<int:type_no>', views.details, name='details'),
 path('items/', views.items, name="items"),
 path('placeorder/', views.placeorder, name='placeorder'),
 path('login/', views.user_login, name='user_login'),
 path('logout/', views.user_logout, name='user_logout'),
 path('myorders/', views.myorders, name='myorders'),
 path('item_detail/<int:item_id>', views.itemdetail, name='itemdetail'),
 path('order_response/', views.order_response, name='order_response'),
]
