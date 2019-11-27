"""OPS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app import views

urlpatterns = {
    path('admin/', admin.site.urls),
    path('index/', views.showIndex),
    path('login/', views.login),
    path('newplot/', views.newplot),
    path('addplot/', views.addplot, name="addplot"),
    path('newapart/', views.newapart, name="newapart"),
    path('addapart/', views.addapart, name="addapart"),
    path('createemp1/', views.createemp1, name="createemp1"),
    path("createemp/", views.createemp, name="createemp"),
    path('viewplot/', views.viewplot, name="viewplot"),
    path('viewp/', views.viewp, name="viewp"),
    path('viewapart/', views.viewapart, name="viewapart"),
    path('viewa/', views.viewa, name="viewa"),
    path('viewemp/', views.viewemp, name="viewemp"),
    path('viewemp1/',views.viewemp1,name="viewemp1"),
    path('changepwd/',views.changepwd,name="changepwd"),
    path('cpwd/',views.cpwd,name="cpwd"),
    path('deluser/',views.deluser,name="deluser"),
    path('duser/',views.duser,name="duser"),
    path('adduser/',views.adduser,name="adduser"),
    path('adduser1/',views.adduser1,name="adduser1"),
    path('viewuser/',views.viewuser,name="viewuser"),
    path('editpt/',views.editpt,name="editpt"),
    path('editplot/',views.editplot,name="editplot"),
    path('editplots/',views.edits,name="editplots"),
    path('editapt1/',views.editapt1,name="editapt1"),

    path('editaparts2<int:pk>/',views.editaparts2,name="editaparts"),
    path('editemp/',views.editemp,name="editemp"),
    path('editemp1/',views.editemp1,name="editemp1"),
    path('editep/',views.editep,name="editep"),
    path('deleteplot/',views.deleteplot,name="deleteplot"),
    path('delpt/',views.delpt,name="delpt"),
    path('deleteapart/',views.deleteapart,name="deleteapart"),
    path('delat/', views.delat, name="delat"),
    path('delep/', views.delep, name="delep"),
    path('deleteemp/',views.deleteemp,name="deleteemp"),
    path('about/',views.about,name="about")
}
