from ast import pattern
from datetime import datetime
from .models import TipoPago
from ast import pattern
from datetime import datetime
from .models import TipoPagoHistorico
import re
from django import forms
from .models import Alumno, DocumentoDPI,Empleado,Catedratico, Factura, Pago,Tutor,Asignatura,Matricula,Reportes,ExpedienteMedico, HorariosNivelEducativo, NivelEducativo, ParcialesAcademicos, NotasAlumnos, Municipio, TipoPago,Seccion, Actitud, CentroEducativo, TutoresAlumnos
from typing import Required, Self
	
from django.core.validators import RegexValidator
from .models import Grado,ParametrosSAR,Meses,TipoReporte,Departamento,TipoPago,CategoriaEmpleado,ExpedienteEscolar,ExpedienteMedico,TipoSanguineo


import re
from django import forms
from .models import Alumno, DocumentoDPI,Empleado,Catedratico,Tutor,Asignatura,Matricula,Reportes,ExpedienteMedico, HorariosNivelEducativo, NivelEducativo, ParcialesAcademicos, NotasAlumnos, Municipio, TipoPago, Seccion, Actitud, CentroEducativo, TutoresAlumnos
from typing import Required, Self
	
from django.core.validators import RegexValidator
from .models import Grado,ParametrosSAR,Meses,TipoReporte,Departamento,TipoPago,CategoriaEmpleado,ExpedienteEscolar,ExpedienteMedico,TipoSanguineo


from django.core.exceptions import ValidationError

def validate_direccion(value):
    # Verificar que la dirección no esté vacía
    if not value.strip():
        raise ValidationError("La dirección no puede estar vacía.")

    # Verificar que la dirección tenga al menos 5 caracteres
    if len(value) < 5:
        raise ValidationError("La dirección debe tener al menos 5 caracteres.")

    # Verificar que la dirección solo contenga letras con tildes y espacios en blanco
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$', value):
        raise ValidationError("La dirección no puede contener Números ")

    # Verificar que la dirección no contenga tres o más letras iguales repetidas seguidas
    for i in range(len(value) - 2):
        if value[i] == value[i+1] == value[i+2]:
            raise ValidationError("La dirección no puede contener tres o más letras iguales repetidas seguidas.")

    # Verificar que la dirección no contenga dobles espacios en blanco seguidos
    if '  ' in value:
        raise ValidationError("La dirección no puede contener dobles espacios en blanco.")

class DPIValidator:

    def __init__(self, queryset):
        self.queryset = queryset

    def __call__(self, value):
        # Obtener la opción seleccionada en el campo "DocumentoDPI"
        documento_dpi_id = self.queryset.get(pk=value.DocumentoDPI_id)
        # Obtener la longitud requerida según la opción seleccionada
        longitud_requerida = documento_dpi_id.longitud

        # Verificar la longitud del DPI
        if len(value) != longitud_requerida:
            raise forms.ValidationError(f'El {documento_dpi_id} debe tener {longitud_requerida} caracteres.')


def password_validator(password):
    # Verificar si la contraseña tiene al menos 8 caracteres
    if len(password) < 8:
        raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
    
    # Verificar si la contraseña contiene al menos un número
    if not any(char.isdigit() for char in password):
        raise ValidationError("La contraseña debe contener al menos un número.")
    
    # Verificar si la contraseña contiene al menos una letra en mayúscula
    if not any(char.isupper() for char in password):
        raise ValidationError("La contraseña debe contener al menos una letra en mayúscula.")
    
    # Verificar si la contraseña contiene al menos una letra en minúscula
    if not any(char.islower() for char in password):
        raise ValidationError("La contraseña debe contener al menos una letra en minúscula.")

def no_numeros_ni_especiales_validator(value):
    if re.search(r'[0-9!@#$%^&*(),.?":{}|<>]', value):
        raise forms.ValidationError('El campo no adminite caracteres especiales.')

def dni_longitud_validator(value):
    if not value.isdigit() or len(value) != 13:
        raise forms.ValidationError('El DNI debe contener solo números y tener exactamente 13 dígitos.')
    return value

def rtn_longitud_validator(value):
    if len(value) != 14:
        raise forms.ValidationError('El RTN debe contener exactamente 14 dígitos numéricos.')

def pasaporte_longitud_validator(value):
    if len(value) != 20:
        raise forms.ValidationError('El pasaporte debe contener exactamente 20 caracteres alfanuméricos.')



def no_campos_vacios_validator(value):
    if not value.strip():
        raise forms.ValidationError('Este campo no puede estar vacío.')


def no_letras_ni_numeros_ni_especiales_validator(value):
    if re.search(r'[a-zA-Z\d!@#$%^&*(),.?":{}|<>]', value):
        raise forms.ValidationError('El campo no debe contener letras, números o caracteres especiales al mismo tiempo.')




def telefono_validator(value):
    if not value.isdigit():
        raise forms.ValidationError('El teléfono debe contener solo dígitos numéricos.')

    if len(value) != 8:
        raise forms.ValidationError('El teléfono debe tener 8 dígitos.')

    if not value.startswith(('9', '8', '3')):
        raise forms.ValidationError('El número de teléfono debe tener 8 dígitos y comenzar con 9, 8 o 3.')

def fecha_rango_validator(value):
    min_fecha = datetime.strptime('2004-01-01', '%Y-%m-%d').date()
    max_fecha = datetime.strptime('2019-01-01', '%Y-%m-%d').date()

    if value < min_fecha or value > max_fecha:
        raise forms.ValidationError(' Ingrese  una edad entre 5  a 18 años.')


def solo_letras_validator(value):
    if not re.match(r'^[a-zA-Z ]*$', value):
        raise forms.ValidationError('El campo solo puede contener letras y un solo espacio.')


def solo_letras_y_un_espacio_validator(value):
    if not re.match(r'^[a-zA-Z]+( [a-zA-Z]+)?$', value):
        raise forms.ValidationError('El campo solo puede contener letras y un solo espacio.')

def no_letras_ni_numeros_ni_especiales_validator(value):
    if re.search(r'[a-zA-Z\d!@#$%^&*(),.?":{}|<>]', value):
        raise forms.ValidationError('El campo no debe contener letras, números o caracteres especiales al mismo tiempo.')
    
def no_campos_vacios_validator(value):
    if not value.strip():
        raise forms.ValidationError('Este campo no puede estar vacío.')
    
def no_dos_espacios_validator(value):
    if '  ' in value:
        raise forms.ValidationError('No se permiten dos espacios en blanco seguidos.')

def no_tres_letras_iguales_validator(value):
    for i in range(len(value) - 2):
        if value[i] == value[i+1] == value[i+2]:
            raise forms.ValidationError('No se permiten tres letras iguales seguidas.')

def no_numeros_validator(value):
    if any(char.isdigit() for char in value):
        raise forms.ValidationError('No se permiten números en este campo.')
    
def no_dos_espacios_validator(value):
    if '  ' in value:
        raise forms.ValidationError('No se permiten dos espacios en blanco seguidos.')

def no_tres_letras_iguales_validator(value):
    for i in range(len(value) - 2):
        if value[i] == value[i+1] == value[i+2]:
            raise forms.ValidationError('No se permiten tres letras iguales seguidas.')
        
def notasacumulativo_longitud_validator(value):
    str_value = str(value)
    
    if '.' in str_value:
        num_entero, num_decimal = str_value.split('.')
        
        if len(num_entero) > 2 or len(num_decimal) > 2:
            raise ValidationError('La nota debe tener hasta 2 dígitos antes del punto y hasta 2 dígitos después del punto.')
    else:
        if len(str_value) > 2:
            raise ValidationError('La nota debe tener hasta 2 dígitos.')
    
def notasexamen_longitud_validator(value):
    
    num_entero, _, num_decimal = value.partition('.')
    
    if len(num_entero) > 2 or len(num_decimal) > 2:
        raise forms.ValidationError('La nota debe tener hasta 2 dígitos antes del punto y hasta 2 dígitos después del punto.')
    
    notaexamen = float(value)
    if notaexamen > 30:
        raise forms.ValidationError('La nota no puede ser mayor a 30.')

