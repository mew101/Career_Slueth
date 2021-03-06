"""career_slueth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import *
from career_slueth.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', Index.as_view(),name='index'),
    path ('dashboard/', Dashboard.as_view()),

    #path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    #path('logout/', Logout.as_view(), name="logout"),
]
