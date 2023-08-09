"""
URL configuration for CentroEducativo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import TipoPagoActualizarView
from .views import TipoReporteCreateView, TipoReporteDeleteView, TipoReporteListView, TipoReporteUpdateView, TipoReporteDetailView, TipoSanguineoCreateView, TipoSanguineoDeleteView, TipoSanguineoListView, TipoSanguineoUpdateView, TipoSanguineoDetailView, TipoPagoCreateView, TipoPagoDeleteView, TipoPagoListView, TipoPagoUpdateView, TipoPagoDetailView, ExpedienteEscolarCreateView, ExpedienteEscolarDeleteView, ExpedienteEscolarDetailView, ExpedienteEscolarListView, ExpedienteEscolarUpdateView, GradoCreateView, GradoDeleteView, GradoDetailView, GradoListView, GradoUpdateView, HorariosDetailView, NivelesDetailView, NotasDetailView, ParcialesDetailView, UsuarioDetailView, AlumnoListView, AlumnoCreateView, AlumnoDetailView, AlumnoUpdateView, AlumnoDeleteView, BienvenidaAdministradorView, BienvenidaAlumnoView, BienvenidaCatedraticoView, CatedraticoCreateView,InicioPantalla, CatedraticoDeleteView, CatedraticoListView, CatedraticoDetailView, CatedraticoUpdateView,EmpleadoListView, EmpleadoCreateView, EmpleadoDetailView, EmpleadoUpdateView, EmpleadoDeleteView, UsuarioCreateView, UsuarioDeleteView, UsuarioListView, UsuarioUpdateView, TutorListView, TutorCreateView, TutorDetailView, TutorUpdateView, TutorDeleteView, AsignaturaForm, AsignaturaListView, AsignaturaCreateView, AsignaturaDetailView, AsignaturaUpdateView, AsignaturaDeleteView, MatriculaListView, MatriculaCreateView, MatriculaDetailView, MatriculaUpdateView, MatriculaDeleteView, ReportesListView, ReportesCreateView, ReportesDetailView, ReportesUpdateView, ReportesDeleteView, ExpedienteMedicoListView, ExpedienteMedicoCreateView, ExpedienteMedicoDetailView, ExpedienteMedicoUpdateView, ExpedienteMedicoDeleteView, load_municipios, login_view, HorariosCreateView, HorariosDeleteView, HorariosListView, HorariosUpdateView, NivelesCreateView, NivelesListView, NivelesDeleteView, NivelesUpdateView, ParcialesListView, ParcialesCreateView, ParcialesDeleteView, ParcialesUpdateView, NotasCreateView, NotasDeleteView, NotasListView, NotasUpdateView, DepaCreateView,DepaDeleteView, DepaUpdateView,DepaListView, DepaDetailView, MuniCreateView, MuniDeleteView, MuniListView, MuniUpdateView, MuniDetailView,  MensualidadCreateView, MensualidadDeleteView, MensualidadListView, MensualidadUpdateView, MensualidadDetailView, ParametrosCreateView, ParametrosDeleteView,ParametrosDetailView, ParametrosUpdateView, ParametrosListView, DocCreateView, DocDeleteView, DocUpdateView, DocListView, DocDetailView, CateCreateView, CateDeleteView, CateListView, CateUpdateView, CateDetailView,    SeccionListView, SeccionCreateView, SeccionDetailView, SeccionUpdateView, SeccionDeleteView, ActitudListView, ActitudCreateView, ActitudDetailView, ActitudUpdateView, ActitudDeleteView, CentroEducativoListView, CentroEducativoCreateView, CentroEducativoDetailView, CentroEducativoUpdateView, CentroEducativoDeleteView, TutoresAlumnosListView, TutoresAlumnosCreateView, TutoresAlumnosDetailView, TutoresAlumnosUpdateView, TutoresAlumnosDeleteView
from .views import TipoReporteCreateView, TipoReporteDeleteView, TipoReporteListView, TipoReporteUpdateView, TipoSanguineoCreateView, TipoSanguineoDeleteView, TipoSanguineoListView, TipoSanguineoUpdateView, TipoPagoCreateView, TipoPagoDeleteView, TipoPagoListView, TipoPagoUpdateView, ExpedienteEscolarCreateView, ExpedienteEscolarDeleteView, ExpedienteEscolarDetailView, ExpedienteEscolarListView, ExpedienteEscolarUpdateView, GradoCreateView, GradoDeleteView, GradoDetailView, GradoListView, GradoUpdateView, HorariosDetailView, NivelesDetailView, NotasDetailView, ParcialesDetailView, UsuarioDetailView, AlumnoListView, AlumnoCreateView, AlumnoDetailView, AlumnoUpdateView, AlumnoDeleteView, BienvenidaAdministradorView, BienvenidaAlumnoView, BienvenidaCatedraticoView, CatedraticoCreateView,InicioPantalla, CatedraticoDeleteView, CatedraticoListView, CatedraticoDetailView, CatedraticoUpdateView,EmpleadoListView, EmpleadoCreateView, EmpleadoDetailView, EmpleadoUpdateView, EmpleadoDeleteView, UsuarioCreateView, UsuarioDeleteView, UsuarioListView, UsuarioUpdateView, TutorListView, TutorCreateView, TutorDetailView, TutorUpdateView, TutorDeleteView, AsignaturaForm, AsignaturaListView, AsignaturaCreateView, AsignaturaDetailView, AsignaturaUpdateView, AsignaturaDeleteView, MatriculaListView, MatriculaCreateView, MatriculaDetailView, MatriculaUpdateView, MatriculaDeleteView, ReportesListView, ReportesCreateView, ReportesDetailView, ReportesUpdateView, ReportesDeleteView, ExpedienteMedicoListView, ExpedienteMedicoCreateView, ExpedienteMedicoDetailView, ExpedienteMedicoUpdateView, ExpedienteMedicoDeleteView, crear_pago, detalle_factura, generar_factura, lista_facturas, lista_pagos, load_municipios, login_view, HorariosCreateView, HorariosDeleteView, HorariosListView, HorariosUpdateView, NivelesCreateView, NivelesListView, NivelesDeleteView, NivelesUpdateView, ParcialesListView, ParcialesCreateView, ParcialesDeleteView, ParcialesUpdateView, NotasCreateView, NotasDeleteView, NotasListView, NotasUpdateView, DepaCreateView,DepaDeleteView, DepaUpdateView,DepaListView, MuniCreateView, MuniDeleteView, MuniListView, MuniUpdateView, MensualidadCreateView, MensualidadDeleteView, MensualidadListView, MensualidadUpdateView, ParametrosCreateView, ParametrosDeleteView,ParametrosDetailView, ParametrosUpdateView, ParametrosListView, DocCreateView, DocDeleteView, DocUpdateView, DocListView, CateCreateView, CateDeleteView, CateListView, CateUpdateView, SeccionListView, SeccionCreateView, SeccionDetailView, SeccionUpdateView, SeccionDeleteView, ActitudListView, ActitudCreateView, ActitudDetailView, ActitudUpdateView, ActitudDeleteView, CentroEducativoListView, CentroEducativoCreateView, CentroEducativoDetailView, CentroEducativoUpdateView, CentroEducativoDeleteView, TutoresAlumnosListView, TutoresAlumnosCreateView, TutoresAlumnosDetailView, TutoresAlumnosUpdateView, TutoresAlumnosDeleteView
urlpatterns = [
    path('', login_view, name='login'),
    path('alumnos/', AlumnoListView.as_view(), name='alumno_listar'),
    path('alumnos/crear/', AlumnoCreateView.as_view(), name='alumno_crear'),
    path('alumnos/<int:pk>/ver/', AlumnoDetailView.as_view(), name='alumno_detalle'),
    path('alumnos/<int:pk>/editar/', AlumnoUpdateView.as_view(), name='alumno_editar'),
    path('alumnos/<int:pk>/eliminar/', AlumnoDeleteView.as_view(), name='alumno_eliminar'),

    path('empleados/', EmpleadoListView.as_view(), name='listar_empleados'),
    path('empleados/crear/', EmpleadoCreateView.as_view(), name='crear_empleado'),
    path('empleados/ver/<int:pk>/', EmpleadoDetailView.as_view(), name='detalle_empleado'),
    path('empleados/editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='editar_empleado'),
    path('empleados/eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='eliminar_empleado'),

    path('catedraticos/', CatedraticoListView.as_view(), name='listar_catedraticos'),
    path('catedraticos/crear/', CatedraticoCreateView.as_view(), name='crear_catedratico'),
    path('catedraticos/ver/<int:pk>/', CatedraticoDetailView.as_view(), name='detalle_catedratico'),
    path('catedraticos/editar/<int:pk>/', CatedraticoUpdateView.as_view(), name='editar_catedratico'),
    path('catedraticos/eliminar/<int:pk>/', CatedraticoDeleteView.as_view(), name='eliminar_catedratico'),

    path('tutores/', TutorListView.as_view(), name='tutor_listar'),
    path('tutores/crear/', TutorCreateView.as_view(), name='tutor_crear'),
    path('tutores/<int:pk>/ver/', TutorDetailView.as_view(), name='tutor_detalle'),
    path('tutores/<int:pk>/editar/', TutorUpdateView.as_view(), name='tutor_editar'),
    path('tutores/<int:pk>/eliminar/', TutorDeleteView.as_view(), name='tutor_eliminar'),

    path('asignaturas/', AsignaturaListView.as_view(), name='asignatura_listar'),
    path('asignaturas/crear/', AsignaturaCreateView.as_view(), name='asignatura_crear'),
    path('asignaturas/<int:pk>/ver/', AsignaturaDetailView.as_view(), name='asignatura_detalle'),
    path('asignaturas/<int:pk>/editar/', AsignaturaUpdateView.as_view(), name='asignatura_editar'),
    path('asignaturas/<int:pk>/eliminar/', AsignaturaDeleteView.as_view(), name='asignatura_eliminar'),

    path('matriculas/', MatriculaListView.as_view(), name='matricula_listar'),
    path('matriculas/crear/', MatriculaCreateView.as_view(), name='matricula_crear'),
    path('matriculas/<int:pk>/ver/', MatriculaDetailView.as_view(), name='detalle_editar'),
    path('matriculas/<int:pk>/editar/', MatriculaUpdateView.as_view(), name='matricula_editar'),
    path('matriculas/<int:pk>/eliminar/', MatriculaDeleteView.as_view(), name='matricula_eliminar'),

    path('reportes/', ReportesListView.as_view(), name='reporte_listar'),
    path('reportes/crear/', ReportesCreateView.as_view(), name='reporte_crear'),
    path('reportes/<int:pk>/ver/', ReportesDetailView.as_view(), name='reporte_detalle'),
    path('reportes/<int:pk>/editar/', ReportesUpdateView.as_view(), name='reporte_editar'),
    path('reportes/<int:pk>/eliminar/', ReportesDeleteView.as_view(), name='reporte_eliminar'),

    path('expedientemedicos/', ExpedienteMedicoListView.as_view(), name='expedientemedico_listar'),
    path('expedientemedicos/crear/', ExpedienteMedicoCreateView.as_view(), name='expedientemedico_crear'),
    path('expedientemedicos/<int:pk>/ver/', ExpedienteMedicoDetailView.as_view(), name='expedientemedico_detalle'),
    path('expedientemedicos/<int:pk>/editar/', ExpedienteMedicoUpdateView.as_view(), name='expedientemedico_editar'),
    path('expedientemedicos/<int:pk>/eliminar/', ExpedienteMedicoDeleteView.as_view(), name='expedientemedico_eliminar'),

    path('horarios/', HorariosListView.as_view(), name='horarios_listar'),
    path('horarios/crear/', HorariosCreateView.as_view(), name='horarios_crear'),
    path('horarios/ver/<int:pk>/', HorariosDetailView.as_view(), name='horarios_detalle'),
    path('horarios/editar/<int:pk>/', HorariosUpdateView.as_view(), name='horarios_editar'),
    path('horarios/eliminar/<int:pk>/', HorariosDeleteView.as_view(), name='horarios_eliminar'),

    path('niveles/', NivelesListView.as_view(), name='niveles_listar'),
    path('niveles/crear/', NivelesCreateView.as_view(), name='niveles_crear'),
    path('niveles/ver/<int:pk>/', NivelesDetailView.as_view(), name='niveles_detalle'),
    path('niveles/editar/<int:pk>/', NivelesUpdateView.as_view(), name='niveles_editar'),
    path('niveles/eliminar/<int:pk>/', NivelesDeleteView.as_view(), name='niveles_eliminar'),

    path('parciales/', ParcialesListView.as_view(), name='parciales_listar'),
    path('parciales/crear/', ParcialesCreateView.as_view(), name='parciales_crear'),
    path('parciales/ver/<int:pk>/', ParcialesDetailView.as_view(), name='parciales_detalle'),
    path('parciales/editar/<int:pk>/', ParcialesUpdateView.as_view(), name='parciales_editar'),
    path('parciales/eliminar/<int:pk>/', ParcialesDeleteView.as_view(), name='parciales_eliminar'),

    path('notas/', NotasListView.as_view(), name='notas_listar'),
    path('notas/crear/', NotasCreateView.as_view(), name='notas_crear'),
    path('notas/ver/<int:pk>/', NotasDetailView.as_view(), name='notas_detalle'),
    path('notas/editar/', NotasUpdateView.as_view(), name='notas_editar'),
    path('notas/eliminar/<int:pk>/', NotasDeleteView.as_view(), name='notas_eliminar'),



    path('techhive/', InicioPantalla.as_view(), name='techhivee'),

    #pantallas segun usuario

    path('bienvenida/administrador/', BienvenidaAdministradorView.as_view(), name='bienvenida_administrador'),
    path('bienvenida/alumno/', BienvenidaAlumnoView.as_view(), name='bienvenida_alumno'),
    path('bienvenida/catedratico/', BienvenidaCatedraticoView.as_view(), name='bienvenida_catedratico'),


    #crear usuario

    path('usuarios/', UsuarioListView.as_view(), name='usuario_listar'),
    path('usuarios/<int:pk>/ver/', UsuarioDetailView.as_view(), name='usuario_detalle'),
    path('usuarios/agregar/', UsuarioCreateView.as_view(), name='usuario_crear'),
    path('usuarios/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_editar'),
    path('usuarios/<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuario_eliminar'),

    path('departamentos/', DepaListView.as_view(), name='departamento_listar'),
    path('departamentos/crear/', DepaCreateView.as_view(), name='departamento_crear'),
    path('departamentos/ver/<int:pk>/', DepaDetailView.as_view(), name='departamento_detalle'),
    path('departamentos/editar/<int:pk>/', DepaUpdateView.as_view(), name='departamento_editar'),
    path('departamentos/eliminar/<int:pk>/', DepaDeleteView.as_view(), name='departamento_eliminar'),

    path('municipios/', MuniListView.as_view(), name='municipio_listar'),
    path('municipios/crear/', MuniCreateView.as_view(), name='municipio_crear'),
    path('municipios/ver/<int:pk>/', MuniDetailView.as_view(), name='municipio_detalle'),
    path('municipios/editar/<int:pk>/', MuniUpdateView.as_view(), name='municipio_editar'),
    path('municipios/eliminar/<int:pk>/', MuniDeleteView.as_view(), name='municipio_eliminar'),



    path('meses/', MensualidadListView.as_view(), name='mensualidad_listar'),
    path('meses/crear/', MensualidadCreateView.as_view(), name='mensualidad_crear'),
    path('meses/ver/<int:pk>/', MensualidadDetailView.as_view(), name='mensualidad_detalle'),
    path('meses/editar/<int:pk>/', MensualidadUpdateView.as_view(), name='mensualidad_editar'),
    path('meses/eliminar/<int:pk>/', MensualidadDeleteView.as_view(), name='mensualidad_eliminar'),

    path('parametrossar/', ParametrosListView.as_view(), name='parametros_listar'),
    path('parametrossar/<int:pk>/ver/', ParametrosDetailView.as_view(), name='parametros_detalle'),
    path('parametrossar/agregar/', ParametrosCreateView.as_view(), name='parametros_crear'),
    path('parametrossar/<int:pk>/editar/', ParametrosUpdateView.as_view(), name='parametros_editar'),
    path('parametrossar/<int:pk>/eliminar/', ParametrosDeleteView.as_view(), name='parametros_eliminar'),

    path('categorias/', CateListView.as_view(), name='categoria_listar'),
    path('categorias/crear/', CateCreateView.as_view(), name='categoria_crear'),
    path('categorias/ver/<int:pk>/', CateDetailView.as_view(), name='categoria_detalle'),
    path('categorias/editar/<int:pk>/', CateUpdateView.as_view(), name='categoria_editar'),
    path('categorias/eliminar/<int:pk>/', CateDeleteView.as_view(), name='categoria_eliminar'),
    
    path('documentos/', DocListView.as_view(), name='documento_listar'),
    path('documentos/crear/', DocCreateView.as_view(), name='documento_crear'),
    path('documentos/ver/<int:pk>/', DocDetailView.as_view(), name='documento_detalle'),
    path('documentos/editar/<int:pk>/', DocUpdateView.as_view(), name='documento_editar'),
    path('documentos/eliminar/<int:pk>/', DocDeleteView.as_view(), name='documento_eliminar'),

    path('tipopago/', TipoPagoListView.as_view(), name='tipopago_listar'),
    path('tipopago/crear/', TipoPagoCreateView.as_view(), name='tipopago_crear'),
    path('tipopago/ver/<int:pk>/', TipoPagoDetailView.as_view(), name='tipopago_detalle'),
    path('tipopago/editar/<int:pk>/', TipoPagoUpdateView.as_view(), name='tipopago_editar'),
    path('tipopago/eliminar/<int:pk>/', TipoPagoDeleteView.as_view(), name='tipopago_eliminar'),

    path('tiporeporte/', TipoReporteListView.as_view(), name='tiporeporte_listar'),
    path('tiporeporte/crear/', TipoReporteCreateView.as_view(), name='tiporeporte_crear'),
    path('tiporeporte/ver/<int:pk>/', TipoReporteDetailView.as_view(), name='tiporeporte_detalle'),
    path('tiporeporte/editar/<int:pk>/', TipoReporteUpdateView.as_view(), name='tiporeporte_editar'),
    path('tiporeporte/eliminar/<int:pk>/', TipoReporteDeleteView.as_view(), name='tiporeporte_eliminar'),

    path('tiposanguineo/', TipoSanguineoListView.as_view(), name='tiposanguineo_listar'),
    path('tiposanguineo/crear/', TipoSanguineoCreateView.as_view(), name='tiposanguineo_crear'),
    path('tiposanguineo/ver/<int:pk>/', TipoSanguineoDetailView.as_view(), name='tiposanguineo_detalle'),
    path('tiposanguineo/editar/<int:pk>/', TipoSanguineoUpdateView.as_view(), name='tiposanguineo_editar'),
    path('tiposanguineo/eliminar/<int:pk>/', TipoSanguineoDeleteView.as_view(), name='tiposanguineo_eliminar'),


    path('seccion/', SeccionListView.as_view(), name='seccion_listar'),
    path('seccion/crear/', SeccionCreateView.as_view(), name='seccion_crear'),
    path('seccion/ver/<int:pk>/', SeccionDetailView.as_view(), name='seccion_detalle'),
    path('seccion/editar/<int:pk>/', SeccionUpdateView.as_view(), name='seccion_editar'),
    path('seccion/eliminar/<int:pk>/', SeccionDeleteView.as_view(), name='seccion_eliminar'),

    path('actitud/', ActitudListView.as_view(), name='actitud_listar'),
    path('actitud/crear/', ActitudCreateView.as_view(), name='actitud_crear'),
    path('actitud/ver/<int:pk>/', ActitudDetailView.as_view(), name='actitud_detalle'),
    path('actitud/editar/<int:pk>/', ActitudUpdateView.as_view(), name='actitud_editar'),
    path('actitud/eliminar/<int:pk>/', ActitudDeleteView.as_view(), name='actitud_eliminar'),

    path('centroeducativos/', CentroEducativoListView.as_view(), name='centroeducativo_listar'),
    path('centroeducativos/crear/', CentroEducativoCreateView.as_view(), name='centroeducativo_crear'),
    path('centroeducativos/ver/<int:pk>/', CentroEducativoDetailView.as_view(), name='centroeducativo_detalle'),
    path('centroeducativos/editar/<int:pk>/', CentroEducativoUpdateView.as_view(), name='centroeducativo_editar'),
    path('centroeducativos/eliminar/<int:pk>/', CentroEducativoDeleteView.as_view(), name='centroeducativo_eliminar'),

    path('tutoresalumnos/', TutoresAlumnosListView.as_view(), name='tutoresalumno_listar'),
    path('tutoresalumnos/crear/', TutoresAlumnosCreateView.as_view(), name='tutoresalumno_crear'),
    path('tutoresalumnos/ver/<int:pk>/', TutoresAlumnosDetailView.as_view(), name='tutoresalumno_detalle'),
    path('tutoresalumnos/editar/<int:pk>/', TutoresAlumnosUpdateView.as_view(), name='tutoresalumno_editar'),
    path('tutoresalumnos/eliminar/<int:pk>/', TutoresAlumnosDeleteView.as_view(), name='tutoresalumno_eliminar'),




    
    
#municipios y departamentos
    path('ajax/load-municipios/', load_municipios, name='ajax_load_municipios'),  
 

 #grados

    path('grados/', GradoListView.as_view(), name='grado_listar'),
    path('grados/crear/', GradoCreateView.as_view(), name='grado_crear'),
    path('grados/<int:pk>/ver/', GradoDetailView.as_view(), name='grado_detalle'),
    path('grados/<int:pk>/editar/', GradoUpdateView.as_view(), name='grado_editar'),
    path('grados/<int:pk>/eliminar/', GradoDeleteView.as_view(), name='grado_eliminar'),


#expedientes

    path('expedienteescolares/', ExpedienteEscolarListView.as_view(), name='expedienteescolar_listar'),
    path('expedienteescolares/crear/', ExpedienteEscolarCreateView.as_view(), name='expedienteescolar_crear'),
    path('expedienteescolares/<int:pk>/ver/', ExpedienteEscolarDetailView.as_view(), name='expedienteescolar_detalle'),
    path('expedienteescolares/<int:pk>/editar/', ExpedienteEscolarUpdateView.as_view(), name='expedienteescolar_editar'),
    path('expedienteescolares/<int:pk>/eliminar/', ExpedienteEscolarDeleteView.as_view(), name='expedienteescolar_eliminar'),


    #urls de Facturacion

    path('crear_pago/', crear_pago, name='crear_pago'),
    path('detalle_factura/<int:factura_id>/', detalle_factura, name='detalle_factura'),
    path('generar_factura/<int:pago_id>/', generar_factura, name='generar_factura'),
    path('lista_pagos/', lista_pagos, name='lista_pagos'),
    path('lista_facturas/', lista_facturas, name='lista_facturas'),

     #tipos de pagos historicos

    path('tipo_pago_historico/listar/', views.TipoPagoHistoricoListView.as_view(), name='tipo_pago_historico_listar'),
    path('tipo_pago_historico/crear/', views.TipoPagoHistoricoCreateView.as_view(), name='tipo_pago_historico_crear'),
    path('tipo_pago_historico/<int:pk>/editar/', views.TipoPagoHistoricoUpdateView.as_view(), name='tipo_pago_historico_editar'),
    path('tipo_pago_historico/<int:pk>/eliminar/', views.TipoPagoHistoricoDeleteView.as_view(), name='tipo_pago_historico_eliminar'),
  path('tipo_pago/<int:pk>/actualizar/', TipoPagoActualizarView.as_view(), name='tipo_pago_actualizar'),
    # ...

    path('tipo_pago_historico/<int:pk>/', views.TipoPagoHistoricoDetailView.as_view(), name='tipo_pago_historico_detalle'),
]