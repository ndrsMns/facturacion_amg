from django.urls import path
from .views import (empresa_nueva_form_view, 
                    contacto_nuevo_form_view, 
                    lista_contactos, 
                    eliminar_contacto, 
                    editar_contacto,
                    EmpresaListView,
                    editar_empresa,
                    eliminar_empresa,
                    )

app_name = 'contactos'

urlpatterns = [
    path('formulario_empresa/',empresa_nueva_form_view, name='nueva_empresa'),
    path('formulario_contacto/',contacto_nuevo_form_view, name='nuevo_contacto'),
    path('lista_contactos/', lista_contactos, name='lista_contactos'),
    path('eliminar_contacto/<int:contacto_id>/', eliminar_contacto, name='eliminar_contacto'),
    path('editar_contacto/<int:contacto_id>/',editar_contacto, name='editar_contacto'),
    path('lista_empresas/', EmpresaListView.as_view(), name='lista_empresas'),
    path('editar_empresa/<int:empresa_id>/',editar_empresa, name='editar_empresa'),
    path('eliminar_empresa/<int:empresa_id>/', eliminar_empresa, name='eliminar_empresa'),
]
