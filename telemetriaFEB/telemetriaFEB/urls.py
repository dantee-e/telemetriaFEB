"""telemetriaFEB URL Configuration

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
from django.contrib import admin
from django.urls import path
from data.views import receber_dados, graficos_basicos, graficos_MPU, graficos_analogicos, graficos_GPS, graficos_MLX, index, velocimetro_RPM
from django.conf import settings
from django.conf.urls.static import static


 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dados/', receber_dados),
    path('', index),
    path('graficos-basicos/', graficos_basicos),
    path('graficos-basicos/<int:data>/', graficos_basicos),
    path('graficos-mpu/', graficos_MPU),
    path('graficos-mpu/<int:data>/', graficos_MPU),
    path('graficos-analogicos/', graficos_analogicos),
    path('graficos-analogicos/<int:data>/', graficos_analogicos),
    path('graficos-gps/', graficos_GPS),
    path('graficos-gps/<int:data>/', graficos_GPS),
    path('graficos-mlx/', graficos_MLX),
    path('graficos-mlx/<int:data>/', graficos_MLX),
    path('velocidade-RPM/', velocimetro_RPM),
    path('velocidade-RPM/<int:data>/', velocimetro_RPM) 
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

