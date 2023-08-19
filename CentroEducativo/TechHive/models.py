import re
from typing import Required
from django.contrib.auth.hashers import make_password
from django.db import models
from django.db.models.signals import pre_save
from django import forms
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from django.dispatch import receiver
ValidacionNumeros = RegexValidator(r'^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$',"No se puede ingresar números a este campo.")
ValidacionLetras = RegexValidator(r'^[0-9 ]*$',"No se puede ingresar letras a este campo.")
ValidacionTelefono = RegexValidator(r'^[[2,3,7,8,9]{1}[0-9]{3}[0-9]{4}]*$',
                         "No puede ingresar letras en este campo, este campo debe comenzar con 2,3,8,9, este campo debe tener 8 a 11 digitos")



from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

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

def no_numeros_validator(value):
    if any(char.isdigit() for char in value):
        raise models.ValidationError('Este campo no debe contener números.')

def no_letras_validator(value):
    if any(char.isalpha() for char in value):
        raise models.ValidationError('Este campo no debe contener letras.')

def no_dos_espacios_validator(value):
    if '  ' in value:
        raise ValidationError('No se permiten dos espacios en blanco seguidos.')

def no_tres_letras_iguales_validator(value):
    for i in range(len(value) - 2):
        if value[i] == value[i+1] == value[i+2]:
            raise ValidationError('No se permiten tres letras iguales seguidas.')

def no_repita_nombre_validator(value):
    if Empleado.objects.filter(NombresEmpleado__iexact=value).exists():
        raise ValidationError('Este nombre ya existe en la base de datos.')

def telefono_validator(value):
    if not value.isdigit():
        raise ValidationError('El teléfono debe contener solo dígitos numéricos.')

    if len(value) != 8:
        raise ValidationError('El teléfono debe tener 8 dígitos.')

    if not value.startswith(('9', '8', '3')):
        raise ValidationError('El teléfono debe iniciar con 9, 8 o 3.')

def dni_validator(value):
    if not value.isdigit():
        raise ValidationError('El DNI debe contener solo dígitos numéricos.')

    if len(value) != 13:
        raise ValidationError('El DNI debe tener 13 dígitos.')

    if Empleado.objects.filter(DPI=value).exists():
        raise ValidationError('Este DNI ya existe en la base de datos.')

def rtn_validator(value):
    if not value.isdigit():
        raise ValidationError('El RTN debe contener solo dígitos numéricos.')

    if len(value) != 14:
        raise ValidationError('El RTN debe tener 14 dígitos.')

def pasaporte_validator(value):
    if not value.isalnum():
        raise ValidationError('El pasaporte debe contener solo caracteres alfanuméricos.')

    if len(value) != 20:
        raise ValidationError('El pasaporte debe tener 20 caracteres.')


class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    departamento = models.CharField(max_length=100,unique=True)
    

    def __str__(self):
        return self.departamento

class Municipio(models.Model):
    nombreMunicipio = models.CharField(max_length=100,unique=True)
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreMunicipio

class TipoSanguineo(models.Model):
    TipoSanguineo = models.CharField(max_length=3)

    def __str__(self):
        return self.TipoSanguineo
    
class DocumentoDPI(models.Model):
    DocumentoDPI = models.CharField(max_length=30)
    longitud = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.DocumentoDPI
    

class HorariosNivelEducativo(models.Model):
    Horario = models.CharField(max_length=15, help_text='No debe contener numeros, caracteres 5-15')
    HoraEntrada = models.TimeField()
    HoraSalida = models.TimeField()

    def __str__(self):
        return f"Horario: {self.Horario} , {self.HoraEntrada} - {self.HoraSalida}"

class NivelEducativo(models.Model):
    NivelEducativo = models.CharField(max_length=20, help_text='No debe contener numeros, caractreres: 5-20 ')
    Horario = models.ForeignKey(HorariosNivelEducativo, on_delete=models.CASCADE)

    def __str__(self):
        return self.NivelEducativo

class Grado(models.Model):
    Grado = models.CharField(max_length=25)
    NivelEducativo = models.ForeignKey(NivelEducativo, on_delete=models.CASCADE)

    def __str__(self):
        return self.Grado

class Seccion(models.Model):
    Seccion = models.CharField(max_length=1)

    def __str__(self):
        return self.Seccion


class TipoPago(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    monto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nombre

class TipoPagoHistorico(models.Model):
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(null=True, blank=True)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.tipo_pago} - {self.fecha_inicio} to {self.fecha_fin}"


class Meses(models.Model):
    Meses = models.CharField(max_length=15)

    def __str__(self):
        return self.Meses
    
class Tutor(models.Model):
    NombresTutor = models.CharField(max_length=20,  help_text='No debe contener numeros, caracteres: 3-20 ')
    ApellidosTutor = models.CharField(max_length=30,  help_text='No debe contener numeros, caracteres: 2-30 ')
    DocumentoDPI = models.ForeignKey(DocumentoDPI, on_delete=models.CASCADE)
    DPI = models.CharField(max_length=20, unique=True,help_text='No, debe contenes letras, digitos: 13-15 ')
    Tel_Tutor = models.CharField(max_length=8,  help_text='Longitud requerida: 8 digitos ')
    Parentesco = models.CharField(max_length=15, help_text='No debe contener numeros, caracteres 3-15 ')
    

    def __str__(self):
        return f"{self.NombresTutor} {self.ApellidosTutor} , Parentesco: {self.Parentesco} "