def notas_longitud_validator(value):
    if not (4 <= len(str(value).split('.')[0]) <= 5) or len(str(value).split('.')[1]) > 2:
        raise forms.ValidationError('La nota debe tener entre 4 y 5 dígitos antes del punto y hasta 2 dígitos después del punto.')
    
    if value > notas_longitud_validator('70'):
        raise forms.ValidationError('La nota no puede ser mayor a 70.')
    
def notasfinales_longitud_validator(value):
    
    num_entero, _, num_decimal = value.partition('.')
    
    if 4 >= len(num_entero) <= 5 and len(num_decimal) <= 2:
        notafinal = float(value)
        if notafinal <= 100:
            raise forms.ValidationError('La nota no puede ser mayor a 100.')
    else:
        raise forms.ValidationError('La nota debe tener entre 4 y 5 dígitos antes del punto y hasta 2 dígitos después del punto.')

def fechainicio_rango_parciales(value):
    min_fecha = datetime.strptime('2023-01-01', '%Y-%m-%d').date()
    max_fecha = datetime.strptime('2025-01-01', '%Y-%m-%d').date()

    if value < min_fecha or value > max_fecha:
        raise forms.ValidationError(' Ingrese una Fecha de Inicio Parcial.')

def fechafinal_rango_parciales(value):
    min_fecha = datetime.strptime('2023-01-01', '%Y-%m-%d').date()
    max_fecha = datetime.strptime('2025-01-01', '%Y-%m-%d').date()

    if value < min_fecha or value > max_fecha:
        raise forms.ValidationError(' Ingrese una Fecha de Final Parcial.')

def fechaaño_rango_año(value):
    min_fecha = datetime.strptime('2023-01-01', '%Y-%m-%d').date()
    max_fecha = datetime.strptime('2025-01-01', '%Y-%m-%d').date()

    if value < min_fecha or value > max_fecha:
        raise forms.ValidationError(' Ingrese una fecha del Año.')

def fecha_rango_emision(value):
    min_fecha = datetime.strptime('2023-01-01', '%Y-%m-%d').date()
    max_fecha = datetime.strptime('2025-01-01', '%Y-%m-%d').date()

    if value < min_fecha or value > max_fecha:
        raise forms.ValidationError(' Ingrese una Fecha de Emisión.')
    
def fecha_rango_vencimiento(value):
    min_fecha = datetime.strptime('2023-01-01', '%Y-%m-%d').date()
    max_fecha = datetime.strptime('2025-01-01', '%Y-%m-%d').date()

    if value < min_fecha or value > max_fecha:
        raise forms.ValidationError(' Ingrese una Fecha de Vencimiento.')

def correlativo_validator(value):
    if not value.isdigit():
        raise forms.ValidationError('El Correlativo debe contener solo dígitos numéricos.')

    if len(value) != 8:
        raise forms.ValidationError('El Correlativo debe tener 8 dígitos.')
    
def RTN_longitud_validator(value):
    if len(value) != 15:
        raise forms.ValidationError('El RTN debe contener exactamente 15 dígitos numéricos.')




from django import forms
from .models import Alumno, DocumentoDPI

import re
from django import forms
from .models import Alumno, DocumentoDPI

def validate_dpi(value):
    # Verificar que el DPI no esté en blanco
    if not value.strip():
        raise forms.ValidationError("El DPI no puede estar en blanco.")

    # Verificar que el DPI tenga solo números y letras (si el tipo de documento es pasaporte)
    if not re.match(r'^[a-zA-Z0-9]+$' if value.startswith('Pasaporte') else r'^[0-9]+$', value):
        raise forms.ValidationError("El DPI solo puede contener números o letras (si el tipo de documento es Pasaporte).")

    # Verificar que el DPI no contenga dos o más espacios en blanco seguidos
    if '  ' in value:
        raise forms.ValidationError("El DPI no puede contener dos o más espacios en blanco seguidos.")

    # Verificar que el DPI no contenga tres o más letras iguales repetidas seguidas
    for i in range(len(value) - 2):
        if value[i] == value[i+1] == value[i+2]:
            raise forms.ValidationError("El DPI no puede contener tres o más letras iguales repetidas seguidas.")

    # Verificar que el DPI no contenga tildes ni caracteres especiales
    if not re.match(r'^[a-zA-Z0-9ÁÉÍÓÚáéíóúÑñ]+$', value):
        raise forms.ValidationError("El DPI no puede contener tildes ni caracteres especiales.")

import re
from django import forms
from .models import Alumno, DocumentoDPI

import re
from django import forms
from .models import Alumno, DocumentoDPI

from django.core.exceptions import ValidationError
import re

def validate_dpi(value, documento_dpi):
    # Verificar que el DPI no esté en blanco
    if not value.strip():
        raise ValidationError("El Campo  no puede estar en blanco.")

    # Verificar que el DPI tenga solo números si no es pasaporte
    if documento_dpi.DocumentoDPI != 'PASAPORTE' and not value.isdigit():
        raise ValidationError("El DNI O RTN solo puede contener números.")

    # Verificar que el DPI tenga letras y números si es pasaporte
    if documento_dpi.DocumentoDPI == 'PASAPORTE' and not re.match(r'^[a-zA-Z0-9]+$', value):
        raise ValidationError("El DPI puede contener letras y números si el tipo de documento es Pasaporte.")

    # Verificar la longitud del DPI de acuerdo al tipo de documento seleccionado
    if len(value) != documento_dpi.longitud:
        raise ValidationError(f"El Documento debe tener {documento_dpi.longitud} caracteres.")

    # Verificar que el DPI no contenga dos o más espacios en blanco seguidos
    if '  ' in value:
        raise ValidationError("El Documento no puede contener dos o más espacios en blanco seguidos.")

    # Verificar que el DPI no contenga tildes ni caracteres especiales
    if not re.match(r'^[a-zA-Z0-9ÁÉÍÓÚáéíóúÑñ]+$', value):
        raise ValidationError("El Documento no puede contener tildes ni caracteres especiales.")

    # Verificar que el pasaporte no tenga letras repetidas
    if documento_dpi.DocumentoDPI == 'PASAPORTE':
        for i in range(len(value) - 2):
            if value[i] == value[i+1] == value[i+2] and value[i].isalpha():
                raise ValidationError("El pasaporte no puede contener tres o más letras iguales repetidas seguidas.")


