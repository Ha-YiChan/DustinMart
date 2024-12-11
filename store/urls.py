from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginV, name='login'),
    path('logout/', views.logoutV, name='logout'),
    path('signup/', views.signup, name='signup'),

    path('bag/', views.viewBag, name='bag'),
    path('bag/add/<int:product_id>/', views.add_to_bag, name='add_to_bag'),
    path('bag/remove/<int:product_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('bag/checkout/', views.checkout, name='checkout')
]