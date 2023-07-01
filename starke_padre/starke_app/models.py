from django.db import models

import datetime
from datetime import date



      
class disciplinas_model(models.Model):
    disciplina = models.CharField(max_length= 100, null=True,blank=True)

    def __str__(self)-> str:
          return self.disciplina
     


class profesores_model(models.Model):
    profesor = models.CharField(max_length= 100, null=True,blank=True)
    disciplinas = models.ForeignKey(disciplinas_model,
                                   on_delete = models.CASCADE,
                                   null=True,blank=True)

    def __str__(self)-> str:
          return self.profesor
    
 
      




class client_register_model(models.Model):
  
    

    nombre=models.CharField(max_length=100,blank= True, null=True)
    apellido=models.CharField(max_length=100,blank= True, null=True)
    edad= models.IntegerField(blank= True, null=True)
    fecha_nacimiento= models.DateField(blank= True, null=True)
    email=models.EmailField(max_length=100,blank= True, null=True)
    telefono=models.IntegerField(blank= True, null=True)
    telefono_emergencia=models.IntegerField(blank= True, null=True)
    nombre_emergencia=models.CharField(max_length=100,blank= True, null=True)

    SI = 'Si'
    NO = 'No'
   
    OPCIONES_SN = [(SI,'Si'),
                   (NO,'No')]
    problemas_cardiacos = models.CharField(max_length= 5,
                                  blank = True,
                                  choices= OPCIONES_SN,
                                  default=NO)
   
    problemas_asma = models.CharField(max_length= 5,
                                  blank = True,
                                  choices= OPCIONES_SN,
                                  default=NO)
   
    lesion_pregunta = models.CharField(max_length= 5,
                                  blank = True,
                                  choices= OPCIONES_SN,
                                  default=NO)
    especificar_lesion = models.TextField(max_length= 500, blank= True, null=True)
    
   
    
    UNO = 1
    DOS=2
    TRES=3
    CUATRO=4
    CINCO=5
    SEIS=6
    SIETE=7
    
    OPCIONES_DIAS = [(UNO,1),(DOS,2),(TRES,3),(CUATRO,4),(CINCO,5),(SEIS,6),(SIETE,7)]
    
   
   
    disciplina = models.ForeignKey(disciplinas_model,
                                   on_delete = models.CASCADE,
                                   null=True,blank=True)
   
    dias = models.IntegerField(blank=True,null= True,
                               choices = OPCIONES_DIAS,
                               default = UNO)
    
    
    DIARIO = 'Diario'
    MENSUAL = 'Mensual'
    SEMANAL = 'Semanal'
    DIARIO = 'Diario'
     
    OPCIONES_PLAN = [(DIARIO,'Diario'),
                 (MENSUAL,'Mensual'),
                  (SEMANAL,'Semanal'),
                  (DIARIO,'Diario')
                 ]
    
    plan = models.CharField(max_length= 20,
                                  blank = True,
                                  null=True,
                                  choices= OPCIONES_PLAN,
                                  default=MENSUAL)
    profesor = models.ForeignKey(profesores_model,
                                   on_delete = models.CASCADE,
                                   null=True,blank=True)
    fecha_inicio = models.DateField(blank = True,null=True)
    fecha_pago = models.DateField(blank= True, null=True)
    pago = models.IntegerField(blank = True,null=True)
    fecha_vencimiento = models.DateField(blank= True, null=True)
    #cambiar pago por monto
    
    def __str__(self)-> str:
          return self.nombre 
 
    


