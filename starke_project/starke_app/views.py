from django.shortcuts import render, redirect

from django.contrib import messages
import sqlite3 
from .models import *
from .forms import *

import datetime
from datetime import date


#

def index (request):
    conn = sqlite3.connect('db.sqlite3.bd')
    
  
    
    form= client_register_model.objects.all()
    total_nombres = client_register_model.objects.filter(nombre='David')
    return render(request,'starke_app/dashboard/index.html',{'form':form,'total_nombres':total_nombres})



def tables(request):
 
    form= client_register_model.objects.all()
    return render(request,'starke_app/tables/tables.html',{'form':form})

def table_pagos(request):

    hoy= datetime.datetime.now()
    dia= datetime.datetime.strftime(hoy,'%Y-%b-%d')

    form= client_register_model.objects.all()
    

 
 
    return render(request,'starke_app/tables/table_pagos.html',{'form':form,
                                                                'dia':dia})
   

def table_salud(request):
    form= client_register_model.objects.all()
    return render(request,'starke_app/tables/table_salud.html',{'form':form})

def table_contacto(request):
    form= client_register_model.objects.all()
    return render(request,'starke_app/tables/table_contacto.html',{'form':form})

def table_plan(request):
    form= client_register_model.objects.all()
    return render(request,'starke_app/tables/table_plan.html',{'form':form})

