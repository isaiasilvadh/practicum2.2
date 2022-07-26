from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.regex_helper import Group
from rest_framework import permissions, viewsets
from administrativo.serializers import *
# Create your views here.

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *


def index(request):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    medidores = Medidor.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'medidores': medidores, 'nroMedidores': len(medidores)}
    return render(request, 'index.html', informacion_template)

@login_required(login_url='login')
def editarMedidor(request, id):
    """
    """
    medidor = Medidor.objects.get(pk=id)
    if request.method=='POST':
        formulario = MedidorForm(request.POST, instance=medidor)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = MedidorForm(instance=medidor)
    diccionario = {'formulario': formulario}

    return render(request, 'editarMedidor.html', diccionario)

@login_required(login_url='login')
def eliminarMedidor(request, id):
    """
    """
    estudiante = Medidor.objects.get(pk=id)
    estudiante.delete()
    return redirect(index)

def ingreso(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(index)
    else:
        form = AuthenticationForm()

    informacion_template = {'form': form}
    return render(request, 'login.html', informacion_template)


def logout_view(request):
    logout(request)
    return redirect(index)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]


class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class MedidorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer
    permission_classes = [permissions.IsAuthenticated]

class MarcaMedidorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MarcaMedidor.objects.all()
    serializer_class = MarcaMedidorSerializer
    permission_classes = [permissions.IsAuthenticated]