import datetime
from imaplib import _Authenticator
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from django.shortcuts import render
from imaplib import _Authenticator
import io

from xhtml2pdf import pisa
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django.views.generic import FormView
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Alumno, CentroEducativo,Empleado,Catedratico, ExpedienteEscolar, Factura, Grado, Municipio, Pago,Tutor,Asignatura,Matricula,Reportes,ExpedienteMedico, HorariosNivelEducativo, NivelEducativo, ParcialesAcademicos, NotasAlumnos, Departamento, ParametrosSAR, Meses, CategoriaEmpleado, DocumentoDPI, TipoPagoHistorico
from .forms import AlumnoForm,EmpleadoForm,CatedraticoForm, ExpedienteEscolarForm,GradoForm, PagoForm, TutorForm,AsignaturaForm,MatriculaForm,ReportesForm,ExpedienteMedicoForm, HorariosForm, NivelesForm, ParcialesForm, NotasForm, DepartamentoForm, MunicipioForm,  MensualidadForm, ParametrosSARForm, CategoriaForm, DocumentoForm, UserCreationForm, UserEditForm, TipoPagoEditForm, TipoPagoActualizarForm

from .models import TipoReporte, TipoSanguineo, Alumno,Empleado,Catedratico,TipoPago, ExpedienteEscolar, Grado, Municipio,Tutor,Asignatura,Matricula,Reportes,ExpedienteMedico, HorariosNivelEducativo, NivelEducativo, ParcialesAcademicos, NotasAlumnos, Departamento, ParametrosSAR, Meses, CategoriaEmpleado, DocumentoDPI
from .forms import TipoReporteForm,TipoSanguineoForm, AlumnoForm,EmpleadoForm,CatedraticoForm, TipoPagoForm,ExpedienteEscolarForm, GradoForm,TutorForm,AsignaturaForm,MatriculaForm,ReportesForm,ExpedienteMedicoForm, HorariosForm, NivelesForm, ParcialesForm, NotasForm, DepartamentoForm, MunicipioForm,  MensualidadForm, ParametrosSARForm, CategoriaForm, DocumentoForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Usuario,Parentesco
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Alumno,Empleado,Catedratico, ExpedienteEscolar, Grado, Municipio,Tutor,Asignatura,Matricula,Reportes,ExpedienteMedico, HorariosNivelEducativo, NivelEducativo, ParcialesAcademicos, NotasAlumnos, Departamento,  ParametrosSAR,  Meses, CategoriaEmpleado, DocumentoDPI,  Seccion, Actitud, CentroEducativo, TutoresAlumnos
from .forms import AlumnoForm,EmpleadoForm,CatedraticoForm, ExpedienteEscolarForm, GradoForm, TutorForm,AsignaturaForm,MatriculaForm,ReportesForm,ExpedienteMedicoForm, HorariosForm, NivelesForm, ParcialesForm, NotasForm, DepartamentoForm, MunicipioForm, MensualidadForm, ParametrosSARForm, CategoriaForm, DocumentoForm, UserCreationForm, UserEditForm,  SeccionForm, ActitudForm, CentroEducativoForm, TutoresAlumnosForm

from .models import TipoReporte, TipoSanguineo, Alumno,Empleado,Catedratico,TipoPago, ExpedienteEscolar, Grado, Municipio,Tutor,Asignatura,Matricula,Reportes,ExpedienteMedico, HorariosNivelEducativo, NivelEducativo, ParcialesAcademicos, NotasAlumnos, Departamento,  ParametrosSAR,  Meses, CategoriaEmpleado, DocumentoDPI,  Seccion, Actitud, CentroEducativo, TutoresAlumnos
from .forms import ParentescoForm, TipoPagoHistoricoForm,TipoReporteForm,TipoSanguineoForm, AlumnoForm,EmpleadoForm,CatedraticoForm, TipoPagoForm,ExpedienteEscolarForm, GradoForm,TutorForm,AsignaturaForm,MatriculaForm,ReportesForm,ExpedienteMedicoForm, HorariosForm, NivelesForm, ParcialesForm, NotasForm, DepartamentoForm, MunicipioForm,  MensualidadForm, ParametrosSARForm, CategoriaForm, DocumentoForm,  SeccionForm, ActitudForm, CentroEducativoForm, TutoresAlumnosForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Usuario
from xhtml2pdf import pisa
from django.contrib import messages

#login

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.db.models import F

from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.db.models import F

