from django import forms
from models import 	Venta

class Venta_Form(forms.ModelForm):

	class Meta:
		model = Venta 

		fields = (
			'productos', 
			)
