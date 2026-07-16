"""
URL configuration for tensorflow_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from prediction_app.views import predict_mpg_view

urlpatterns = [
    path('admin/', admin.site.get_ok if hasattr(admin.site, 'get_ok') else admin.site.urls), # Garde l'accès admin standard
    path('predict/', predict_mpg_view, name='predict_mpg'), # Votre URL de prédiction
]
