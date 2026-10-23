from django.contrib import admin
from django.urls import path, include
from materias.views import pagina_reserva

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('materias.urls')),      # Endpoints da API (/api/materias/)
    path('reserva/', pagina_reserva, name='reserva'), # Página do Chatbot (/reserva/)
]