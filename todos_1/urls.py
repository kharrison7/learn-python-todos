"""todos URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

#imports greeting_view
# from core.views import greeting_view
from core import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #calls the greeting_view
    # url(r'^$', greeting_view),
    url(r'^hello/$',views. greeting_view),
    url(r'^goodbye/$',views. goodbye_view),
    url(r'^bmi/$',views. bmi),
]

# regular expression
# ^ begin of string
# $ end of string
