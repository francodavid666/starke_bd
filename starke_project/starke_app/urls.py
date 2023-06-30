from django.contrib import admin
from django.urls import path,include
from .views import * 
from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings
from django.views.static import serve





urlpatterns=[
    path('', agregar_cliente, name = 'agregar_cliente'),
    path('index',index, name = 'index'),
    path('tables/',tables, name = 'tables'),
    path('table_pagos/',table_pagos, name = 'table_pagos'),
    path('table_plan/',table_plan, name = 'table_plan'),
    path('table_salud/',table_salud, name = 'table_salud'),
    path('table_contacto/',table_contacto, name = 'table_contacto'),
    path('modificar_pago/<id>',modificar_pago, name = 'modificar_pago'),
    path('modificar_datos/<id>',modificar_datos, name = 'modificar_datos'),
    path('modificar_contacto/<id>',modificar_contacto, name = 'modificar_contacto'),
    path('modificar_salud/<id>',modificar_salud, name = 'modificar_salud'),
    path('modificar_plan/<id>',modificar_plan, name = 'modificar_plan'),
    path('profesores_tabla/',profesores_tabla, name = 'profesores_tabla'),
    path('agregar_profesor/',agregar_profesor, name = 'agregar_profesor'),
    path('modificar_profesor/<id>',modificar_profesor, name = 'modificar_profesor'),
    path('eliminar_profesor/<id>',eliminar_profesor, name = 'eliminar_profesor'),
    path('eliminar_cliente/<id>',eliminar_cliente, name = 'eliminar_cliente'),
    path('tabla_disciplina/',tabla_disciplina, name = 'tabla_disciplina'),
    path('modificar_disciplina/<id>',modificar_disciplina, name = 'modificar_disciplina'),
  
]