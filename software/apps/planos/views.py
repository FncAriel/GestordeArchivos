from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps.planos.forms import proyectoForm, RegistroForm, PlanoForm, ArquitectoForm
from apps.planos.models import proyecto, arquitecto, plano
from django.contrib.auth import login
from django.views.generic import FormView, CreateView, ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,'planos/index.html')

def index_planos(request):
        return render(request,'planos/index_planos.html')

def i2d(request):
        return render(request,'planos/2d.html')

def i3d(request):
        return render(request,'planos/3d.html')

def videos(request):
        return render(request,'planos/videos.html')

class CrearProyecto(CreateView):
    model = proyecto
    template_name = "planos/proyecto_form.html"
    form_class = proyectoForm
    success_url = reverse_lazy('proyecto_listar')


class Login(FormView):
        template_name = 'planos/login.html'
        form_class = AuthenticationForm
        success_url = reverse_lazy("proyecto_listar")

def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
                return HttpResponseRedirect(self.get_success_url())
        else:
                return super(Login, self).dispatch(request, *args, **kwargs)

def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

class RegistrodeUsuario(CreateView):
    model = User
    template_name = "planos/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')


class ProyectoList(ListView):
    model = proyecto
    template_name = 'planos/proyecto_list.html'

class ColabList(ListView):
    model = arquitecto
    template_name = 'planos/listarcolaboradores.html'

def upload_file(request):
    if request.method == 'POST':
        form = PlanoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index_planos')
    else:
        form = PlanoForm()
    return render(request, 'planos/upload_planos.html', {
        'form': form
    })

class CrearArquitecto(CreateView):
    model = arquitecto
    template_name = "planos/agregar_arquitecto.html"
    form_class = ArquitectoForm
    success_url = reverse_lazy('index_planos')
