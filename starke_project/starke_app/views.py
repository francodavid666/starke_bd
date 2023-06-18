from django.shortcuts import render, redirect
import pandas as pd
from django.contrib import messages
import sqlite3 
from .models import *
from .forms import *

import datetime
from datetime import date




def index (request):
    conn = sqlite3.connect('db.sqlite3.bd')
    
  
    
    form= client_register_model.objects.all()
    total_nombres = client_register_model.objects.filter(nombre='David')
    return render(request,'starke_app/dashboard/index.html',{'form':form,'total_nombres':total_nombres})



def tables(request):
 
    form= client_register_model.objects.all()
    return render(request,'starke_app/tables/tables.html',{'form':form})

def table_pagos(request):
    
    
    form= client_register_model.objects.all()
    form2= disciplinas_model.objects.all()
    return render(request,'starke_app/tables/table_pagos.html',{'form':form,
                                                                'form2':form2
                                                                })


def table_salud(request):
    form= client_register_model.objects.all()
    return render(request,'starke_app/tables/table_salud.html',{'form':form})

def table_contacto(request):
    form= client_register_model.objects.all()
    return render(request,'starke_app/tables/table_contacto.html',{'form':form})

def agregar_cliente(request):
    if request.method=='POST':
        formulario = client_register_form(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            nombre=info.get('nombre')
            apellido=info.get('apellido')
            edad=info.get('edad')
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
  
            
            cliente_1 = client_register_model(nombre = nombre,
                                              apellido= apellido,
                                              edad= edad,     
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
                                              pago=pago 
                                              )
            
            cliente_1.save()
            return redirect('index')
    else:    
        messages.success (request,'¡Nuevo producto creado!')    
        form = client_register_form()
        return render(request,'starke_app/clientes/register_informacion.html',{'form': form})




def agregar_cliente_salud(request):
    if request.method=='POST':
        formulario = client_salud_form(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            cardiacos_no=info.get('cardiacos_no')
            cardiacos_si=info.get('cardiacos_si')
            asma_no=info.get('asma_no')
            asma_si=info.get('asma_si')
            lesion_no=info.get('lesion_no')
            lesion_si=info.get('lesion_si')
            especificar_lesion=info.get('especificar_lesion')
            telefono_emergencia=info.get('telefono_emergencia')

        
  
            
            cliente_1 = client_salud_model(cardiacos_no = cardiacos_no,
                                              cardiacos_si = cardiacos_si,
                                              asma_si = asma_si,
                                              asma_no = asma_no,
                                              lesion_no = lesion_no,
                                              lesion_si = lesion_si,
                                              especificar_lesion = especificar_lesion,
                                                )
            
            cliente_1.save()
            return redirect('agregar_cliente_plan')
    else:      
        form = client_salud_form()
        return render(request,'starke_app/clientes/register_salud.html',{'form':form})



def agregar_cliente_plan (request):
    if request.method=='POST':
        formulario = client_plan_form(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            disciplina=info.get('disciplina')
            dias=info.get('dias')
            plan=info.get('plan')
            pago=info.get('pago')
        

            cliente_1 = cliente_plan_model(disciplina = disciplina,
                                           dias = dias,
                                           plan=plan,
                                           pago=pago                                
                                              )
            cliente_1.save()
            return redirect('agregar_cliente_salud')
        else:
            return redirect('agregar_cliente_plan')
            messages.success (request,'¡Nuevo producto creado!')   
    else:      
        form = client_plan_form()
        return render(request,'starke_app/clientes/register_plan.html',{'form':form})
    
    
    

def modificar_plan(request,id):
    cliente = client_register_model.objects.get(id=id)
    if request.method=='POST':
        
        form = client_register_form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            cliente.pago = info['pago']
            
            cliente.save()
            return redirect('table_pagos')

        
    else:    
        form = client_register_form(initial={
        'pago':555
        })
        return render(request,'starke_app/modificar/modificar_plan.html',{'form':form,'id':id}) 
    

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
                                                                           'apellido':cliente.apellido}) 
        
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