class AlumnoForm(forms.ModelForm):
    DPI = forms.CharField(
        max_length=30,
        label='Número de Documento',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese  el Documento',
        })
    )
    DireccionAlumno = forms.CharField(
        max_length=200,
        label='Dirección del Alumno',
        validators=[validate_direccion],
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Agregamos el atributo 'class' al campo
    )
    class Meta:
        model = Alumno
        fields = ['NombresAlumno', 'ApellidosAlumno', 'DocumentoDPI', 'DPI', 'FechaNacimientoAlumno', 'DireccionAlumno', 'Departamento', 'Municipio', 'Grado','Seccion', 'TipoSanguineo']
        labels = {
            'NombresAlumno': 'Nombres del Alumno:',
            'ApellidosAlumno': 'Apellidos del Alumno:',
            'DocumentoDPI': 'Tipo de Documento:',
            'DPI': 'Documento',
            'FechaNacimientoAlumno': 'Fecha de Nacimiento del Alumno:',
            'DireccionAlumno': 'Dirección del Alumno:',
            'Departamento': 'Departamento nativo:',
            'Municipio': 'Municipio nativo:',
            'Grado': 'Grado al que aspira:',
            'Seccion': 'Secciones:',
            'TipoSanguineo': 'Tipo de Sangre del Alumno:',
        }
        widgets = {
            'NombresAlumno': forms.TextInput(
                attrs={'class': 'form-control'}),
            'ApellidosAlumno': forms.TextInput(
                attrs={'class': 'form-control'}),
            'DocumentoDPI': forms.Select(
                attrs={'class': 'form-control'}),
            'FechaNacimientoAlumno': forms.DateInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'DD/MM/YYYY', 
                    'type': 'date',
                }
            ),
            'DireccionAlumno': forms.TextInput(
            attrs={
                'class': 'form-control',
                'required': 'required',
                'id': 'DireccionAlumno',}),


            'Departamento': forms.Select(
                attrs={'class': 'form-control'}),
            'Grado': forms.Select(
                attrs={'class': 'form-control'}),
            'Seccion': forms.Select(
                attrs={'class': 'form-control'}),
            'TipoSanguineo': forms.Select(
                attrs={'class': 'form-control'}),
    }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtener el queryset para las opciones del campo "DocumentoDPI"
        queryset = DocumentoDPI.objects.all()
        # Agregar las opciones de DocumentoDPI al campo "DocumentoDPI" del formulario
        self.fields['DocumentoDPI'].queryset = queryset

    def clean_DPI(self):
        dpi = self.cleaned_data.get('DPI')
        documento_dpi = self.cleaned_data.get('DocumentoDPI')

        # Verificar que el campo "DocumentoDPI" tenga una opción seleccionada
        if not documento_dpi:
            raise forms.ValidationError("Debe seleccionar un tipo de documento.")

        # Validar el DPI de acuerdo al tipo de documento seleccionado
        validate_dpi(dpi, documento_dpi)

        return dpi

    def __init__(self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)
        if 'Departamento' in self.data:
            try:
                departamento_id = int(self.data.get('departamento'))
                self.fields['Municipio'].queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('departamento')
            except (ValueError, TypeError):
                pass

    def clean_FechaNacimientoAlumno(self):
        fecha_nacimiento = self.cleaned_data.get('FechaNacimientoAlumno')
        fecha_rango_validator(fecha_nacimiento)
        return fecha_nacimiento
    

    
    def clean_NombresAlumno(self):
        nombres_alumno = self.cleaned_data.get('NombresAlumno')

        if any(char.isdigit() for char in nombres_alumno):
            raise forms.ValidationError('El nombre no debe contener números.')

        if len(nombres_alumno) < 3 or len(nombres_alumno) > 20:
            raise forms.ValidationError('La longitud del nombre debe ser entre 3 y 20 caracteres.')

        if re.search(r'(\w)\1', nombres_alumno):
            raise forms.ValidationError('El nombre no puede contener mas  letras repetidas, Asegurate de Poner Los Nombres Validos.')

        if '  ' in nombres_alumno:
            raise forms.ValidationError('El nombre no puede contener espacios dobles.')

        return nombres_alumno.capitalize()

    def clean_ApellidosAlumno(self):
        apellidos_alumno = self.cleaned_data.get('ApellidosAlumno')

        if any(char.isdigit() for char in apellidos_alumno):
            raise forms.ValidationError('Los apellidos no deben contener números.')

        if len(apellidos_alumno) < 2 or len(apellidos_alumno) > 30:
            raise forms.ValidationError('La longitud de los apellidos debe ser entre 2 y 30 caracteres.')

        if re.search(r'(\w)\1', apellidos_alumno):
            raise forms.ValidationError('Los apellidos no puede contener mas  letras repetidas, Asegurate de Poner Los Apellidos Validos..')

        if '  ' in apellidos_alumno:
            raise forms.ValidationError('Los apellidos no pueden contener espacios dobles.')

        return apellidos_alumno.capitalize()
    
   
    
#Validaciones especificas

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['NombresEmpleado', 'ApellidosEmpleado', 'DocumentoDPI', 'DPI', 'FechaNacimientoEmpleado', 'CategoriaEmpleado', 'Tel_Empleado']
        labels = {
            'NombresEmpleado': 'Nombres del Empleado',
            'ApellidosEmpleado': 'Apellidos del Empleado',
            'DocumentoDPI': 'Tipo de Documento',
            'DPI': 'Documento',
            'FechaNacimientoEmpleado': 'Fecha de Nacimiento del Empleado',
            'CategoriaEmpleado': 'Categoría del Empleado',
            'Tel_Empleado': 'Teléfono del Empleado',
        }
        widgets = {
            'NombresEmpleado': forms.TextInput(
                attrs={'class': 'form-control',
                       'Required':'Required',
                       'id':'NombresEmpleado',
                       'Type':'text',
                       'min_length':'3',
                       'max_length':'10' ,
                       'pattern':'[a-zA-Z].{2,20}' }),
            'ApellidosEmpleado': forms.TextInput(
                attrs={'class': 'form-control',
                       'Required':'Required',
                       'id':'ApellidosEmpleado',
                       'Type':'text',
                       'min_length':'1',
                       'max_length':'40' ,
                       'pattern':'[a-zA-Z].{3,30}', }),
           'DocumentoDPI': forms.Select(
                attrs={'class': 'form-control'}),
            'DPI': forms.TextInput(
                attrs={'class': 'form-control'}),
            'FechaNacimientoEmpleado': forms.DateInput(
                attrs={'class': 'form-control', 
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date',
                       }),
            'CategoriaEmpleado': forms.Select(
                attrs={'class': 'form-control'}),
            'Tel_Empleado': forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': '########',
               'title': 'El número de teléfono debe tener 8 dígitos y comenzar con 9, 8 o 3.'}),
        }

    


    def clean_Tel_Empleado(self):
        telefono_empleado = self.cleaned_data['Tel_Empleado']
        telefono_validator(telefono_empleado)
        return telefono_empleado



    def clean_FechaNacimientoEmpleado(self):
        fecha_nacimiento = self.cleaned_data.get('FechaNacimientoEmpleado')
        fecha_rango_validator(fecha_nacimiento)
        return fecha_nacimiento
    

    
    def clean_NombresEmpleado(self):
        nombres_empleado = self.cleaned_data.get('NombresEmpleado')
        solo_letras_validator(nombres_empleado)
        no_campos_vacios_validator(nombres_empleado)
        no_dos_espacios_validator(nombres_empleado)
        no_numeros_validator(nombres_empleado)
        no_tres_letras_iguales_validator(nombres_empleado)
        return nombres_empleado.capitalize()
    
    def clean_ApellidosEmpleado(self):
        nombres_empleado = self.cleaned_data.get('ApellidosEmpleado')
        solo_letras_validator(nombres_empleado)
        no_campos_vacios_validator(nombres_empleado)
        no_dos_espacios_validator(nombres_empleado)
        no_numeros_validator(nombres_empleado)
        no_tres_letras_iguales_validator(nombres_empleado)
        return nombres_empleado.capitalize()
    

   