class Alumno(models.Model):
    

    NombresAlumno = models.CharField(max_length=20, help_text='No debe contener numeros, caracteres: 3-20 ')
    ApellidosAlumno = models.CharField(max_length=30, help_text='No debe contener numeros, caracteres: 2-30 ')
    DocumentoDPI = models.ForeignKey(DocumentoDPI, on_delete=models.CASCADE)
    DPI = models.CharField(max_length=20, unique=True,help_text='No, debe contenes letras, digitos: 13-15 ')
    FechaNacimientoAlumno = models.DateField()
    DireccionAlumno = models.CharField(max_length=30, help_text=' No se permiten espacios dobles, Longitud requerida: 5-30 ')
    Departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    Seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    Grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    TipoSanguineo = models.ForeignKey(TipoSanguineo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.NombresAlumno} {self.ApellidosAlumno}"    


class Catedratico(models.Model):
    NombresCatedratico = models.CharField(max_length=20, help_text='No debe contener numeros, caracteres 3-20 ')
    ApellidosCatedratico = models.CharField(max_length=30, help_text='No debe contener numeros, caracteres 2-30 ')
    DocumentoDPI = models.ForeignKey(DocumentoDPI, on_delete=models.CASCADE)
    DPI = models.CharField(max_length=20, unique=True,help_text='No, debe contenes letras, digitos: 13-15 ')
    FechaNacimientoCatedratico = models.DateField()
    Tel_Catedratico = models.CharField(max_length=8, help_text='No debe contener letras, 8 digitos' )

    def __str__(self):
        return f"{self.NombresCatedratico} {self.ApellidosCatedratico}"


class CategoriaEmpleado(models.Model):
    CategoriaEmpleado = models.CharField(max_length=30)

    def __str__(self):
        return self.CategoriaEmpleado



class TipoReporte(models.Model):
    TipoReporte = models.CharField(max_length=40)

    def __str__(self):
        return self.TipoReporte


class Asignatura(models.Model):
    Asignatura = models.CharField(max_length=25, help_text='No debe contener numeros, caracteres 5-25 ')
    Catedratico = models.ForeignKey(Catedratico, on_delete=models.CASCADE)
    NivelEducativo = models.ForeignKey(NivelEducativo, on_delete=models.CASCADE)

    def __str__(self):
        return self.Asignatura


class TutoresAlumnos(models.Model):
    Tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.Tutor}"


    
class Pago(models.Model):
    Tutor = models.ForeignKey(TutoresAlumnos, related_name='pagos_tutor', on_delete=models.CASCADE)
    Alumno = models.ForeignKey(TutoresAlumnos, related_name='pagos_alumno', on_delete=models.CASCADE)
    FechaHoraPago = models.DateTimeField(auto_now_add=True)
    TipoPago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    Meses= models.ForeignKey(Meses, on_delete=models.CASCADE)

    def __str__(self):
        return f" Pago: {self.id} - Tutor: {self.Tutor.Tutor} Alumno: {self.Alumno.Alumno}, Fecha y hora: {self.FechaHoraPago} Tipo Pago: {self.TipoPago} Mes: {self.Meses}"

    
class CentroEducativo(models.Model):
    NombreCentro= models.CharField(max_length=100)
    CodigoCentro = models.IntegerField()
    Titularidad= models.CharField(max_length=100)
    Localidad = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Sucursal = models.CharField(max_length=100)
    Telefono=models.IntegerField()

    def __str__(self):
        return f"{self.NombreCentro}, {self.CodigoCentro} ,{self.Localidad}, {self.Sucursal}, {self.Telefono}"

class Empleado(models.Model):
    NombresEmpleado = models.CharField(max_length=20)
    ApellidosEmpleado = models.CharField(max_length=30, help_text='No debe contener numeros, caracteres 2-30 ')
    DocumentoDPI = models.ForeignKey(DocumentoDPI, on_delete=models.CASCADE)
    DPI = models.CharField(max_length=20, unique=True,help_text='No, debe contenes letras, digitos: 13-15 ')
    FechaNacimientoEmpleado = models.DateField()
    CategoriaEmpleado = models.ForeignKey(CategoriaEmpleado, on_delete=models.CASCADE)
    Tel_Empleado = models.CharField(max_length=8, help_text='No debe contener letras, 8 digitos ')
    Sucursal=models.ForeignKey(CentroEducativo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.NombresEmpleado} {self.ApellidosEmpleado}"

class Usuario(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128, help_text="La contraseña debe tener al menos 8 caracteres y contener al menos un número, una letra mayúscula y una letra minúscula.")
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    Empleado= models.ForeignKey(Empleado,  on_delete=models.CASCADE)
    intentos_fallidos = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super(Usuario, self).save(*args, **kwargs)


