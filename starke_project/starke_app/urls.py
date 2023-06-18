from django.contrib import admin
from django.urls import path
from .views import * 




urlpatterns=[
    path('', agregar_cliente, name = 'agregar_cliente'),
    path('index',index, name = 'index'),
    path('tables/',tables, name = 'tables'),
    path('table_pagos/',table_pagos, name = 'table_pagos'),
    path('table_salud/',table_salud, name = 'table_salud'),
    path('table_contacto/',table_contacto, name = 'table_contacto'),
    path('modificar_plan/<id>',modificar_plan, name = 'modificar_plan'),
    path('modificar_datos/<id>',modificar_datos, name = 'modificar_datos'),
    path('modificar_contacto/<id>',modificar_contacto, name = 'modificar_contacto'),
    path('modificar_salud/<id>',modificar_salud, name = 'modificar_salud'),
  
]