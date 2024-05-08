from django.forms import ModelForm
from .models import Rental

class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = ['date', 'rental']