# Generated by Django 4.2.2 on 2023-08-09 22:20

import TechHive.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Actitud', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombresAlumno', models.CharField(help_text='No debe contener numeros, caracteres: 3-20 ', max_length=20)),
                ('ApellidosAlumno', models.CharField(help_text='No debe contener numeros, caracteres: 2-30 ', max_length=30)),
                ('DPI', models.CharField(help_text='No, debe contenes letras, digitos: 13-15 ', max_length=20, unique=True)),
                ('FechaNacimientoAlumno', models.DateField()),
                ('DireccionAlumno', models.CharField(help_text=' No se permiten espacios dobles, Longitud requerida: 5-30 ', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(help_text='No debe contener numeros, caracteres 5-25 ', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoriaEmpleado', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CentroEducativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCentro', models.CharField(max_length=100)),
                ('CodigoCentro', models.IntegerField()),
                ('Titularidad', models.CharField(max_length=100)),
                ('Sucursal', models.CharField(max_length=100)),
                ('Telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentoDPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocumentoDPI', models.CharField(max_length=30)),
                ('longitud', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grado', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='HorariosNivelEducativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Horario', models.CharField(help_text='No debe contener numeros, caracteres 5-15', max_length=15)),
                ('HoraEntrada', models.TimeField()),
                ('HoraSalida', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Meses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Meses', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ParametrosSAR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CAI', models.CharField(max_length=100)),
                ('RTN', models.CharField(help_text='No, debe contenes letras, digitos: 14 ', max_length=14)),
                ('RangoInicial', models.CharField(max_length=8)),
                ('RangoFinal', models.CharField(max_length=8)),
                ('TipoDocumento', models.CharField(max_length=12)),
                ('Establecimiento', models.CharField(max_length=4)),
                ('FechaEmision', models.DateField()),
                ('FechaVencimiento', models.DateField()),
                ('Correlativo', models.CharField(max_length=100)),
                ('Sucursal', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ParcialesAcademicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ParcialAcademico', models.CharField(help_text='Longitud requerida: 5-20 caracteres ', max_length=20)),
                ('FechaInicio', models.DateField()),
                ('FechaFinal', models.DateField()),
                ('Año', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seccion', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=40)),
                ('monto', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoReporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoReporte', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSanguineo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoSanguineo', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombresTutor', models.CharField(help_text='No debe contener numeros, caracteres: 3-20 ', max_length=20)),
                ('ApellidosTutor', models.CharField(help_text='No debe contener numeros, caracteres: 2-30 ', max_length=30)),
                ('DPI', models.CharField(help_text='No, debe contenes letras, digitos: 13-15 ', max_length=20, unique=True)),
                ('Tel_Tutor', models.CharField(help_text='Longitud requerida: 8 digitos ', max_length=8)),
                ('Parentesco', models.CharField(help_text='No debe contener numeros, caracteres 3-15 ', max_length=15)),
                ('DocumentoDPI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.documentodpi')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(help_text='La contraseña debe tener al menos 8 caracteres y contener al menos un número, una letra mayúscula y una letra minúscula.', max_length=128)),
                ('intentos_fallidos', models.IntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
                ('rol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TechHive.rol')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TutoresAlumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.alumno')),
                ('Tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='TipoPagoHistorico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tipo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.tipopago')),
            ],
        ),
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescripcionReporte', models.CharField(help_text='Longitud requerida: caracteres 6-150 ', max_length=150)),
                ('FechaReporte', models.DateField()),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.alumno')),
                ('TipoReporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.tiporeporte')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaHoraPago', models.DateTimeField(auto_now_add=True)),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.alumno')),
                ('Meses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.meses')),
                ('TipoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.tipopago')),
                ('Tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='NotasAlumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NotaAcumulativo', models.DecimalField(decimal_places=2, help_text='Maximo valor para Nota de Acumulativo: 2 caracteres, 70.00 ', max_digits=4)),
                ('NotaExamen', models.DecimalField(decimal_places=2, help_text='Maximo valor para Nota de Examen 2 caracteres, 30.00 ', max_digits=4)),
                ('NotaFinal', models.DecimalField(decimal_places=2, help_text='Maximo valor para Nota final 2 caracteres, 100.00 ', max_digits=4)),
                ('PromedioClase', models.DecimalField(decimal_places=2, help_text='Maximo valor para promedio de clase 2 caracteres, 100.00 ', max_digits=4)),
                ('ApellidosAlumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.alumno')),
                ('Asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.asignatura')),
                ('ParcialAcademico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.parcialesacademicos')),
            ],
        ),
        migrations.CreateModel(
            name='NivelEducativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NivelEducativo', models.CharField(help_text='No debe contener numeros, caractreres: 5-20 ', max_length=20)),
                ('Horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.horariosniveleducativo')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMunicipio', models.CharField(max_length=100, unique=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor', models.CharField(max_length=100)),
                ('alumno', models.CharField(max_length=100)),
                ('fecha_matricula', models.DateField()),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.grado')),
                ('pagos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.pago')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='grado',
            name='NivelEducativo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.niveleducativo'),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_factura', models.CharField(max_length=21, unique=True)),
                ('fecha_emision', models.DateField(auto_now_add=True)),
                ('CentroEducativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.centroeducativo')),
                ('ParametrosSAR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.parametrossar')),
                ('pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.pago')),
            ],
        ),
        migrations.CreateModel(
            name='ExpedienteMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EnfermedadCronica1', models.CharField(help_text='Longitud requerida: 3-30 caracteres', max_length=20)),
                ('EnfermedadCronica2', models.CharField(help_text='Longitud requerida: 3-30 caracteres ', max_length=20)),
                ('EnfermedadCronica3', models.CharField(help_text='Longitud requerida: 3-30 caracteres ', max_length=20)),
                ('MedicamentoUsoDiario1', models.CharField(help_text='Longitud requerida: 3-30 caracteres ', max_length=20)),
                ('MedicamentoUsoDiario2', models.CharField(help_text='Longitud requerida: 3-30 caracteres ', max_length=20)),
                ('Alergia1', models.CharField(help_text='Longitud requerida: 3-30 caracteres ', max_length=20)),
                ('Alergia2', models.CharField(help_text='Longitud requerida: 3-30 caracteres ', max_length=20)),
                ('Alergia3', models.CharField(help_text='Longitud requerida: 3-30 caracteres ', max_length=20)),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.alumno')),
                ('Grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.grado')),
                ('Tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='ExpedienteEscolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InstitutoAnterior', models.CharField(max_length=60)),
                ('PromedioAnualAnterior', models.IntegerField()),
                ('Actitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.actitud')),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.alumno')),
                ('Tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombresEmpleado', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[^\\d]{3,20}$', 'No debe contener números, caracteres: 3-20'), TechHive.models.no_numeros_validator])),
                ('ApellidosEmpleado', models.CharField(help_text='No debe contener numeros, caracteres 2-30 ', max_length=30)),
                ('DPI', models.CharField(help_text='No, debe contenes letras, digitos: 13-15 ', max_length=20, unique=True)),
                ('FechaNacimientoEmpleado', models.DateField()),
                ('Tel_Empleado', models.CharField(help_text='No debe contener letras, 8 digitos ', max_length=8)),
                ('CategoriaEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.categoriaempleado')),
                ('DocumentoDPI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.documentodpi')),
            ],
        ),
        migrations.AddField(
            model_name='centroeducativo',
            name='Localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.departamento'),
        ),
        migrations.CreateModel(
            name='Catedratico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombresCatedratico', models.CharField(help_text='No debe contener numeros, caracteres 3-20 ', max_length=20)),
                ('ApellidosCatedratico', models.CharField(help_text='No debe contener numeros, caracteres 2-30 ', max_length=30)),
                ('DPI', models.CharField(help_text='No, debe contenes letras, digitos: 13-15 ', max_length=20, unique=True)),
                ('FechaNacimientoCatedratico', models.DateField()),
                ('Tel_Catedratico', models.CharField(help_text='No debe contener letras, 8 digitos', max_length=8)),
                ('DocumentoDPI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.documentodpi')),
            ],
        ),
        migrations.AddField(
            model_name='asignatura',
            name='Catedratico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.catedratico'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='NivelEducativo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.niveleducativo'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='Departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.departamento'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='DocumentoDPI',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.documentodpi'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='Grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.grado'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='Municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.municipio'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='Seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.seccion'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='TipoSanguineo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.tiposanguineo'),
        ),
    ]
