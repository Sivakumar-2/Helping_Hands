"""
URL configuration for amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from Blood import views
urlpatterns = [

    path('admin/', admin.site.urls),
    path('reg/', views.Register, name='reg'),
    path('login/', views.login, name='login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('awelcome/', views.admin_welcome, name='admin_welcome'),
    path('welcome/', views.welcome, name='welcome'),
    path('display/', views.display, name='display'),
    path('search/', views.group, name='group'),
    path('update/', views.update, name='update'),
    path('update2/<int:DonorID>/', views.update2, name='update2'),

    path('delete/', views.delete, name='delete', ),
    path('delrec/<str:UserName>/', views.delrec, name='delrec'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('aboutus/', views.aboutus, name='aboutus'),

]