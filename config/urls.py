"""OpenCollectivités URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls import url
from config.api import api

# Personalize the Django admin header
admin.site.site_header = "Administration d’Open Collectivités"

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^favicon\.ico$", RedirectView.as_view(url="/static/favicon.ico")),
    path("api/", api.urls),
    path("", include("core.urls")),
]

handler404 = "core.views.error404"
handler500 = "core.views.error500"
