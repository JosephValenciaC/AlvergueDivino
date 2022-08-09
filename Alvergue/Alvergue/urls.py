"""Alvergue URL Configuration

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
from inicio import views
from django.conf import settings
from registros import views as registros_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='Principal'),
    path('contacto/', views.contacto, name='Contacto'),
    path('about/', views.about, name='About'),
    path('registros/', registros_views.medicamentos, name='Registros'),
    path('subir',registros_views.archivos,name="Subir"),
    path('consultasSQL',registros_views.consultasSQL,name="sql"),
    path('consultarMedicamento/<int:id>',registros_views.consultarMedicamento,name="consultarMedicamento"),
    path('editarSalida/<int:id>',registros_views.editarSalida,name="editarSalida"),
    path('eliminar/<int:id>',registros_views.eliminar,name="eliminar"),
    path('stock',registros_views.stock,name="stock"),
    path('salida',registros_views.SalidaSQL,name="salida"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)