from django.db import models

class Matricula(models.Model):
    pagos = models.ForeignKey(Pago, on_delete=models.CASCADE)
    tutor = models.CharField(max_length=100)
    alumno = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_matricula = models.DateField()

    def __str__(self):
        return f"{self.pagos} {self.fecha_matricula}"

class ParametrosSAR(models.Model):
    CAI = models.CharField(max_length=100)
    RTN = models.CharField(max_length=14,help_text='No, debe contenes letras, digitos: 14 ')
    RangoInicial = models.CharField(max_length=8)
    RangoFinal = models.CharField(max_length=8)
    TipoDocumento= models.CharField(max_length=12)
    Establecimiento=models.CharField(max_length=4)
    FechaEmision = models.DateField()
    FechaVencimiento = models.DateField()
    Correlativo=models.CharField(max_length=100)
    Sucursal=models.CharField(max_length=3)
    
    def __str__(self):
        return f"CAI: {self.CAI} RTN: {self.RTN} Rango Inicial: {self.RangoInicial} Rango Final: {self.RangoFinal}, Sucursal :{self.Sucursal}"


class Factura(models.Model):
    numero_factura = models.CharField(unique=True, max_length=21)
    fecha_emision = models.DateField(auto_now_add=True)
    ParametrosSAR = models.ForeignKey(ParametrosSAR, on_delete=models.CASCADE)
    CentroEducativo = models.ForeignKey(CentroEducativo, on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.numero_factura:
            param_sar = self.ParametrosSAR
            rango_inicial = str(param_sar.RangoInicial)
            establecimiento = self.ParametrosSAR.Establecimiento.replace('-', '')  # Elimina los guiones
            sucursal = self.ParametrosSAR.Sucursal.replace('-', '')  # Elimina los guiones
            tipo_documento = self.ParametrosSAR.TipoDocumento.replace('-', '')  # Elimina los guiones
            
            # Encuentra el último número de factura existente
            ultima_factura = Factura.objects.order_by('-numero_factura').first()
            if ultima_factura:
                ultimo_numero = ultima_factura.numero_factura.split('-')[-1]
            else:
                ultimo_numero = rango_inicial
            
            nuevo_numero = str(int(ultimo_numero) + 1).zfill(len(rango_inicial))
            
            self.numero_factura = f"{establecimiento}-{sucursal}-{tipo_documento}-{nuevo_numero}"
            
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Sucursal: {self.CentroEducativo} - Factura N° {self.numero_factura} - Fecha de Emisión: {self.fecha_emision} - {self.ParametrosSAR} - Pago ID: {self.pago.id}"

class Reportes(models.Model):
    TipoReporte = models.ForeignKey(TipoReporte, on_delete=models.CASCADE)
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    DescripcionReporte = models.CharField(max_length=150, help_text='Longitud requerida: caracteres 6-150 ')
    FechaReporte = models.DateField()
    
    
    def __str__(self):
        return self.TipoReporte
    
class Actitud(models.Model):
    Actitud = models.CharField(max_length=15)

    def __str__(self):
        return self.Actitud
    
class ExpedienteEscolar(models.Model):
    Actitud = models.ForeignKey(Actitud, on_delete=models.CASCADE)
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    InstitutoAnterior = models.CharField(max_length=60)
    PromedioAnualAnterior=models.IntegerField()
    Tutor= models.ForeignKey(Tutor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Alumno

class ExpedienteMedico(models.Model):
    Grado = models.ForeignKey(Grado,  on_delete=models.CASCADE)
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    EnfermedadCronica1 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres')
    EnfermedadCronica2 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
    EnfermedadCronica3 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
    MedicamentoUsoDiario1 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
    MedicamentoUsoDiario2 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
    Alergia1 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
    Alergia2 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
    Alergia3 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
  
    
    def __str__(self):
        return f"{self.Alumno}{self.Tutor}"

class ParcialesAcademicos(models.Model):
    ParcialAcademico = models.CharField(max_length=20, help_text='Longitud requerida: 5-20 caracteres ')
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()
    Año= models.DateField()

    def __str__(self):
        return f"{self.ParcialAcademico}, {self.Año}"
    
class NotasAlumnos(models.Model):
    Asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    ParcialAcademico = models.ForeignKey(ParcialesAcademicos, on_delete=models.CASCADE)
    ApellidosAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    NotaAcumulativo= models.DecimalField(max_digits=4, decimal_places=2,  help_text='Maximo valor para Nota de Acumulativo: 2 caracteres, 70.00 ')
    NotaExamen = models.DecimalField(max_digits=4, decimal_places=2,   help_text='Maximo valor para Nota de Examen 2 caracteres, 30.00 ')
    NotaFinal= models.DecimalField(max_digits=4, decimal_places=2,   help_text='Maximo valor para Nota final 2 caracteres, 100.00 ')
    PromedioClase= models.DecimalField(max_digits=4,  decimal_places=2,  help_text='Maximo valor para promedio de clase 2 caracteres, 100.00 ')


    def __str__(self):
        return f"{self.ApellidosAlumno},{self.NotaFinal}"