class CatedraticoForm(forms.ModelForm):
    class Meta:
        model = Catedratico
        fields = ['NombresCatedratico', 'ApellidosCatedratico', 'DocumentoDPI', 'DPI', 'FechaNacimientoCatedratico', 'Tel_Catedratico']
        labels = {
            'NombresCatedratico': 'Nombres del Catedrático',
            'ApellidosCatedratico': 'Apellidos del Catedrático',
            'DocumentoDPI': 'Tipo de Documento',
            'DPI': 'Documento',
            'FechaNacimientoCatedratico': 'Fecha de Nacimiento del Catedrático',
            'Tel_Catedratico': 'Teléfono del Catedrático',
        }
        widgets = {
            
            'NombresCatedratico': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,20}',}),
            'ApellidosCatedratico': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{3,30}',}),
            'DocumentoDPI': forms.Select(
                attrs={'class': 'form-control'}),
            'DPI': forms.TextInput(
                attrs={'class': 'form-control',
                       'Type':'number',
                       'pattern':'[0,9].{12,15}'}),
            'FechaNacimientoCatedratico': forms.DateInput(
                attrs={'class': 'form-control', 
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date',}),
            'Tel_Catedratico': forms.TextInput(
                attrs={'class': 'form-control',
                    'placeholder': '########'}),

        }

    def clean_Tel_Catedratico(self):
        telefono_catedratico = self.cleaned_data['Tel_Catedratico']
        telefono_validator(telefono_catedratico)
        return telefono_catedratico

    def clean_FechaNacimientoCatedratico(self):
        fecha_nacimiento = self.cleaned_data.get('FechaNacimientoCatedratico')
        fecha_rango_validator(fecha_nacimiento)
        return fecha_nacimiento
    
    def clean_NombresCatedratico(self):
        nombres_catedratico = self.cleaned_data.get('NombresCatedratico')
        solo_letras_validator(nombres_catedratico)
        no_campos_vacios_validator(nombres_catedratico)
        no_dos_espacios_validator(nombres_catedratico)
        no_numeros_validator(nombres_catedratico)
        no_tres_letras_iguales_validator(nombres_catedratico)
        return nombres_catedratico.capitalize()
    
    def clean_ApellidosCatedratico(self):
        apellidos_catedratico = self.cleaned_data.get('ApellidosCatedratico')
        solo_letras_validator(apellidos_catedratico)
        no_campos_vacios_validator(apellidos_catedratico)
        no_dos_espacios_validator(apellidos_catedratico)
        no_numeros_validator(apellidos_catedratico)
        no_tres_letras_iguales_validator(apellidos_catedratico)
        return apellidos_catedratico.capitalize()




class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['NombresTutor', 'ApellidosTutor', 'DocumentoDPI', 'DPI', 'Tel_Tutor', 'Parentesco']
        labels = {
            'NombresTutor': 'Nombres del Tutor',
            'ApellidosTutor': 'Apellidos del Tutor',
            'DocumentoDPI': 'Tipo de Documento',
            'DPI': 'Documento',
            'Tel_Tutor': 'Teléfono del Tutor',
            'Parentesco': 'Parentesco',
        }
        widgets = {
            'NombresTutor': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,20}',}),
            'ApellidosTutor': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{3,30}',}),
            'DocumentoDPI': forms.Select(
                attrs={'class': 'form-control'}),
            'DPI': forms.TextInput(
                attrs={'class': 'form-control',
                       'Type':'Number',
                       'pattern':'[0,9].{12,15}'}),
            'Tel_Tutor': forms.TextInput(
                attrs={'class': 'form-control',
                
                    'placeholder': '########'}),
            'Parentesco': forms.TextInput(
                attrs={'class': 'form-control',
                       }),
        }

    def clean_NombresTutor(self):
        nombres_tutor = self.cleaned_data.get('NombresTutor')
        solo_letras_validator(nombres_tutor)
        no_campos_vacios_validator(nombres_tutor)
        no_tres_letras_iguales_validator(nombres_tutor)
        return nombres_tutor.capitalize()

    def clean_ApellidosTutor(self):
        apellidos_tutor = self.cleaned_data.get('ApellidosTutor')
        solo_letras_validator(apellidos_tutor)
        no_campos_vacios_validator(apellidos_tutor)
        no_tres_letras_iguales_validator(apellidos_tutor)
        return apellidos_tutor

    def clean_Tel_Tutor(self):
        telefono_tutor = self.cleaned_data.get('Tel_Tutor')
        telefono_validator(telefono_tutor)
        return telefono_tutor



    def clean_Parentesco(self):
        parentesco = self.cleaned_data.get('Parentesco')
        solo_letras_validator(parentesco)
        no_campos_vacios_validator(parentesco)
        no_tres_letras_iguales_validator(parentesco)
        return parentesco.capitalize()

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['Asignatura', 'Catedratico', 'NivelEducativo']
        labels = {
            'Asignatura': 'Nombre de la Asignatura',
            'Catedratico': 'Nombre del Catedratico',
            'NivelEducativo': 'Nivel Educativo',
        }
        widgets = {
            'Asignatura': forms.TextInput(
                attrs={'class': 'form-control'}),
            'Catedratico': forms.Select(
                attrs={'class': 'form-control'}),
            'NivelEducativo': forms.Select(
                attrs={'class': 'form-control'}),
        }

    def clean_Asignatura(self):
        asignatura = self.cleaned_data.get('Asignatura')
        solo_letras_validator(asignatura)
        no_campos_vacios_validator(asignatura)
        no_dos_espacios_validator(asignatura)
        no_numeros_validator(asignatura)
        no_tres_letras_iguales_validator(asignatura)
        return asignatura.capitalize()

from django import forms
from .models import Matricula, Pago, Usuario

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['pagos', 'tutor', 'alumno', 'grado', 'usuario', 'fecha_matricula']
        labels = {
            'pagos': 'Pagos',
            'tutor': 'Tutor',
            'alumno': 'Alumno',
            'grado': 'Grado',
            'usuario': 'Nombre del Usuario',
            'fecha_matricula': 'Fecha de la Matrícula',
        }
        widgets = {
            'pagos': forms.Select(attrs={'class': 'form-control'}),
            'tutor': forms.TextInput(attrs={'class': 'form-control'}),
            'alumno': forms.TextInput(attrs={'class': 'form-control'}),
            'grado': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'fecha_matricula': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD',
                'type': 'date',
            }),
        }

    def clean_tutor(self):
        tutor = self.cleaned_data.get('tutor')
        solo_letras_validator(tutor)
        no_campos_vacios_validator(tutor)
        no_dos_espacios_validator(tutor)
        no_numeros_validator(tutor)
        no_tres_letras_iguales_validator(tutor)
        return tutor.capitalize()
    
    def clean_alumno(self):
        alumno = self.cleaned_data.get('alumno')
        solo_letras_validator(alumno)
        no_campos_vacios_validator(alumno)
        no_dos_espacios_validator(alumno)
        no_numeros_validator(alumno)
        no_tres_letras_iguales_validator(alumno)
        return alumno.capitalize()
    


class ReportesForm(forms.ModelForm):
    class Meta:
        model = Reportes
        fields = ['TipoReporte', 'Alumno', 'DescripcionReporte', 'FechaReporte']
        labels = {
            'TipoReporte': 'Tipos de Reportes',
            'Alumno': 'Nombre del Alumno',
            'DescripcionReporte': 'Descripción del Reporte',
            'FechaReporte': 'Fecha del Reporte',
        }
        widgets = {
            'TipoReporte': forms.Select(
                attrs={'class': 'form-control'}),
            'Alumno': forms.Select(
                attrs={'class': 'form-control'}),
            'DescripcionReporte': forms.TextInput(
                attrs={'class': 'form-control'}),
            'FechaReporte': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date'}),
        }

    def clean_FechaReporte(self):
        fecha_reporte = self.cleaned_data.get('FechaReporte')
        fecha_rango_validator(fecha_reporte)
        return fecha_reporte
    
    def clean_DescripcionReporte(self):
        descripcion_reporte = self.cleaned_data.get('DescripcionReporte')
        solo_letras_validator(descripcion_reporte)
        no_campos_vacios_validator(descripcion_reporte)
        no_dos_espacios_validator(descripcion_reporte)
        no_numeros_validator(descripcion_reporte)
        no_tres_letras_iguales_validator(descripcion_reporte)
        return descripcion_reporte.capitalize()
    
