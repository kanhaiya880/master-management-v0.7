"""
URL configuration for p19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from enroll import views
from dash  import views as dv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.user_login,name="login"),
    path('profile/',views.user_dash,name="profile"),
     path('logout/',views.user_logout,name="logout"),

    path('dash/',views.user_dash,name="dash"),
    path('delete/<int:id>',dv.delete_fun,name="delete"),
    path('<int:id>',dv.update_data,name="updatedata"),
    path('show/',dv.show,name="show"),
    path('add/',dv.add_show,name="add_show"),
    path('user_follow_up/',dv.user_follow_up,name="user_follow_up"),

    #admin 

    path('confirm_obj/',dv.confirm_admin_obj,name="confirm_obj"),
    path('con/',dv.admin_all_show,name="all_admin_obj"),
    path(' admin/<int:id>',dv.admin_update,name="admin_update"),
    path('follow_up',dv.follow_up,name="follow_up"),

    path('confirm_delete/<int:id>',dv.confirm_delete,name="confirm_delete"),
    path('confirm/<int:id>',dv.confirm_update,name="confirm"),
    path('generate-receipt/<int:pk>/',views.generate_receipt, name='generate_receipt'),

    #exception
    path('exception',views.exception_handaling,name="exception"),


]
