from django.views.generic import DetailView
from .models import Client


class ClientView(DetailView):
    model = Client