class ExpedienteMedicoForm(forms.ModelForm):
    class Meta:
        model = ExpedienteMedico
        fields = ['Grado', 'Alumno', 'Tutor', 'EnfermedadCronica1', 'EnfermedadCronica2', 'EnfermedadCronica3', 'MedicamentoUsoDiario1', 'MedicamentoUsoDiario2', 'Alergia1', 'Alergia2', 'Alergia3']
        labels = {
            'Grado': 'Grado',
            'Alumno': 'Nombre del Alumno',
            'Tutor': 'Nombre del Tutor',
            'EnfermedadCronica1': 'Nombre de la Enfermedad Cronica1',
            'EnfermedadCronica2': 'Nombre de la Enfermedad Cronica2',
            'EnfermedadCronica3': 'Nombre de la Enfermedad Cronica3',
            'MedicamentoUsoDiario1': 'Nombre del Medicamento Uso Diario1',
            'MedicamentoUsoDiario2': 'Nombre del Medicamento Uso Diario2',
            'Alergia1': 'Nombre de la Alergia1',
            'Alergia2': 'Nombre de la Alergia2',
            'Alergia3': 'Nombre de la Alergia3',
            
        }
        widgets = {
            'Grado': forms.Select(
                attrs={'class': 'form-control'}),
            'Alumno': forms.Select(
                attrs={'class': 'form-control'}),
            'Tutor': forms.Select(
                attrs={'class': 'form-control'}),
            'EnfermedadCronica1': forms.TextInput(
                attrs={'class': 'form-control'}),
            'EnfermedadCronica2': forms.TextInput(
                attrs={'class': 'form-control'}),
            'EnfermedadCronica3': forms.TextInput(
                attrs={'class': 'form-control'}),
            'MedicamentoUsoDiario1': forms.TextInput(
                attrs={'class': 'form-control'}),
            'MedicamentoUsoDiario2': forms.TextInput(
                attrs={'class': 'form-control'}),
            'Alergia1': forms.TextInput(
                attrs={'class': 'form-control'}),
            'Alergia2': forms.TextInput(
                attrs={'class': 'form-control'}),
            'Alergia3': forms.TextInput(
                attrs={'class': 'form-control'}),
        }

    def clean_EnfermedadCronica1(self):
        enfermedad_cronica1 = self.cleaned_data.get('EnfermedadCronica1')
        solo_letras_validator(enfermedad_cronica1)
        no_campos_vacios_validator(enfermedad_cronica1)
        no_dos_espacios_validator(enfermedad_cronica1)
        no_numeros_validator(enfermedad_cronica1)
        no_tres_letras_iguales_validator(enfermedad_cronica1)
        return enfermedad_cronica1.capitalize()
    
    def clean_EnfermedadCronica2(self):
        enfermedad_cronica2 = self.cleaned_data.get('EnfermedadCronica2')
        solo_letras_validator(enfermedad_cronica2)
        no_campos_vacios_validator(enfermedad_cronica2)
        no_dos_espacios_validator(enfermedad_cronica2)
        no_numeros_validator(enfermedad_cronica2)
        no_tres_letras_iguales_validator(enfermedad_cronica2)
        return enfermedad_cronica2.capitalize()
    
    def clean_EnfermedadCronica3(self):
        enfermedad_cronica3 = self.cleaned_data.get('EnfermedadCronica3')
        solo_letras_validator(enfermedad_cronica3)
        no_campos_vacios_validator(enfermedad_cronica3)
        no_dos_espacios_validator(enfermedad_cronica3)
        no_numeros_validator(enfermedad_cronica3)
        no_tres_letras_iguales_validator(enfermedad_cronica3)
        return enfermedad_cronica3.capitalize()
    
    def clean_MedicamentoUsoDiario1(self):
        medicamento_uso_diario1 = self.cleaned_data.get('MedicamentoUsoDiario1')
        solo_letras_validator(medicamento_uso_diario1)
        no_campos_vacios_validator(medicamento_uso_diario1)
        no_dos_espacios_validator(medicamento_uso_diario1)
        no_numeros_validator(medicamento_uso_diario1)
        no_tres_letras_iguales_validator(medicamento_uso_diario1)
        return medicamento_uso_diario1.capitalize()
    
    def clean_MedicamentoUsoDiario2(self):
        medicamento_uso_diario2 = self.cleaned_data.get('MedicamentoUsoDiario2')
        solo_letras_validator(medicamento_uso_diario2)
        no_campos_vacios_validator(medicamento_uso_diario2)
        no_dos_espacios_validator(medicamento_uso_diario2)
        no_numeros_validator(medicamento_uso_diario2)
        no_tres_letras_iguales_validator(medicamento_uso_diario2)
        return medicamento_uso_diario2.capitalize()
    
    def clean_Alergia1(self):
        alergia1 = self.cleaned_data.get('Alergia1')
        solo_letras_validator(alergia1)
        no_campos_vacios_validator(alergia1)
        no_dos_espacios_validator(alergia1)
        no_numeros_validator(alergia1)
        no_tres_letras_iguales_validator(alergia1)
        return alergia1.capitalize()
    
    def clean_Alergia2(self):
        alergia2 = self.cleaned_data.get('Alergia2')
        solo_letras_validator(alergia2)
        no_campos_vacios_validator(alergia2)
        no_dos_espacios_validator(alergia2)
        no_numeros_validator(alergia2)
        no_tres_letras_iguales_validator(alergia2)
        return alergia2.capitalize()
    
    def clean_Alergia3(self):
        alergia3 = self.cleaned_data.get('Alergia3')
        solo_letras_validator(alergia3)
        no_campos_vacios_validator(alergia3)
        no_dos_espacios_validator(alergia3)
        no_numeros_validator(alergia3)
        no_tres_letras_iguales_validator(alergia3)
        return alergia3.capitalize()

class HorariosForm(forms.ModelForm):
    class Meta:
        model = HorariosNivelEducativo
        fields = ['Horario', 'HoraEntrada', 'HoraSalida']
        labels = {
            'Horario': 'Horario',
            'HoraEntrada': 'Hora de entrada',
            'HoraSalida': 'Hora de salida',
        }
        widgets = {
            'Horario': forms.TextInput(
                attrs={'class': 'form-control'}),
            'HoraEntrada': forms.TimeInput(
                attrs={'class': 'form-control'}),
            'HoraSalida': forms.TimeInput(
                attrs={'class': 'form-control'}),
        }
    
    def clean_Horario(self):
        horario = self.cleaned_data.get('Horario')
        solo_letras_validator(horario)
        no_campos_vacios_validator(horario)
        no_dos_espacios_validator(horario)
        no_numeros_validator(horario)
        no_tres_letras_iguales_validator(horario)
        no_numeros_ni_especiales_validator(horario)
        return horario.capitalize()

class NivelesForm(forms.ModelForm):
    class Meta:
        model = NivelEducativo
        fields = ['NivelEducativo', 'Horario']
        labels = {
            'NivelEducativo': 'Nivel Educativo',
            'Horario': 'Horario',
        }
        widgets = {
            'NivelEducativo': forms.TextInput(
                attrs={'class': 'form-control'}),
            'Horario': forms.Select(
                attrs={'class': 'form-control'}),
        }

    def clean_NivelEducativo(self):
        nivel_educativo = self.cleaned_data.get('NivelEducativo')
        solo_letras_validator(nivel_educativo)
        no_campos_vacios_validator(nivel_educativo)
        no_dos_espacios_validator(nivel_educativo)
        no_numeros_validator(nivel_educativo)
        no_tres_letras_iguales_validator(nivel_educativo)
        no_numeros_ni_especiales_validator(nivel_educativo)
        return nivel_educativo.capitalize()

class ParcialesForm(forms.ModelForm):
    class Meta:
        model = ParcialesAcademicos
        fields = ['ParcialAcademico', 'FechaInicio', 'FechaFinal', 'Año']
        labels = {
            'ParcialAcademico': 'Parcial Academico',
            'FechaInicio': 'Fecha de inicio del parcial',
            'FechaFinal': 'Fecha final del parcial',
            'Año':'Año',
        }
        widgets = {
            'ParcialAcademico': forms.TextInput(
                attrs={'class': 'form-control'}),
            'FechaInicio': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date'}),
            'FechaFinal': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date'}),
            'Año': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY', 
                       'type': 'date'}),
        }

    def clean_ParcialAcademico(self):
        parcial_academico = self.cleaned_data.get('ParcialAcademico')
        solo_letras_validator(parcial_academico)
        no_campos_vacios_validator(parcial_academico)
        no_dos_espacios_validator(parcial_academico)
        no_numeros_validator(parcial_academico)
        no_tres_letras_iguales_validator(parcial_academico)
        return parcial_academico.capitalize()
    
    def clean_FechaInicio(self):
        fecha_inicio = self.cleaned_data.get('FechaInicio')
        fechainicio_rango_parciales(fecha_inicio)
        return fecha_inicio
    
    def clean_FechaFinal(self):
        fecha_final = self.cleaned_data.get('FechaFinal')
        fechafinal_rango_parciales(fecha_final)
        return fecha_final

    def clean_Año(self):
        año = self.cleaned_data.get('Año')
        fechaaño_rango_año(año)
        return año