def agregar_cliente(request):
    if request.method=='POST':
        formulario = client_register_form(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            nombre=info.get('nombre')
            apellido=info.get('apellido')
            edad=info.get('edad')
            fecha_nacimiento=info.get('fecha_nacimiento')
            email=info.get('email')
            telefono=info.get('telefono')
            telefono_emergencia=info.get('telefono_emergencia')
            nombre_emergencia=info.get('nombre_emergencia')
            
        
            problemas_cardiacos=info.get('problemas_cardiacos')
            problemas_asma=info.get('problemas_asma')
            lesion_pregunta=info.get('lesion_pregunta')
            especificar_lesion=info.get('especificar_lesion')
            telefono_emergencia=info.get('telefono_emergencia')
            
            disciplina=info.get('disciplina')
            dias=info.get('dias')
            plan=info.get('plan')
            pago=info.get('pago')
            
            fecha_vencimiento=info.get('fecha_vencimiento')
            fecha_pago=info.get('fecha_pago')
            fecha_inicio=info.get('fecha_inicio')
            
            
            #diferencia = 'dia de pago - dias a vencer' hacer la resta de los dias aca.
  
            
            cliente_1 = client_register_model(nombre = nombre,
                                              apellido= apellido,
                                              edad= edad,     
                                              fecha_nacimiento = fecha_nacimiento,
                                              email = email,
                                              telefono = telefono,
                                              telefono_emergencia = telefono_emergencia,
                                              nombre_emergencia = nombre_emergencia,
                                              problemas_cardiacos= problemas_cardiacos,
                                              problemas_asma= problemas_asma,
                                            
                                              lesion_pregunta = lesion_pregunta,
                                              especificar_lesion = especificar_lesion,
                                              disciplina = disciplina,
                                              dias = dias,
                                              plan=plan,
                                              pago=pago, 
                                              fecha_pago = fecha_pago,
                                              fecha_inicio = fecha_inicio,
                                              fecha_vencimiento=fecha_vencimiento
                                              )
            
            cliente_1.save()
            return redirect('tables')
    else:    
        messages.success (request,'¡Nuevo producto creado!')    
        form = client_register_form()
        return render(request,'starke_app/clientes/register_informacion.html',{'form': form})






    
    
    

def modificar_pago(request,id):
    cliente = client_register_model.objects.get(id=id)
    if request.method=='POST':
        
        form = client_register_form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            cliente.pago = info['pago']
            cliente.fecha_pago = info['fecha_pago']
            cliente.fecha_vencimiento =info['fecha_vencimiento']
            
            cliente.save()
            return redirect('table_pagos')

        
    else:    
        form = client_register_form(initial={
        'pago':cliente.pago,
        'fecha_pago':cliente.fecha_pago,
         'fecha_vencimiento':cliente.fecha_vencimiento,
        })
        return render(request,'starke_app/modificar/modificar_pago.html',{'form':form,'id':id}) 
    

def modificar_plan(request,id):
    cliente = client_register_model.objects.get(id=id)
    if request.method=='POST':
        
        form = client_register_form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            cliente.plan = info['plan']
            cliente.dias = info['dias']
            cliente.profesor = info['profesor']
            
            
            
            cliente.save()
            return redirect('table_plan')

        
    else:    
        form = client_register_form(initial={
        'plan':cliente.plan,
        'dias':cliente.dias,
        'profesor':cliente.profesor
        })
        return render(request,'starke_app/modificar/modificar_plan.html',{'form':form,'id':id,
                                                                          'nombre':cliente.nombre,
                                                                          'apellido':cliente.apellido}) 
    


def modificar_datos(request,id):
    cliente = client_register_model.objects.get(id=id)
    if request.method=='POST':
        
        form = client_register_form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            cliente.nombre = info['nombre']
            cliente.apellido = info['apellido']
            cliente.edad = info['edad']
            cliente.fecha_nacimiento = info['fecha_nacimiento']
            cliente.fecha_inicio = info['fecha_inicio']
            
            cliente.save()
            return redirect('tables')

        
    else:    
        form = client_register_form(initial={
        'nombre':cliente.nombre ,
        'apellido':cliente.apellido,
        'edad':cliente.edad ,
        'fecha_nacimiento':cliente.fecha_nacimiento 
        })
        return render(request,'starke_app/modificar/modificar_datos.html',{'form':form,'id':id,
                                                                           'nombre':cliente.nombre,
                                                                           'apellido':cliente.apellido,
                                                                           'fecha_inicio':cliente.fecha_inicio}) 
        
def modificar_contacto(request,id):
    cliente = client_register_model.objects.get(id=id)
    if request.method=='POST':
        
        form = client_register_form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            cliente.email = info['email']
            cliente.telefono = info['telefono']
            cliente.telefono_emergencia= info['telefono_emergencia']
            cliente.nombre_emergencia = info['nombre_emergencia']
            
            cliente.save()
            return redirect('table_contacto')

        
    else:    
        form = client_register_form(initial={
        'email':cliente.email,
        'telefono':cliente.telefono,
        'telefono_emergencia':cliente.telefono_emergencia,
        'nombre_emergencia':cliente.nombre_emergencia 
        })
        return render(request,'starke_app/modificar/modificar_contacto.html',{'form':form,'id':id,
                                                                           'nombre':cliente.nombre,
                                                                           'apellido':cliente.apellido})    
                 
                 
def modificar_salud(request,id):
    cliente = client_register_model.objects.get(id=id)
    if request.method=='POST':
        
        form = client_register_form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            cliente.problemas_cardiacos = info['problemas_cardiacos']
            cliente.problemas_asma = info['problemas_asma']
            cliente.lesion_pregunta= info['lesion_pregunta']
            cliente.especificar_lesion = info['especificar_lesion']
            
            cliente.save()
            return redirect('table_salud')

        
    else:    
        form = client_register_form(initial={
        'problemas_cardiacos':cliente.problemas_cardiacos,
        'problemas_asma':cliente.problemas_asma,
        'lesion_pregunta':cliente.lesion_pregunta,
        'especificar_lesion':cliente.especificar_lesion
        })
        return render(request,'starke_app/modificar/modificar_salud.html',{'form':form,'id':id,
                                                                           'nombre':cliente.nombre,
                                                                           'apellido':cliente.apellido})
        
        
        

        
        '''
profesore
profesores
profesores
'''        


def profesores_tabla(request):
        form= profesores_model.objects.all()
        return render(request,'starke_app/profesores/profesores_tabla.html',{'form':form,'id':id})
        
        
def agregar_profesor(request):
    if request.method =='POST':
        formulario = profesores_form(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            profesor= info.get('profesor')
            disciplinas= info.get('disciplinas')
            
            profesor_1 = profesores_model(profesor = profesor,
                                          disciplinas=disciplinas)
            profesor_1.save()
            return redirect('profesores_tabla')
    else:         
        form = profesores_form()
        return render (request, 'starke_app/profesores/agregar_profesor.html',{'form':form}) 
    

def modificar_profesor(request,id):
    profesor = profesores_model.objects.get(id=id)
    if request.method=='POST':
        form = profesores_form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            profesor.profesor = info['profesor']
            profesor.disciplinas=info['disciplinas']
            
            profesor.save()
            return redirect('profesores_tabla')
    else:
        form= profesores_form(initial={
                            'profesor':profesor.profesor,
                            'disciplinas':profesor.disciplinas
                        })
        return render (request, 'starke_app/profesores/modificar_profesor.html',{'form':form,'id':id})
              
              
              
              
              
              
              
def eliminar_profesor(request,id):
    elementos = profesores_model.objects.filter(id=id)
    if len(elementos)!=0:
        elemento=elementos[0]
        elemento.delete()
        messages.success(request,'¡Eliminado correctamente!')
    return redirect ('profesores_tabla')




def tabla_disciplina(request):
 
    form= disciplinas_model.objects.all()
    return render(request,'starke_app/disciplinas/tabla_disciplina.html',{'form':form})



              
def eliminar_cliente(request,id):
    elementos = client_register_model.objects.filter(id=id)
    if len(elementos)!=0:
        elemento=elementos[0]
        elemento.delete()
        messages.success(request,'¡Eliminado correctamente!')
    return redirect ('tables')


def modificar_disciplina(request,id):
    cliente = client_register_model.objects.get(id=id)
    if request.method=='POST':
        
        form = client_register_form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            cliente.disciplina = info['disciplina']
         
            
            cliente.save()
            return redirect('tabla_disciplina')

        
    else:    
        form = client_register_form(initial={
        'disciplina':cliente.disciplina,
     
        })
        return render(request,'starke_app/disciplinas/modificar_disciplina.html',{'form':form,'id':id}) 