from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.db.models import F
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .models import Usuario
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import timedelta
from .models import TipoPago, TipoPagoHistorico
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from django.conf import settings
from django.contrib.auth import authenticate

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.hashers import check_password

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            user = None

        if user is not None and check_password(password, user.password):
            # Las credenciales son correctas
            if user.activo:
                if user.intentos_fallidos >= 3:
                    # El usuario ha excedido el número máximo de intentos fallidos y se bloqueará
                    # Puedes bloquear al usuario aquí o aplicar alguna lógica adicional de seguridad

                    # Bloquear al usuario
                    user.activo = False
                    user.save()

                    messages.error(request, 'Ha excedido el número máximo de intentos fallidos. Su cuenta ha sido bloqueada. Por favor, contacte al administrador.')
                    return redirect('login')  # Redirigir al formulario de inicio de sesión
                else:
                    # Restablecer el número de intentos fallidos a 0 si aún no ha alcanzado el límite
                    user.intentos_fallidos = 0
                    user.save()

                login(request, user)
                if user.rol.nombre == "Administrador":
                    messages.success(request, f'Bienvenido, {user.username} (Administrador)')
                    return redirect('bienvenida_administrador')
                elif user.rol.nombre == "Alumno":
                    messages.success(request, f'Bienvenido, {user.username} (Alumno)')
                    return redirect('bienvenida_alumno')
                elif user.rol.nombre == "Catedrático":
                    messages.success(request, f'Bienvenido, {user.username} (Catedrático)')
                    return redirect('bienvenida_catedratico')
                else:
                    messages.error(request, 'Rol de usuario no válido')
                    return redirect('login')  # Redirigir al formulario de inicio de sesión si el rol no es válido
            else:
                # La cuenta del usuario está bloqueada
                messages.error(request, 'Su cuenta está bloqueada. Por favor, contacte al administrador.')
                return redirect('login')  # Redirigir al formulario de inicio de sesión si la cuenta está bloqueada
        else:
            # Las credenciales son incorrectas
            if user is not None:
                # Incrementar el número de intentos fallidos
                user.intentos_fallidos += 1
                user.save()

            messages.error(request, 'Credenciales incorrectas')
            return redirect('login')  # Redirigir al formulario de inicio de sesión si las credenciales son incorrectas
    
    return render(request, 'base/login.html')


from django.shortcuts import render
from .models import Tutor, TutoresAlumnos


def crear_pago(request):
    tutores_distinct = TutoresAlumnos.objects.order_by('Tutor').values('Tutor').distinct()
    tutor_ids = [tutor['Tutor'] for tutor in tutores_distinct]
    tutores = Tutor.objects.filter(id__in=tutor_ids)

    tutores_choices = [(tutor.id, f"{tutor.NombresTutor} {tutor.ApellidosTutor}") for tutor in tutores]

    if request.method == 'POST':
        form = PagoForm(request.POST)
        form.fields['Tutor'].choices = [('', 'Seleccione un tutor')] + tutores_choices

        if form.is_valid():
            pago = form.save()

            parametros_sar = ParametrosSAR.objects.latest('id')
            centro_educativo = CentroEducativo.objects.latest('id')

            factura = Factura(ParametrosSAR=parametros_sar, CentroEducativo=centro_educativo, pago=pago)
            factura.save()

            return JsonResponse({'pago_id': pago.id})
            # Realizar otras acciones si es necesario
            
    else:
        form = PagoForm()
        form.fields['Tutor'].choices = [('', 'Seleccione un tutor')] + tutores_choices

    context = {
        'form': form,
    }

    return render(request, 'crear_pago.html', context)

def get_monto(request):
    tipo_pago_id = request.GET.get('tipo_pago_id')
    try:
        tipo_pago = TipoPago.objects.get(pk=tipo_pago_id)
        monto = tipo_pago.monto
        return JsonResponse({'monto': str(monto)})  # Convertir el monto a cadena
    except TipoPago.DoesNotExist:
        return JsonResponse({'monto': ''})  

def get_alumnos(request):
    tutor_id = request.GET.get('tutor_id')

    if tutor_id:
        try:
            tutor_id = int(tutor_id)
            alumnos = TutoresAlumnos.objects.filter(Tutor_id=tutor_id).values_list('Alumno_id', flat=True)
            alumnos_relacionados = Alumno.objects.filter(id__in=alumnos)
            
            alumnos_data = []
            for alumno in alumnos_relacionados:
                alumnos_data.append({
                    'id': alumno.id,
                    'NombresAlumno': alumno.NombresAlumno,
                    'ApellidosAlumno': alumno.ApellidosAlumno,
                })

            return JsonResponse(alumnos_data, safe=False)
        except (ValueError, TypeError):
            pass

    return JsonResponse([], safe=False)  # Retornar una lista vacía en caso de error o sin tu


def detalle_factura(request, factura_id):
    
    factura = get_object_or_404(Factura, pk=factura_id)
    return render(request, 'detalle_factura.html', {'factura': factura})


def lista_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'lista_pagos.html', {'pagos': pagos})

from django.conf import settings
import os

def generar_factura(request, pago_id):
    pago = get_object_or_404(Pago, pk=pago_id)
    
    parametros_sar = ParametrosSAR.objects.latest('id')
    centro_educativo = CentroEducativo.objects.latest('id')
   
    factura = Factura( ParametrosSAR=parametros_sar, CentroEducativo=centro_educativo, pago=pago)
    factura.save()

    context = {'factura': factura}
    template = 'generar_factura.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{factura.numero_factura}.pdf"'
    
    with io.BytesIO() as buffer:
        pisa.CreatePDF(render_to_string(template, context), dest=buffer)
        pdf_data = buffer.getvalue()
    
    response.write(pdf_data)
    return response