class NotasForm(forms.ModelForm):
    class Meta:
        model = NotasAlumnos
        fields = ['Asignatura', 'ParcialAcademico', 'ApellidosAlumno',  'NotaAcumulativo', 'NotaExamen', 'NotaFinal', 'PromedioClase']
        labels = {
            'Asignatura': 'Asignatura', 
            'ParcialAcademico':'Parcial', 
            'ApellidosAlumno':'Apellidos del Alumno', 
            'NotaAcumulativo': 'Nota de Acumulativo', 
            'NotaExamen': 'Nota de Examen', 
            'NotaFinal':'Nota final',
            'PromedioClase':'Promedio de clase'
        }
        widgets = {
             'Asignatura': forms.Select(
                attrs={'class': 'form-control'}),
        
            'ParcialAcademico': forms.Select(
                attrs={'class': 'form-control'}),
            'ApellidosAlumno': forms.Select(
                attrs={'class': 'form-control'}),
            'NotaAcumulativo': forms.NumberInput(
                attrs={'class': 'form-control',
                       'step':'.10'}),
            'NotaExamen': forms.NumberInput(
                attrs={'class': 'form-control',
                       'step':'.10'}),
            'NotaFinal':forms.NumberInput(
                attrs={'class': 'form-control',
                       'step':'.10'}),
            'PromedioClase':forms.NumberInput(
                attrs={'class': 'form-control',
                       'step':'.10'}),
              
           }
        
    def clean_NotaAcumulativo(self):
        nota_acumulativo = self.cleaned_data.get('NotaAcumulativo')
        notasacumulativo_longitud_validator(nota_acumulativo)
        return nota_acumulativo
    
    def clean_NotaExamen(self):
        nota_examen = self.cleaned_data.get('NotaExamen')
        notasexamen_longitud_validator(nota_examen)
        return nota_examen
    
    def clean_NotaFinal(self):
        nota_final = self.cleaned_data.get('NotaFinal')
        notasfinales_longitud_validator(nota_final)
        return nota_final

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña', max_length=100)


from django import forms

from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    usuario = forms.CharField(
        label='Usuario',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    )
    contraseña = forms.CharField(
        label='Contraseña',
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )

    def clean(self):
        cleaned_data = super().clean()
        usuario = cleaned_data.get('usuario')
        contraseña = cleaned_data.get('contraseña')

        if usuario and contraseña:
            user = authenticate(username=usuario, password=contraseña)
            if not user:
                raise forms.ValidationError('Credenciales incorrectas. Por favor, verifique sus datos.')

        return cleaned_data
    

from django import forms
from .models import Usuario

from django import forms
from .models import Usuario

from django import forms


    


from django import forms
from django.contrib.auth.models import User

class UserEditForm(forms.ModelForm):
    password = forms.CharField(
        label='contraseña',  # Cambio del atributo label a español
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
       help_text="La contraseña debe tener al menos 8 caracteres y contener al menos un número, una letra mayúscula y una letra minúscula."
    )
    confirm_password = forms.CharField(
        label='Confirmar contraseña',  # Cambio del atributo label a español
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'})
    )

    ACTIVO_CHOICES = [
        (True, 'Sí'),
        (False, 'No'),
    ]
    activo = forms.ChoiceField(
        choices=ACTIVO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'confirm_password', 'rol', 'activo']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['username'].widget.attrs['readonly'] = True

    def clean_activo(self):
        activo = self.cleaned_data.get('activo')
        if activo == 'True':
            # Si el campo activo se cambia a True, restablecer los intentos fallidos a 0
            self.instance.intentos_fallidos = 0
            self.instance.save()
        return activo

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden. Por favor, inténtelo de nuevo.')
        return confirm_password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return password

