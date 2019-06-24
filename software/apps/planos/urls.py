from django.urls import path, include
from apps.planos.views import Login, RegistrodeUsuario, ProyectoList, CrearProyecto, upload_file, CrearArquitecto, index, index_planos, i2d, i3d, videos, ColabList

urlpatterns = [
    path('login/', Login.as_view(), name = 'login'),
    path('proyectonuevo/', CrearProyecto.as_view(), name = 'proyecto_nuevo'),
    path('registrar/',RegistrodeUsuario.as_view(), name ='registrar'),
    path('listarproyecto/', ProyectoList.as_view(), name = 'proyecto_listar'),
    path('agregararquitecto/', CrearArquitecto.as_view(), name = 'arquitecto_nuevo'),
    path('subirplano/', upload_file, name = 'upload_planos'),
    path('', index, name = 'index'),
    path('indexplanos/', index_planos, name = 'index_planos'),
    path('trabajo2d/', i2d, name = '2d'),
    path('trabajo3d/', i3d, name = '3d'),
    path('videos/', videos, name = 'videos'),
    path('colaboradores/', ColabList.as_view(), name = 'colablist'),
]