def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'lista_facturas.html', {'facturas': facturas})
#View Municipios
def load_municipios(request):
    departamento_id = request.GET.get('Departamento')
    municipios = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombreMunicipio')
    return render(request, 'Municipios/municipios_dropdown_list.html', {'municipios':municipios})




#View Municipios
def load_municipios(request):
    departamento_id = request.GET.get('Departamento')
    municipios = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombreMunicipio')
    return render(request, 'Municipios/municipios_dropdown_list.html', {'municipios':municipios})



 #inicios segun rol   
from django.views.generic import TemplateView

class BienvenidaAdministradorView(TemplateView):
    template_name = 'pantallas/administrador.html'

class BienvenidaAlumnoView(TemplateView):
    template_name = 'pantallas/alumno.html'

class BienvenidaCatedraticoView(TemplateView):
    template_name = 'pantallas/catedratico.html'
        

from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class InicioPantalla(LoginRequiredMixin, TemplateView):
    template_name = 'inicio/index.html'
    login_url = 'base/login'

    def get_success_url(self):
        # Agrega aquí tu lógica personalizada para determinar la URL de éxito
        # Puedes utilizar self.request.user para acceder al usuario actual

        # Ejemplo: redirigir a una URL diferente según el rol del usuario
        if self.request.user.usuario.rol.nombre == 'Administrador':
            return reverse_lazy('bienvenida_administrador')
        elif self.request.user.usuario.rol.nombre == 'Alumno':
            return reverse_lazy('bienvenida_alumno')
        elif self.request.user.usuario.rol.nombre == 'Catedratico':
            return reverse_lazy('bienvenida_catedratico')
        else:
            return reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega aquí el contexto adicional que desees pasar a la plantilla
        # Puedes utilizar self.request.user para acceder al usuario actual
        return context



from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Usuario

#usuarios

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'Usuario/usuario_detalle.html'

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'Usuario/usuario_listar.html'
    context_object_name = 'usuarios'



class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UserCreationForm
    template_name = 'Usuario/usuario_crear.html'
    success_url = reverse_lazy('usuario_listar')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UserEditForm
    template_name = 'Usuario/usuario_editar.html'
    success_url = reverse_lazy('usuario_listar')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'Usuario/usuario_eliminar.html'
    success_url = reverse_lazy('usuario_listar')


class AlumnoListView(ListView):
    model = Alumno
    template_name = 'Alumno/alumno_listar.html'
    context_object_name = 'alumnos'
    login_url='base/login'

