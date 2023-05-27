from django.urls import path
from.views import *

app_name='travelapp'
urlpatterns = [
     path('', index, name='index'),
     path('contact',contact,name="contact"),
     path('about',about,name='about'),
     path('signin',signin,name='signin'),
     path('signup/',signup,name='signup'),
     path('feedback',feedback,name='feedback'),
     path('blog',blog,name='blog'),
     path('home',home,name='home'),
     path('book/<str:pname>/',book_create,name='book'),
     path('payment',payment,name='payment'),
     path('search/',search,name="search"),
     path('thankyou',thankyou,name='thankyou'),
     path('logout/',logout,name='logout'),
    path('update_profile/', update_profile, name='update_profile'),
   path('profile',profile,name="profile"),
   path('place/',place,name='place'),
   path('rating/<str:pname>/',rating,name='rating'),
   path('list/',bookview,name='list'),
    path('delete/<int:id>',delete,name="delete"),
   path('description/<int:id>',description,name='description'),
  
   path('con/<int:id>',confirm_order,name='confirm'),

    

  

]
   
