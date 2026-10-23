from django.shortcuts import render
from rest_framework import viewsets
from .models import Materia
from .serializers import MateriaSerializer

# View da API REST (CRUD automático)
class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

# View do Frontend (Chatbot)
def pagina_reserva(request):
    return render(request, 'materias/laboratorio.html')