class AlumnoCreateView(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'Alumno/alumno_crear.html'
    success_url = reverse_lazy('alumno_listar')


class AlumnoDetailView(DetailView):
    model = Alumno
    template_name = 'Alumno/alumno_detalle.html'

class AlumnoUpdateView(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'Alumno/alumno_editar.html'
    success_url = reverse_lazy('alumno_listar')

class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'Alumno/alumno_eliminar.html'
    success_url = reverse_lazy('alumno_listar')

#views de Empleado



class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'Empleado/Empleado_listar.html'
    context_object_name = 'empleados'

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'Empleado/empleado_crear.html'
    success_url = reverse_lazy('listar_empleados')

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'Empleado/empleado_detalle.html'

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'Empleado/empleado_editar.html'
    success_url = reverse_lazy('listar_empleados')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'Empleado/eliminar.html'
    success_url = reverse_lazy('listar_empleados')

#views catedratico



class CatedraticoListView(ListView):
    model = Catedratico
    template_name = 'catedratico/catedratico_listar.html'
    context_object_name = 'catedraticos'

class CatedraticoCreateView(CreateView):
    model = Catedratico
    form_class = CatedraticoForm
    template_name = 'catedratico/catedratico_crear.html'
    success_url = reverse_lazy('listar_catedraticos')

    def agregar_catedratico(request):
        if request.method == 'POST':
            form = CatedraticoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Catedrático agregado exitosamente.')
                return redirect('listar_catedraticos')
            else:
                messages.error(request, 'Error: Algunos campos están incorrectos.')
        else:
            form = CatedraticoForm()
        
        context = {
            'form': form,
        }
        return render(request, 'Catedratico/catedratico_crear.html', context)


class CatedraticoDetailView(DetailView):
    model = Catedratico
    template_name = 'Catedratico/catedratico_detalle.html'

class CatedraticoUpdateView(UpdateView):
    model = Catedratico
    form_class = CatedraticoForm
    template_name = 'catedratico/catedratico_editar.html'
    success_url = reverse_lazy('listar_catedraticos')

class CatedraticoDeleteView(DeleteView):
    model = Catedratico
    template_name = 'catedratico/catedratico_eliminar.html'
    success_url = reverse_lazy('listar_catedraticos')

#views de Tutor

class TutorListView(ListView):
    model = Tutor
    template_name = 'Tutor/tutor_listar.html'
    context_object_name = 'tutores'
    login_url = 'base/login'

class TutorCreateView(CreateView):
    model = Tutor
    form_class = TutorForm
    template_name = 'Tutor/tutor_crear.html'
    success_url = reverse_lazy('tutor_listar')

class TutorDetailView(DetailView):
    model = Tutor
    template_name = 'Tutor/tutor_detalle.html'

class TutorUpdateView(UpdateView):
    model = Tutor
    form_class = TutorForm
    template_name = 'Tutor/tutor_editar.html'
    success_url = reverse_lazy('tutor_listar')

class TutorDeleteView(DeleteView):
    model = Tutor
    template_name = 'Tutor/tutor_eliminar.html'
    success_url = reverse_lazy('tutor_listar')

#views Asignatura

class AsignaturaListView(ListView):
    model = Asignatura
    template_name = 'Asignatura/asignatura_listar.html'
    context_object_name = 'asignaturas'

class AsignaturaCreateView(CreateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'Asignatura/asignatura_crear.html'
    success_url = reverse_lazy('asignatura_listar')

def agregar_asignatura(request):
    if request.method == 'POST':
        # Lógica para guardar la asignatura
        messages.success(request, 'Asignatura guardada exitosamente.')
        return redirect('asignatura_listar')
    
    form = AsignaturaForm()
    return render(request, 'Asignatura/asignatura_crear.html', {'form': form})

class AsignaturaDetailView(DetailView):
    model = Asignatura
    template_name = 'Asignatura/asignatura_detalle.html'

class AsignaturaUpdateView(UpdateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'Asignatura/asignatura_editar.html'
    success_url = reverse_lazy('asignatura_listar')

class AsignaturaDeleteView(DeleteView):
    model = Asignatura
    template_name = 'Asignatura/asignatura_eliminar.html'
    success_url = reverse_lazy('asignatura_listar')

#views Matricula

class MatriculaListView(ListView):
    model = Matricula
    template_name = 'Matricula/matricula_listar.html'
    context_object_name = 'matriculas'

class MatriculaCreateView(CreateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'Matricula/matricula_crear.html'
    success_url = reverse_lazy('matricula_listar')

class MatriculaDetailView(DetailView):
    model = Matricula
    template_name = 'Matricula/matricula_detalle.html'

class MatriculaUpdateView(UpdateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'Matricula/matricula_editar.html'
    success_url = reverse_lazy('matricula_listar')

class MatriculaDeleteView(DeleteView):
    model = Matricula
    template_name = 'Matricula/matricula_eliminar.html'
    success_url = reverse_lazy('matricula_listar')

#views Reportes

class ReportesListView(ListView):
    model = Reportes
    template_name = 'Reporte/reporte_listar.html'
    context_object_name = 'reportes'

class ReportesCreateView(CreateView):
    model = Reportes
    form_class = ReportesForm
    template_name = 'Reporte/reporte_crear.html'
    success_url = reverse_lazy('reporte_listar')

class ReportesDetailView(DetailView):
    model = Reportes
    template_name = 'Reporte/reporte_detalle.html'

class ReportesUpdateView(UpdateView):
    model = Reportes
    form_class = ReportesForm
    template_name = 'Reporte/reporte_editar.html'
    success_url = reverse_lazy('reporte_listar')

class ReportesDeleteView(DeleteView):
    model = Reportes
    template_name = 'Reporte/reporte_eliminar.html'
    success_url = reverse_lazy('reporte_listar')

    
#views Expediente Médicos

class ExpedienteMedicoListView(ListView):
    model = ExpedienteMedico
    template_name = 'ExpedienteMedico/expedientemedico_listar.html'
    context_object_name = 'expedientemedicos'

class ExpedienteMedicoCreateView(CreateView):
    model = ExpedienteMedico
    form_class = ExpedienteMedicoForm
    template_name = 'ExpedienteMedico/expedientemedico_crear.html'
    success_url = reverse_lazy('expedientemedico_listar')

class ExpedienteMedicoDetailView(DetailView):
    model = ExpedienteMedico
    template_name = 'ExpedienteMedico/expedientemedico_detalle.html'

class ExpedienteMedicoUpdateView(UpdateView):
    model = ExpedienteMedico
    form_class = ExpedienteMedicoForm
    template_name = 'ExpedienteMedico/expedientemedico_editar.html'
    success_url = reverse_lazy('expedientemedico_listar')

class ExpedienteMedicoDeleteView(DeleteView):
    model = ExpedienteMedico
    template_name = 'ExpedienteMedico/expedientemedico_eliminar.html'
    success_url = reverse_lazy('expedientemedico_listar')

# views Horarios
class HorariosListView(ListView):
    model = HorariosNivelEducativo
    template_name = 'Horarios/horarios_listar.html'
    context_object_name = 'horarios'

class HorariosCreateView(CreateView):
    model = HorariosNivelEducativo
    form_class =    HorariosForm
    template_name = 'Horarios/horarios_crear.html'
    success_url = reverse_lazy('horarios_listar')

class HorariosUpdateView(UpdateView):
    model = HorariosNivelEducativo
    form_class = HorariosForm
    template_name = 'Horarios/horarios_editar.html'
    success_url = reverse_lazy('horarios_listar')

class HorariosDeleteView(DeleteView):
    model = HorariosNivelEducativo
    template_name = 'Horarios/horarios_eliminar.html'
    success_url = reverse_lazy('horarios_listar')

class HorariosDetailView(DetailView):
    model = HorariosNivelEducativo
    template_name = 'Horarios/horarios_detalle.html'
#views niveles

class NivelesListView(ListView):
    model = NivelEducativo
    template_name = 'Niveles/niveles_listar.html'
    context_object_name = 'niveles'

class NivelesCreateView(CreateView):
    model = NivelEducativo
    form_class = NivelesForm
    template_name = 'Niveles/niveles_crear.html'
    success_url = reverse_lazy('niveles_listar')

class NivelesUpdateView(UpdateView):
    model = NivelEducativo
    form_class = NivelesForm
    template_name = 'Niveles/niveles_editar.html'
    success_url = reverse_lazy('niveles_listar')

class NivelesDeleteView(DeleteView):
    model = NivelEducativo
    template_name = 'Niveles/niveles_eliminar.html'
    success_url = reverse_lazy('niveles_listar')

class NivelesDetailView(DetailView):
    model = NivelEducativo
    template_name = 'Niveles/niveles_detalle.html'

#vies parciales

class ParcialesListView(ListView):
    model = ParcialesAcademicos
    template_name = 'Parciales/parciales_listar.html'
    context_object_name = 'parciales'

class ParcialesCreateView(CreateView):
    model = ParcialesAcademicos
    form_class = ParcialesForm
    template_name = 'Parciales/parciales_crear.html'
    success_url = reverse_lazy('parciales_listar')

class ParcialesUpdateView(UpdateView):
    model = ParcialesAcademicos
    form_class = ParcialesForm
    template_name = 'Parciales/parciales_editar.html'
    success_url = reverse_lazy('parciales_listar')

class ParcialesDeleteView(DeleteView):
    model = ParcialesAcademicos
    template_name = 'Parciales/parciales_eliminar.html'
    success_url = reverse_lazy('parciales_listar')

class ParcialesDetailView(DetailView):
    model = ParcialesAcademicos
    template_name = 'Parciales/parciales_detalle.html'

#Views Notas
class NotasListView(ListView):
    model = NotasAlumnos
    template_name = 'Notas/notas_listar.html'
    context_object_name = 'notas'

class NotasCreateView(CreateView):
    model = NotasAlumnos
    form_class = NotasForm
    template_name = 'Notas/notas_crear.html'
    success_url = reverse_lazy('notas_listar')

class NotasUpdateView(UpdateView):
    model = NotasAlumnos
    form_class = NotasForm
    template_name = 'Notas/notas_editar.html'
    success_url = reverse_lazy('notas_listar')

class NotasDeleteView(DeleteView):
    model = NotasAlumnos
    template_name = 'Notas/notas_eliminar.html'
    success_url = reverse_lazy('notas_listar')

class NotasDetailView(DetailView):
    model = NotasAlumnos
    template_name = 'Notas/notas_detalle.html'

#grados

class GradoListView(ListView):
    model = Grado
    template_name = 'Grado/grado_listar.html'
    context_object_name = 'grados'
    login_url = 'base/login'

class GradoCreateView(CreateView):
    model = Grado
    form_class = GradoForm
    template_name = 'Grado/grado_crear.html'
    success_url = reverse_lazy('grado_listar')

class GradoDetailView(DetailView):
    model = Grado
    template_name = 'Grado/grado_detalle.html'

class GradoUpdateView(UpdateView):
    model = Grado
    form_class = GradoForm
    template_name = 'Grado/grado_editar.html'
    success_url = reverse_lazy('grado_listar')

class GradoDeleteView(DeleteView):
    model = Grado
    template_name = 'Grado/grado_eliminar.html'
    success_url = reverse_lazy('grado_listar')

#expedientes escolares

class ExpedienteEscolarListView(ListView):
    model = ExpedienteEscolar
    template_name = 'ExpedienteEscolar/expedienteescolar_listar.html'
    context_object_name = 'expedienteescolares'

class ExpedienteEscolarCreateView(CreateView):
    model = ExpedienteEscolar
    form_class = ExpedienteEscolarForm
    template_name = 'ExpedienteEscolar/expedienteescolar_crear.html'
    success_url = reverse_lazy('expedienteescolar_listar')

class ExpedienteEscolarDetailView(DetailView):
    model = ExpedienteEscolar
    template_name = 'ExpedienteEscolar/expedienteescolar_detalle.html'

class ExpedienteEscolarUpdateView(UpdateView):
    model = ExpedienteEscolar
    form_class = ExpedienteEscolarForm
    template_name = 'ExpedienteEscolar/expedienteescolar_editar.html'
    success_url = reverse_lazy('expedienteescolar_listar')

class ExpedienteEscolarDeleteView(DeleteView):
    model = ExpedienteEscolar
    template_name = 'ExpedienteEscolar/expedienteescolar_eliminar.html'
    success_url = reverse_lazy('expedienteescolar_listar')


class DepaListView(ListView):
    model = Departamento
    template_name = 'Departamento/departamento_listar.html'
    context_object_name = 'departamentos'
    
class DepaCreateView(CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'Departamento/departamento_crear.html'
    success_url = reverse_lazy('departamento_listar')
class DepaUpdateView(UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'Departamento/departamento_editar.html'
    success_url = reverse_lazy('departamento_listar')

class DepaDeleteView(DeleteView):
    model = Departamento
    template_name = 'Departamento/departamento_eliminar.html'
    success_url = reverse_lazy('departamento_listar')

class DepaDetailView(DetailView):
    model = Departamento
    template_name = 'Departamento/departamento_detalle.html'

class MuniListView(ListView):
    model = Municipio
    template_name = 'Municipios/municipio_listar.html'
    context_object_name = 'municipios'
    
class MuniCreateView(CreateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'Municipios/municipio_crear.html'
    success_url = reverse_lazy('municipio_listar')
class MuniUpdateView(UpdateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'Municipios/municipio_editar.html'
    success_url = reverse_lazy('municipio_listar')
class MuniDeleteView(DeleteView):
    model = Municipio
    template_name = 'Municipios/municipio_eliminar.html'
    success_url = reverse_lazy('municipio_listar')


class MuniDetailView(DetailView):
    model = Municipio
    template_name = 'Municipios/municipio_detalle.html'


class MensualidadListView(ListView):
    model = Meses
    template_name = 'Meses/mensualidad_listar.html'
    context_object_name = 'mensualidades'  
class MensualidadCreateView(CreateView):
    model = Meses
    form_class = MensualidadForm
    template_name = 'Meses/mensualidad_crear.html'
    success_url = reverse_lazy('mensualidad_listar')
class MensualidadUpdateView(UpdateView):
    model = Meses
    form_class = MensualidadForm
    template_name = 'Meses/mensualidad_editar.html'
    success_url = reverse_lazy('mensualidad_listar')
class MensualidadDeleteView(DeleteView):
    model = Meses
    template_name = 'Meses/mensualidad_eliminar.html'
    success_url = reverse_lazy('mensualidad_listar')

class MensualidadDetailView(DetailView):
    model = Meses
    template_name = 'Meses/mensualidad_detalle.html'


class ParametrosListView(ListView):
    model = ParametrosSAR
    template_name = 'Parametros/parametros_listar.html'
    context_object_name = 'parametros'

class ParametrosCreateView(CreateView):
    model = ParametrosSAR
    form_class = ParametrosSARForm
    template_name = 'Parametros/parametros_crear.html'
    success_url = reverse_lazy('parametros_listar')

class ParametrosDetailView(DetailView):
    model = ParametrosSAR
    template_name = 'Parametros/parametros_detalle.html'

class ParametrosUpdateView(UpdateView):
    model = ParametrosSAR
    form_class = ParametrosSARForm
    template_name = 'Parametros/parametros_editar.html'
    success_url = reverse_lazy('parametros_listar')

class ParametrosDeleteView(DeleteView):
    model = ParametrosSAR
    template_name = 'Parametros/parametros_eliminar.html'
    success_url = reverse_lazy('parametros_listar')

#Views Categoria de empleados
class CateListView(ListView):
    model = CategoriaEmpleado
    template_name = 'Categorias/categoria_listar.html'
    context_object_name = 'categorias'  
class CateCreateView(CreateView):
    model = CategoriaEmpleado
    form_class = CategoriaForm
    template_name = 'Categorias/categoria_crear.html'
    success_url = reverse_lazy('categoria_listar')
class CateUpdateView(UpdateView):
    model = CategoriaEmpleado
    form_class = CategoriaForm
    template_name = 'Categorias/categoria_editar.html'
    success_url = reverse_lazy('categoria_listar')
class CateDeleteView(DeleteView):
    model = CategoriaEmpleado
    template_name = 'Categorias/categoria_eliminar.html'
    success_url = reverse_lazy('categoria_listar')

class CateDetailView(DetailView):
    model = CategoriaEmpleado
    template_name = 'Categorias/categoria_detalle.html'

#Views documentos

class DocListView(ListView):
    model = DocumentoDPI
    template_name = 'Documentos/documento_listar.html'
    context_object_name = 'documentos'  
class DocCreateView(CreateView):
    model = DocumentoDPI
    form_class = DocumentoForm
    template_name = 'Documentos/documento_crear.html'
    success_url = reverse_lazy('documento_listar')
class DocUpdateView(UpdateView):
    model = DocumentoDPI
    form_class = DocumentoForm
    template_name = 'Documentos/documento_editar.html'
    success_url = reverse_lazy('documento_listar')
class DocDeleteView(DeleteView):
    model = DocumentoDPI
    template_name = 'Documentos/documento_eliminar.html'
    success_url = reverse_lazy('documento_listar')

class DocDetailView(DetailView):
    model = DocumentoDPI
    template_name = 'Documentos/documento_detalle.html'

#Views TiposPagos

class TipoPagoListView(ListView):
    model = TipoPago
    template_name = 'TipoPago/tipopago_listar.html'
    context_object_name = 'tipospago'


class TipoPagoCreateView(CreateView):
    model = TipoPago
    form_class = TipoPagoForm
    template_name = 'TipoPago/tipopago_crear.html'
    success_url = reverse_lazy('tipopago_listar')

    def form_valid(self, form):
        response = super().form_valid(form)
        tipo_pago = form.instance

        TipoPagoHistorico.objects.create(
            tipo_pago=tipo_pago,
            fecha_inicio=timezone.now().date(),
            fecha_fin=None,  # Deja la fecha final vacía
            monto=tipo_pago.monto,  # Utiliza el monto proporcionado en el formulario
            Impuesto=tipo_pago.Impuesto
        )

        return response


class TipoPagoActualizarView(UpdateView):
    model = TipoPago
    form_class = TipoPagoActualizarForm
    template_name = 'TipoPagoHistorico/actualizarMonto.html'
    success_url = reverse_lazy('tipopago_listar')

    def form_valid(self, form):
        response = super().form_valid(form)

        tipo_pago = form.instance

        registro_anterior = TipoPagoHistorico.objects.filter(tipo_pago=tipo_pago).order_by('-fecha_inicio').first()

        if registro_anterior:
            registro_anterior.fecha_fin = timezone.now().date() - timedelta(days=1)
            registro_anterior.save()

        TipoPagoHistorico.objects.create(
            tipo_pago=tipo_pago,
            fecha_inicio=timezone.now().date(),
            fecha_fin=None,  # Deja la fecha final vacía
            monto=form.cleaned_data['monto'],  # Utiliza el monto del formulario
            Impuesto=tipo_pago.Impuesto
        )

        return response











class TipoPagoUpdateView(UpdateView):
    model = TipoPago
    form_class = TipoPagoEditForm
    template_name = 'TipoPago/tipopago_editar.html'
    success_url = reverse_lazy('tipopago_listar')

class TipoPagoDeleteView(DeleteView):
    model = TipoPago
    template_name = 'TipoPago/tipopago_eliminar.html'
    success_url = reverse_lazy('tipopago_listar')

class TipoPagoDetailView(DetailView):
    model = TipoPago
    template_name = 'TipoPago/tipopago_detalle.html'

#Views TiposReportes

class TipoReporteListView(ListView):
    model = TipoReporte
    template_name = 'TipoReporte/tiporeporte_listar.html'
    context_object_name = 'tiposreportes'

class TipoReporteCreateView(CreateView):
    model = TipoReporte
    form_class = TipoReporteForm
    template_name = 'TipoReporte/tiporeporte_crear.html'
    success_url = reverse_lazy('tiporeporte_listar')

class TipoReporteUpdateView(UpdateView):
    model = TipoReporte
    form_class = TipoReporteForm
    template_name = 'TipoReporte/tiporeporte_editar.html'
    success_url = reverse_lazy('tiporeporte_listar')

class TipoReporteDeleteView(DeleteView):
    model = TipoReporte
    template_name = 'TipoReporte/tiporeporte_eliminar.html'
    success_url = reverse_lazy('tiporeporte_listar')

class TipoReporteDetailView(DetailView):
    model = TipoReporte
    template_name = 'TipoReporte/tiporeporte_detalle.html'

#Views TiposReportes

class TipoSanguineoListView(ListView):
    model = TipoSanguineo
    template_name = 'TipoSanguineo/tiposanguineo_listar.html'
    context_object_name = 'tiposanguineos'

class TipoSanguineoCreateView(CreateView):
    model = TipoSanguineo
    form_class = TipoSanguineoForm
    template_name = 'TipoSanguineo/tiposanguineo_crear.html'
    success_url = reverse_lazy('tiposanguineo_listar')

class TipoSanguineoUpdateView(UpdateView):
    model = TipoSanguineo
    form_class = TipoSanguineoForm
    template_name = 'TipoSanguineo/tiposanguineo_editar.html'
    success_url = reverse_lazy('tiposanguineo_listar')

class TipoSanguineoDeleteView(DeleteView):
    model = TipoSanguineo
    template_name = 'TipoSanguineo/tiposanguineo_eliminar.html'
    success_url = reverse_lazy('tiposanguineo_listar')


class TipoSanguineoDetailView(DetailView):
    model = TipoSanguineo
    template_name = 'TipoSanguineo/tiposanguineo_detalle.html'





class SeccionListView(ListView):
    model = Seccion
    template_name = 'Seccion/seccion_listar.html'
    context_object_name = 'secciones'

class SeccionCreateView(CreateView):
    model = Seccion
    form_class = SeccionForm
    template_name = 'Seccion/seccion_crear.html'
    success_url = reverse_lazy('seccion_listar')

class SeccionDetailView(DetailView):
    model = Seccion
    template_name = 'Seccion/seccion_detalle.html'

class SeccionUpdateView(UpdateView):
    model = Seccion
    form_class = SeccionForm
    template_name = 'Seccion/seccion_editar.html'
    success_url = reverse_lazy('seccion_listar')

class SeccionDeleteView(DeleteView):
    model = Seccion
    template_name = 'Seccion/seccion_eliminar.html'
    success_url = reverse_lazy('seccion_listar')

#views Actitud

class ActitudListView(ListView):
    model = Actitud
    template_name = 'Actitud/actitud_listar.html'
    context_object_name = 'actitudes'

class ActitudCreateView(CreateView):
    model = Actitud
    form_class = ActitudForm
    template_name = 'Actitud/actitud_crear.html'
    success_url = reverse_lazy('actitud_listar')

class ActitudDetailView(DetailView):
    model = Actitud
    template_name = 'Actitud/actitud_detalle.html'

class ActitudUpdateView(UpdateView):
    model = Actitud
    form_class = ActitudForm
    template_name = 'Actitud/actitud_editar.html'
    success_url = reverse_lazy('actitud_listar')

class ActitudDeleteView(DeleteView):
    model = Actitud
    template_name = 'Actitud/actitud_eliminar.html'
    success_url = reverse_lazy('actitud_listar')

#views Centro Educativo

class CentroEducativoListView(ListView):
    model = CentroEducativo
    template_name = 'CentroEducativo/centroeducativo_listar.html'
    context_object_name = 'centroeducativos'

class CentroEducativoCreateView(CreateView):
    model = CentroEducativo
    form_class = CentroEducativoForm
    template_name = 'CentroEducativo/centroeducativo_crear.html'
    success_url = reverse_lazy('centroeducativo_listar')

class CentroEducativoDetailView(DetailView):
    model = CentroEducativo
    template_name = 'CentroEducativo/centroeducativo_detalle.html'

class CentroEducativoUpdateView(UpdateView):
    model = CentroEducativo
    form_class = CentroEducativoForm
    template_name = 'CentroEducativo/centroeducativo_editar.html'
    success_url = reverse_lazy('centroeducativo_listar')

class CentroEducativoDeleteView(DeleteView):
    model = CentroEducativo
    template_name = 'CentroEducativo/centroeducativo_eliminar.html'
    success_url = reverse_lazy('centroeducativo_listar')

#views TutoresAlumno

class TutoresAlumnosListView(ListView):
    model = TutoresAlumnos
    template_name = 'TutoresAlumno/tutoresalumno_listar.html'
    context_object_name = 'tutoresalumnos'

class TutoresAlumnosCreateView(CreateView):
    model = TutoresAlumnos
    form_class = TutoresAlumnosForm
    template_name = 'TutoresAlumno/tutoresalumno_crear.html'
    success_url = reverse_lazy('tutoresalumno_listar')

class TutoresAlumnosDetailView(DetailView):
    model = TutoresAlumnos
    template_name = 'TutoresAlumno/tutoresalumno_detalle.html'

class TutoresAlumnosUpdateView(UpdateView):
    model = TutoresAlumnos
    form_class = TutoresAlumnosForm
    template_name = 'TutoresAlumno/tutoresalumno_editar.html'
    success_url = reverse_lazy('tutoresalumno_listar')

class TutoresAlumnosDeleteView(DeleteView):
    model = TutoresAlumnos
    template_name = 'TutoresAlumno/tutoresalumno_eliminar.html'
    success_url = reverse_lazy('tutoresalumno_listar')



#TipoPago Historicos

class TipoPagoHistoricoListView(ListView):
    model = TipoPagoHistorico
    template_name = 'TipoPagoHistorico/listar.html'
    context_object_name = 'tipos_pago_historicos'

class TipoPagoHistoricoCreateView(CreateView):
    model = TipoPagoHistorico
    form_class = TipoPagoHistoricoForm
    template_name = 'TipoPagoHistorico/agregar.html'
    success_url = reverse_lazy('tipo_pago_historico_listar')

class TipoPagoHistoricoUpdateView(UpdateView):
    model = TipoPagoHistorico
    form_class = TipoPagoEditForm
    template_name = 'TipoPagoHistorico/editar.html'
    success_url = reverse_lazy('tipo_pago_historico_listar')

       

class TipoPagoHistoricoDeleteView(DeleteView):
    model = TipoPagoHistorico
    template_name = 'TipoPagoHistorico/eliminar.html'
    success_url = reverse_lazy('tipo_pago_historico_listar')

class TipoPagoHistoricoDetailView(DetailView):
    model = TipoPagoHistorico
    template_name = 'TipoPagoHistorico/detalle.html'

#Parentezco



class ParentescoListView(ListView):
    model = Parentesco
    template_name = 'Parentesco/parentesco_lista.html'  # Replace with your template path
    context_object_name = 'parentescos'  # Name used in the template context




import re
class ParentescoCreateView(CreateView):
    template_name = 'Parentesco/parentesco_crear.html'

    def get(self, request):
        form = ParentescoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ParentescoForm(request.POST)
        if form.is_valid():
            parentesco = form.cleaned_data['Parentesco']

            # Custom validation: Only letters are allowed
            if not parentesco.isalpha():
                form.add_error('Parentesco', 'Solo se permiten letras en este campo.')

            # Custom validation: No whitespaces allowed
            if ' ' in parentesco:
                form.add_error('Parentesco', 'No se permiten espacios en blanco.')

            # Custom validation: No three identical consecutive letters
            if re.search(r'(.)\1\1', parentesco):
                form.add_error('Parentesco', 'No se permiten tres letras idénticas consecutivas.')

            if form.errors:
                return render(request, self.template_name, {'form': form})

            Parentesco.objects.create(Parentesco=parentesco)
            return redirect(reverse_lazy('parentesco_list'))

        return render(request, self.template_name, {'form': form})