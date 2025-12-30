from django.urls import path
from .views import SaleView

urlpatterns = [
    path("sales/<pk>/", SaleView.as_view(), name="sale_detail"),
]
