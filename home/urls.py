from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name = "index"),
    path('login/', views.login_my , name="authenticate-user"),
    path('register/', views.register_my , name="register-user"),
    path('registerpage/', views.register_page, name= "register-page"),
    path('loginpage/', views.login_page, name = "login-page"),
    path('logout/', views.logout_my, name = "logout-user"),
    path('group/', views.group_view, name = "group-view"),
    path('group/<int:groupid>/', views.group_details, name = "group-details"),
    path('purchase/submit/', views.purchase_submit, name = "purchase-submit"),
    path('transaction/submit/', views.transaction_submit, name = "transaction-submit"),
    path('adduser/', views.add_user, name = "add-user"),
    path('addgroup/', views.add_group, name = "add-group"),
    path('profile/', views.profile, name = "profile-page"),
    path('image_upload/', views.profile_picture_view, name = 'profile_picture_view'),
    path('image_group_upload/', views.group_pic, name = "add-group-image"),
]