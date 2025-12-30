from django.urls import path
from .views import ClientView

urlpatterns = [
    path("clients/<pk>/", ClientView.as_view(), name="client_detail"),
]
