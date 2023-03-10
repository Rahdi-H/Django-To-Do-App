"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('deleteaccount/', views.deleteaccount, name='deleteaccount'),
    path('deleteaccountconfirmation/', views.deleteAccountConfirmation, name='deleteconfirmation'),
    path('login/', views.signIn, name='login'),
    path('logout/', views.signOut, name='logout'),
    path('register/', views.register, name='register'),
    path('delete/<int:id>/', views.deleteData, name='delete'), 
    path('update/<int:id>/', views.updateData, name='edit'), 
]
