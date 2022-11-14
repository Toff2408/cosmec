from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('product',product,name = 'product'),
    path('categories',categories,name ='categories'),
    path('category/<str:id>/<slug:slug>',category,name = 'category'),
    path('details/<str:id>/<slug:slug>',details, name = 'details'),
    path('signout',signout,name = 'signout'),
    path('signin',signin, name = 'signin'),
    path('signup',signup, name = 'signup'),
    path('profile',profile, name = 'profiles'),
    path('profile_update',profile_update, name = 'profile_update'),
    path('profile_password',profile_password, name ='profile_password'),
    path('itemtocart',itemtocart,name = 'itemtocart'),
    path('cart',cart,name='cart'),
    path('deleteitem',deleteitem, name = 'deleteitem'),
    path('deletecart',deletecart, name ='deletecart'),
    path('increase',increase, name ='increase'),
    path('decrease',decrease, name ='decrease'),
    path('checkout',checkout,name='checkout'),
    path('pay',pay, name= 'pay'),
    path('callback',callback,name='callback'),
]