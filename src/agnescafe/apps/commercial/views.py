from django.views.generic import DetailView
from .models import Sale


class SaleView(DetailView):
    model = Sale
