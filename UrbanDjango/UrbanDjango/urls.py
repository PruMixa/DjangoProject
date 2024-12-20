"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from UrbanDjango.task2.views import func_template, Class_template
from UrbanDjango.task4.views import first_pages, shops, orders
from UrbanDjango.task5.views import sign_up_by_django, sign_up_by_html

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', func_template, name='home'),
#     path('class/', Class_template.as_view())
# ]

urlpatterns = [
    path('',sign_up_by_html),
    #path('', first_pages),
    path('first_page/', first_pages),
    path('shop/', shops),
    path('order/', orders)
]