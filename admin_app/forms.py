from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Orders, Services, Clients
# from datepickerwidget import widgets
# from input_mask.widgets import InputMask
#
# class SSNInput(InputMask):
#     mask = {'mask': '999-99-9999'}

class DateInput(forms.DateInput):
    input_type = 'date'

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients

        fields = '__all__'

        widgets = {
        'bith': DateInput,
        'phone': forms.TextInput(attrs={'data-mask': '+38(099) 999-99-99'})
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = [
            'service',
            'date',
            'client',
            'price',
            'info',
            'status',
        ]

        widgets = {
            'date': DateInput
        }

        labels = {
            'price': 'price, UAH',
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['name']
        labels = {
            'name': 'Contact name'
        }
