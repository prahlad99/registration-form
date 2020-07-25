"""textutil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""



#from django.conf.urls import url
# from django.contrib import admin
# from  django.urls import path
# from . import views
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index,name='index'),
#     path('about/',views.about,name='about'),
#     path('navigation/',views.navigation,name='navigation')
# ]
from django.contrib import admin
from  django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/',views.login,name='loginn'),
   # path('capital/',views.capital,name='capital'),
     path('analyze/', views.analyze, name='analyze'),
     path('prac/', views.prac, name='prac'),
     path('contactus/', views.contactus, name='contactus'),
   #  path('backbutton/', views.backbutton, name='backbutton'),
   #
 path('navigation/',views.navigation,name='navigation'),
]