import re
import re

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'})
    )
    ACTIVO_CHOICES = [
        (True, 'Sí'),
        (False, 'No'),
    ]
    activo = forms.ChoiceField(
        choices=ACTIVO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'confirm_password', 'rol', 'activo','Empleado']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'Empleado': forms.Select(attrs={'class': 'form-control'}),
        }

    def _init_(self, *args, **kwargs):
        super(UserCreationForm, self)._init_(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password'].label = 'Contraseña'
        self.fields['confirm_password'].label = 'Confirmar Contraseña'




    def clean_username(self):
            username = self.cleaned_data['username']
            username = username.strip()  # Eliminar espacios en blanco al inicio y al final

            # Validar longitud mínima y máxima del nombre de usuario
            if len(username) < 5:
                raise forms.ValidationError('El nombre de usuario debe tener al menos 5 caracteres.')
            if len(username) > 30:
                raise forms.ValidationError('El nombre de usuario no puede tener más de 30 caracteres.')

            # Validar caracteres permitidos (letras, números y guiones bajos)
            if not re.match(r'^[a-zA-Z0-9_]+$', username):
                raise forms.ValidationError('El nombre de usuario solo puede contener letras, números y guiones bajos (_).')

            # Validar que no haya dobles espacios o dos letras seguidas
            if re.search(r'\s{2}', username) or re.search(r'(.)\1{1}', username):
                raise forms.ValidationError('El nombre de usuario no puede contener dobles espacios ni dos letras seguidas.')

            # Verificar si el nombre de usuario ya está en uso
            base_username = username.lower()
            counter = 1
            while Usuario.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
                if counter > 100:
                    raise forms.ValidationError('No se pudo generar un nombre de usuario único. Por favor, elige otro.')
            
            # Si el nombre de usuario original estaba disponible, mostrar una sugerencia con un número al final
            if username != self.cleaned_data['username']:
                raise forms.ValidationError(f"El nombre de usuario {self.cleaned_data['username']} ya está en uso. ¿Qué tal {username}?")
            
            return username
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden. Por favor, inténtelo de nuevo.')
        return confirm_password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return password



class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ['Grado', 'NivelEducativo']
        labels = {
            'Grado': 'Nombre del Grado',
            'NivelEducativo': 'Nivel Educativo',
        }
        widgets = {
            'Grado': forms.TextInput(
                attrs={'class': 'form-control',
                       }),
            'NivelEducativo': forms.Select(
                attrs={'class': 'form-control'}),
        }

    def clean_Grado(self):
        grado = self.cleaned_data.get('Grado')
        solo_letras_validator(grado)
        no_campos_vacios_validator(grado)
        no_dos_espacios_validator(grado)
        no_numeros_validator(grado)
        no_tres_letras_iguales_validator(grado)
        return grado.capitalize()
    

class ExpedienteEscolarForm(forms.ModelForm):
    class Meta:
        model = ExpedienteEscolar
        fields = ['Actitud', 'Alumno', 'InstitutoAnterior', 'PromedioAnualAnterior', 'Tutor']
        labels = {
            'Actitud': 'Actitud del Alumno',
            'Alumno': 'Nombre del Alumno',
            'InstitutoAnterior': 'Instituto Anterior del Alumno',
            'PromedioAnualAnterior': 'Promedio Anual Anterior del Alumno',
            'Tutor': 'Nombre del Tutor',
        }
        widgets = {
            'Actitud': forms.Select(
                attrs={'class': 'form-control'}),
            'Alumno': forms.Select(
                attrs={'class': 'form-control'}),
            'InstitutoAnterior': forms.TextInput(
                attrs={'class': 'form-control'}),
            'PromedioAnualAnterior': forms.TextInput(
                attrs={'class': 'form-control'}),
            'Tutor': forms.Select(
                attrs={'class': 'form-control'}),
        }

    def clean_InstitutoAnterior(self):
        instituto_anterior = self.cleaned_data.get('InstitutoAnterior')
        solo_letras_validator(instituto_anterior)
        no_campos_vacios_validator(instituto_anterior)
        no_dos_espacios_validator(instituto_anterior)
        no_numeros_validator(instituto_anterior)
        no_tres_letras_iguales_validator(instituto_anterior)
        return instituto_anterior.capitalize()
    
class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['departamento']
        labels = {
            'departamento': 'Departamento',
        }
        widgets = {
            'departamento': forms.TextInput(
                attrs={'class': 'form-control'}),
            
        }
   
    def clean_Departamento(self):
        departamento = self.cleaned_data['Departamento']
        # Validar que no haya dobles espacios en blanco seguidos
        if '  ' in departamento:
            raise forms.ValidationError("No se permiten dobles espacios en blanco seguidos.")
        # Validar que el campo no esté vacío
        if not departamento.strip():
            raise forms.ValidationError("El campo Departamento no puede estar vacío.")
        # Validar si el nombre del departamento ya está registrado en la base de datos
        if Departamento.objects.filter(Departamento__iexact=departamento).exists():
            raise forms.ValidationError("Este nombre de departamento ya está registrado.")
        # Validar que no haya 3 letras iguales repetidas
        no_tres_letras_iguales_validator(departamento)
        # Validar que solo contenga letras y acentos
        no_numeros_ni_especiales_validator(departamento)
        return departamento
    def get_error_list(self):
        errors = []
        for field, error_list in self.errors.items():
            for error in error_list:
                errors.append(f"{self[field].label}: {error}")
        return errors


class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['nombreMunicipio', 'departamento']
        labels = {
            'nombeMunicipio': 'Municipio',
            'departamento': 'Departamento',
        }
        widgets = {
            'nombreMunicipio': forms.TextInput(
                attrs={'class': 'form-control'}),
            'departamento': forms.Select(
                attrs={'class': 'form-control'}),
        }
    
    def clean_nombreMunicipio(self):
        nombre_municipio = self.cleaned_data.get('nombreMunicipio')
        solo_letras_validator(nombre_municipio)
        no_campos_vacios_validator(nombre_municipio)
        no_dos_espacios_validator(nombre_municipio)
        no_numeros_validator(nombre_municipio)
        no_tres_letras_iguales_validator(nombre_municipio)
        return nombre_municipio.capitalize()

class PagoForm(forms.ModelForm):
    Tutor = forms.ModelChoiceField(queryset=Tutor.objects.distinct(), label='Tutor:', widget=forms.Select(attrs={'class': 'form-control'}))
    Alumno = forms.ModelChoiceField(queryset=Alumno.objects.none(), label='Alumno:', widget=forms.Select(attrs={'class': 'form-control'}))
    TipoPago = forms.ModelChoiceField(queryset=TipoPago.objects.all(), label='Tipo de Pago:', widget=forms.Select(attrs={'class': 'form-control'}))
    monto = forms.DecimalField(label='Precio:', disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Tutor'].label_from_instance = lambda obj: f"{obj.NombresTutor} {obj.ApellidosTutor}"
        self.fields['Alumno'].queryset = Alumno.objects.none()

        if 'Tutor' in self.data:
            try:
                tutor_id = int(self.data.get('Tutor'))
                alumno_ids = TutoresAlumnos.objects.filter(Tutor_id=tutor_id).values_list('Alumno_id', flat=True)
                self.fields['Alumno'].queryset = Alumno.objects.filter(id__in=alumno_ids)
            except (ValueError, TypeError):
                pass

    class Meta:
        model = Pago
        fields = ['Tutor', 'Alumno', 'Meses', 'TipoPago', 'monto']
        labels = {
            'Meses': 'Mes a pagar:',
            
        }
        widgets = {
            'Meses': forms.Select(attrs={'class': 'form-control'}),
            
        }




class MensualidadForm(forms.ModelForm):
    class Meta:
        model = Meses
        fields = ['Meses']
        labels = {
            'Meses': 'Mes.',
        }
        widgets = {
            'Meses': forms.TextInput(
                attrs={'class': 'form-control'}),
            
        }

    def clean_Meses(self):
        mes = self.cleaned_data.get('Meses')
        solo_letras_validator(mes)
        no_campos_vacios_validator(mes)
        no_dos_espacios_validator(mes)
        no_numeros_validator(mes)
        no_tres_letras_iguales_validator(mes)
        return mes.capitalize()
    
class ParametrosSARForm(forms.ModelForm):
    class Meta:
        model = ParametrosSAR
        fields = ['CAI', 'RTN', 'RangoInicial', 'RangoFinal', 'FechaEmision', 'FechaVencimiento', 'Correlativo']
        labels = {
            'CAI': 'CAI:',
            'RTN': 'RTN:',
            'RangoInicial': 'Rango Inicial:',
            'RangoFinal': 'Rango Final:',
            'FechaEmision': 'Fecha de emision:',
            'FechaVencimiento': 'Fecha de vencimiento',
            'Correlativo': 'Correlativo'
        }
        widgets = {
            'CAI': forms.TextInput(
                attrs={'class': 'form-control'}),
            'RTN': forms.TextInput(
                attrs={'class': 'form-control'}),
            'RangoInicial': forms.TextInput(
                attrs={'class': 'form-control'}),
            'RangoFinal': forms.TextInput(
                attrs={'class': 'form-control'}),
            'FechaEmision': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date'}),
            'FechaVencimiento': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date'}),
            'Correlativo': forms.DateInput(
                attrs={'class': 'form-control'}),
        }
    
    def clean_FechaEmision(self):
        fecha_emision = self.cleaned_data.get('FechaEmision')
        fecha_rango_emision(fecha_emision)
        return fecha_emision
    
    def clean_FechaVencimiento(self):
        fecha_vencimiento = self.cleaned_data.get('FechaVencimiento')
        fecha_rango_vencimiento(fecha_vencimiento)
        return fecha_vencimiento
    
    def clean_Correlativo(self):
        correlativo = self.cleaned_data['Correlativo']
        correlativo_validator(correlativo)
        return correlativo

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaEmpleado
        fields = ['CategoriaEmpleado']
        labels = {
            'CategoriaEmpleado': 'Categoria de empleado',
        }
        widgets = {
            'CategoriaEmpleado': forms.TextInput(
                attrs={'class': 'form-control'}),
        }

    def clean_CategoriaEmpleado(self):
        categoria_empleado = self.cleaned_data.get('CategoriaEmpleado')
        solo_letras_validator(categoria_empleado)
        no_campos_vacios_validator(categoria_empleado)
        no_dos_espacios_validator(categoria_empleado)
        no_numeros_validator(categoria_empleado)
        no_tres_letras_iguales_validator(categoria_empleado)
        return categoria_empleado.capitalize()

class TipoPagoEditForm(TipoPagoForm):
    class Meta:
        model = TipoPago
        fields = ['nombre', 'descripcion', 'monto']
        labels = {
            'nombre': 'Nombre del pago',
            'descripcion': 'Descripción del pago',
            'monto': 'Precio del pago'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'readonly': 'readonly'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        if "  " in nombre:
            raise forms.ValidationError('El nombre no debe contener más de un espacio en blanco consecutivo.')

        for i in range(len(nombre) - 2):
            if nombre[i] == nombre[i+1] == nombre[i+2]:
                raise forms.ValidationError('El nombre no debe contener tres letras iguales consecutivas.')

        if any(char.isdigit() for char in nombre):
            raise forms.ValidationError('El nombre no debe contener números.')

        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']

        if "  " in descripcion:
            raise forms.ValidationError('La descripción no debe contener más de un espacio en blanco consecutivo.')

        for i in range(len(descripcion) - 2):
            if descripcion[i] == descripcion[i+1] == descripcion[i+2]:
                raise forms.ValidationError('La descripción no debe contener tres letras iguales consecutivas.')

        if any(char.isdigit() for char in descripcion):
            raise forms.ValidationError('La descripción no debe contener números.')

        return descripcion



class DocumentoForm(forms.ModelForm):
    class Meta:
        model = DocumentoDPI
        fields = ['DocumentoDPI']
        labels = {
            'DocumentoDPI': 'Documento de identificacion personal:',
        }
        widgets = {
            'DocumentoDPI': forms.TextInput(
                attrs={'class': 'form-control'}),
            
        }
    
    def clean_DocumentoDPI(self):
        documentodpi = self.cleaned_data.get('DocumentoDPI')
        solo_letras_validator(documentodpi)
        no_campos_vacios_validator(documentodpi)
        no_dos_espacios_validator(documentodpi)
        no_numeros_validator(documentodpi)
        no_tres_letras_iguales_validator(documentodpi)
        return documentodpi.capitalize()

from django import forms
from .models import TipoPago

from django import forms
from .models import TipoPago

class TipoPagoForm(forms.ModelForm):
    class Meta:
        model = TipoPago
        fields = ['nombre', 'descripcion', 'monto']
        labels = {
            'nombre': 'Nombre del pago',
            'descripcion': 'Descripción del pago',
            'monto': 'Precio del pago'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if "  " in nombre:
            raise forms.ValidationError('El nombre no debe contener más de un espacio en blanco consecutivo.')
        
        for i in range(len(nombre) - 2):
            if nombre[i] == nombre[i+1] == nombre[i+2]:
                raise forms.ValidationError('El nombre no debe contener tres letras iguales consecutivas.')
        
        if any(char.isdigit() for char in nombre):
            raise forms.ValidationError('El nombre no debe contener números.')
        
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        
        if "  " in descripcion:
            raise forms.ValidationError('La descripción no debe contener más de un espacio en blanco consecutivo.')
        
        for i in range(len(descripcion) - 2):
            if descripcion[i] == descripcion[i+1] == descripcion[i+2]:
                raise forms.ValidationError('La descripción no debe contener tres letras iguales consecutivas.')
        
        if any(char.isdigit() for char in descripcion):
            raise forms.ValidationError('La descripción no debe contener números.')
        
        return descripcion
         
    def clean_monto(self):
        


        


from django import forms
from .models import TipoPago

class TipoPagoActualizarForm(forms.ModelForm):
    class Meta:
        model = TipoPago
        fields = ['nombre', 'monto']  # Campos que se pueden actualizar

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        
        if instance:
            self.fields['nombre'] = forms.CharField(
                initial=instance.nombre,
                widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
            )
            
        self.fields['monto'] = forms.DecimalField(
            widget=forms.TextInput(attrs={'class': 'form-control'}),
            label='Nuevo Monto',
            help_text='Ingrese el nuevo monto.',
            validators=[self.validate_monto]
        )

    def validate_monto(self, value):
        if value <= 0:
            raise forms.ValidationError('El monto debe ser mayor que cero.')





class TipoSanguineoForm(forms.ModelForm):
    class Meta:
        model = TipoSanguineo
        fields = ['TipoSanguineo']
        labels = {
            'TipoSanguineo': 'Tipo Sanguineo',
        }
        widgets = {
            'TipoSanguineo': forms.TextInput(
                attrs={'class': 'form-control'}),
        }

    def clean_TipoSanguineo(self):
        tipo_sanguineo = self.cleaned_data.get('TipoSanguineo')
        no_campos_vacios_validator(tipo_sanguineo)
        no_dos_espacios_validator(tipo_sanguineo)
        no_numeros_validator(tipo_sanguineo)
        no_tres_letras_iguales_validator(tipo_sanguineo)
        return tipo_sanguineo.capitalize()
    
class TipoReporteForm(forms.ModelForm):
    class Meta:
        model = TipoReporte
        fields = ['TipoReporte']
        labels = {
            'TipoReporte': 'Tipo de reporte',
        }
        widgets = {
            'TipoReporte': forms.TextInput(
                attrs={'class': 'form-control'}),   
        }

    def clean_TipoReporte(self):
        tipo_reporte = self.cleaned_data.get('TipoReporte')
        solo_letras_validator(tipo_reporte)
        no_campos_vacios_validator(tipo_reporte)
        no_dos_espacios_validator(tipo_reporte)
        no_numeros_validator(tipo_reporte)
        no_tres_letras_iguales_validator(tipo_reporte)
        return tipo_reporte.capitalize()
    
class FacturaForm(forms.ModelForm):
    class Meta:
        model= Factura
        fields=['numero_factura', 'ParametrosSAR', 'CentroEducativo', 'pago']





class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['Tutor', 'Alumno', 'TipoPago', 'Meses']
        labels = {
            'Tutor': 'Tutor:',
            'Alumno': 'Alumno:',
            'TipoPago': 'Movimiento a pagar:',
            'Meses': 'Mes a pagar:',
        }
        widgets = {
            'Tutor': forms.Select(
                attrs={'class': 'form-control'}),
            'Alumno': forms.Select(
                attrs={'class': 'form-control'}),
            'TipoPago': forms.Select(
                attrs={'class': 'form-control'}),
            'Meses': forms.Select(
                attrs={'class': 'form-control'}),    
        }
class SeccionForm(forms.ModelForm):
    class Meta:
        model = Seccion
        fields = ['Seccion']
        labels = {
            'Seccion': 'Sección',
        }
        widgets = {
            'Seccion': forms.TextInput(
                attrs={'class': 'form-control'}),
            
        }

    def clean_Seccion(self):
        seccion = self.cleaned_data.get('Seccion')
        solo_letras_validator(seccion)
        no_campos_vacios_validator(seccion)
        no_dos_espacios_validator(seccion)
        no_numeros_validator(seccion)
        no_tres_letras_iguales_validator(seccion)
        return seccion.capitalize()

class ActitudForm(forms.ModelForm):
    class Meta:
        model = Actitud
        fields = ['Actitud']
        labels = {
            'Actitud': 'Actitud',
        }
        widgets = {
            'Actitud': forms.TextInput(
                attrs={'class': 'form-control'}),
            
        }

    def clean_Actitud(self):
        actitud = self.cleaned_data.get('Actitud')
        solo_letras_validator(actitud)
        no_campos_vacios_validator(actitud)
        no_dos_espacios_validator(actitud)
        no_numeros_validator(actitud)
        no_tres_letras_iguales_validator(actitud)
        return actitud.capitalize()

class CentroEducativoForm(forms.ModelForm):
    class Meta:
        model = CentroEducativo
        fields = ['NombreCentro', 'CodigoCentro', 'Titularidad', 'Localidad', 'Sucursal', 'Telefono']
        labels = {
            'NombreCentro': 'Nombre del Centro Educativo',
            'CodigoCentro': 'Código del Centro Educativo',
            'Titularidad': 'Titularidad del Centro Educativo',
            'Localidad': 'Localidad del Centro Educativo',
            'Sucursal': 'Sucursal del Centro Educativo',
            'Telefono': 'Teléfono del Centro Educativo',
        }
        widgets = {
            'NombreCentro': forms.TextInput(
                attrs={'class': 'form-control'}),
            'CodigoCentro': forms.TextInput(
                attrs={'class': 'form-control'}),
            'Titularidad': forms.TextInput(
                attrs={'class': 'form-control'}),
            'Localidad': forms.Select(
                attrs={'class': 'form-control'}),
            'Sucursal': forms.TextInput(
                attrs={'class': 'form-control'}),
            'Telefono': forms.TextInput(
                attrs={'class': 'form-control',
                    'placeholder': '########'}),
        }

    def clean_NombreCentro(self):
        nombre_centro = self.cleaned_data.get('NombreCentro')
        solo_letras_validator(nombre_centro)
        no_campos_vacios_validator(nombre_centro)
        no_dos_espacios_validator(nombre_centro)
        no_numeros_validator(nombre_centro)
        no_tres_letras_iguales_validator(nombre_centro)
        return nombre_centro.capitalize()
    
    def clean_Titularidad(self):
        titularidad = self.cleaned_data.get('Titularidad')
        solo_letras_validator(titularidad)
        no_campos_vacios_validator(titularidad)
        no_dos_espacios_validator(titularidad)
        no_numeros_validator(titularidad)
        no_tres_letras_iguales_validator(titularidad)
        return titularidad.capitalize()
    
    

class TutoresAlumnosForm(forms.ModelForm):
    class Meta:
        model = TutoresAlumnos
        fields = ['Tutor', 'Alumno']
        labels = {
            'Tutor': 'Nombre del Tutor',
            'Alumno': 'Nombre del Alumno',
        }
        widgets = {
            'Tutor': forms.Select(
                attrs={'class': 'form-control'}),
            'Alumno': forms.Select(
                attrs={'class': 'form-control'}),
        }






