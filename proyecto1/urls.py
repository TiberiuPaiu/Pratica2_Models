"""proyecto1 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin # para el admin
from django.urls import path
from tienda import views
from django.contrib.auth.views import LoginView, logout_then_login

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.pagina_pricipal),
    path('panel/admistrado/', admin.site.urls),
    
    path('producto_add/', views.add_product),
    path('post_product_add/', views.add_post_product),

    path('hombre/', views.pagina_pricipal_h),
    path('mujer/', views.pagina_pricipal_f),
   
    
    path('busacr/<str:id1>/<str:id2>/<int:id3>/', views.pagina_pricipal_busar), 
    path('busacr_nombre/<str:id1>/', views.pagina_pricipal_busar_input), 

    path('accounts/login/',LoginView.as_view(template_name='pagina_login.html')),
    path('validar_usuario/',views.validar_usuario),
    path('des_logarse/',logout_then_login),

    path('registrate/',views.registrar_cliente ),
    path('from_cliente_post/',views.from_cliente ),


    path('comprar/<str:id>/',views.add_compra ),
    path('visualizar/comprar/',views.view_compra ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
