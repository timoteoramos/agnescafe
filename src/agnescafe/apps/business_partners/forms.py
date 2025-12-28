from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Client


class ClientForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        label="Número de telefone",
        required=False,
    )

    class Meta:
        model = Client
        fields = "__all__"
