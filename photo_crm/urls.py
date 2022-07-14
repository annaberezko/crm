"""photo_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from decorator_include import decorator_include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from .settings import LOGIN_URL
from .views import AuthView

urlpatterns = [
    path('mainadmin/', admin.site.urls),
    path('admin/', AuthView.as_view(redirect_authenticated_user=True)),
    # path('admin/', decorator_include(login_required, ('my_secret_app.urls', 'my_secret_app'))),
    path('admin/', decorator_include(login_required(login_url=LOGIN_URL), include('admin_app.urls')))
]

