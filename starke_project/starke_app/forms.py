from django import forms
from .models import *
from django.forms import ModelForm
from django.conf import settings
'''
class client_register_form(forms.ModelForm):
    
    class Meta:
        model = client_register_model
        fields= '__all__'
        widgets = {'nombre':forms.TextInput(
            attrs={'class':'form-control',
                   'type':'text',
                   'placeholder':'Nombre',
                   'id':"inputFirstName",
                   'label':'Nombre'}
        ),
         'apellido':forms.TextInput(
             attrs={'class':'form-control',
                   'type':'text',
                   'placeholder':'Apellido',
                   'id':"inputFirstName",
                   'label':'Apellido'}
         ),
          'edad':forms.NumberInput(
             attrs={'class':'form-control',
                   'type':'number',
                   'placeholder':'Edad',
                   'id':"inputPassword",
                   'label':'Edad'}
        ),
          'fecha_nacimiento':forms.DateInput(
             attrs={'class':'form-control',
                   'type':'date',
                   'placeholder':'Fecha de nacimiento',
                   'id':"DateEmail",
                   'label':'Fecha de nacimiento'}
        ),
          'email':forms.EmailInput(
             attrs={'class':'form-control',
                   'type':'email',
                   'placeholder':'Email',
                   'id':"inputEmail",
                   'label':'Email'}
        ),
           'telefono':forms.NumberInput(
             attrs={'class':'form-control',
                   'type':'number',
                   'placeholder':'Telefono',
                   'id':"inputPassword",
                   'label':'Telefono'},
             ),
           'telefono_emergencia':forms.NumberInput(
             attrs={'class':'form-control',
                   'type':'number',
                   'placeholder':'Telefono de emergencia',
                   'id':"inputPassword",
                   'label':'Telefono de emergencia'},
             ),
           'nombre_emergencia':forms.TextInput(
             attrs={'class':'form-control',
                   'type':'text',
                   'placeholder':'Nombre de tel emergencia',
                   'id':"inputPassword",
                   'label':'Nombre de tel emergencia'},
             ),
              'red_social':forms.NumberInput(
             attrs={'class':'form-control',
                   'type':'url',
                   'placeholder':'Red social',
                   'id':"inputPasswordConfirm",
                   'label':'Red social'},
             ),
           }
        
   '''     
        
class client_register_form(forms.ModelForm):
     
   
      '''fecha_nacimiento= forms.DateField(widget=forms.DateInput(attrs={
                                                                       'class':'form-control',
                                                                        'type':'date',
                                                                        'placeholder':'Fecha de nacimiento',
                                                                        'id':"DateEmail",
                                                                        'label':'Fecha de nacimiento'
                                                                       },format = '%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)'''
      class Meta:
        model = client_register_model
        fields= '__all__'
        widgets = {
            'especificar_lesion':forms.Textarea(
            attrs={'class':'form-control',
            'type':'textarea',
            'placeholder':'Lesion especificar',
            'id':"especificarFracturaOLesion",
            'atribute':'label',
            'label':'textarea',
            'style':"height: 10rem"}
      ),
            'nombre':forms.TextInput(
           attrs={'class':'form-control',
                   'type':'text',
                   'placeholder':'Nombre',
                   'id':"inputFirstName",
                   'label':'Nombre'}
      ),
         'apellido':forms.TextInput(
             attrs={'class':'form-control',
                   'type':'text',
                   'placeholder':'Apellido',
                   'id':"inputFirstName",
                   'label':'Apellido'}
         ),
          'edad':forms.NumberInput(
             attrs={'class':'form-control',
                   'type':'number',
                   'placeholder':'Edad',
                   'id':"inputPassword",
                   'label':'Edad'}
        ),
         
          'email':forms.EmailInput(
             attrs={'class':'form-control',
                   'type':'email',
                   'placeholder':'Email',
                   'id':"inputEmail",
                   'label':'Email'}
        ),
           'telefono':forms.NumberInput(
             attrs={'class':'form-control',
                   'type':'number',
                   'placeholder':'Telefono',
                   'id':"inputPassword",
                   'label':'Telefono'},
             ),
           'telefono_emergencia':forms.NumberInput(
             attrs={'class':'form-control',
                   'type':'number',
                   'placeholder':'Telefono de emergencia',
                   'id':"inputPassword",
                   'label':'Telefono de emergencia'},
             ),
           'nombre_emergencia':forms.TextInput(
             attrs={'class':'form-control',
                   'type':'text',
                   'placeholder':'Nombre de tel emergencia',
                   'id':"inputPassword",
                   'label':'Nombre de tel emergencia'},
             ),
              'red_social':forms.NumberInput(
             attrs={'class':'form-control',
                   'type':'url',
                   'placeholder':'Red social',
                   'id':"inputPasswordConfirm",
                   'label':'Red social'},
             ),
              'pago':forms.NumberInput(
                  attrs = {'class': 'form-control',
                           'id':'agregarElPagoDelPlan',
                           'type':'number',
                           }
            ),
            
          'fecha_nacimiento':forms.DateInput(
             attrs={'class':'form-control',
                   'type':'date',
                   'placeholder':'Fecha de nacimiento',
                   'id':"DateEmail",
                   'label':'Fecha de nacimiento'}
        ),
           'fecha_inicio':forms.DateInput(
             attrs={'class':'form-control',
                   'type':'date',
                   'placeholder':'Fecha de inicio',
                   'id':"DateEmail",
                   'label':'Fecha de inicio'}
        ),
              
          'fecha_vencimiento':forms.DateInput(
             attrs={'class':'form-control',
                   'type':'date',
                   'placeholder':'Fecha de vencimiento',
                   'id':"DateEmail",
                   'label':'Fecha de vencimiento'}
        ),
                 
          'fecha_pago':forms.DateInput(
             attrs={'class':'form-control',
                   'type':'date',
                   'placeholder':'Fecha de inicio',
                   'id':"DateEmail",
                   'label':'Fecha de inicio'}
        ),
            
        }
        
        
class profesores_form(forms.ModelForm):
      class Meta:
            model = profesores_model
            fields = '__all__'
            widgets = {'profesor':forms.TextInput(
                        attrs={'class':'form-control',
                        'type':'text',
                        'placeholder':'Nombre de profesor',
                        'id':"inputFirstName",
                        'label':'Nombre de profesor'}
                        ),
                       'disciplina':forms.TextInput(
                        attrs={'class':'form-control',
                        'type':'text',
                        'placeholder':'Nombre de profesor',
                        'id':"inputFirstName",
                        'label':'Nombre de profesor'}
                        ),
                       }