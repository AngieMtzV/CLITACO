from django import forms
from models import valoracionInicial, avanceRapido, evolucionConsultaExterna, refContraRef

class ValoracionInicialForm(forms.ModelForm):

	class Meta:
		model = valoracionInicial
		fields = (
			'nombre_paciente_VI',
			'edad',
			'nota_medica',
			'peso_CE',
			'talla_CE',
			'imc_CE',
			'cintura_CE',
			'icc_CE',
			'peso_ideal_CE',
			'fc_CE',
			'fr_CE',
			'ta_CE1',
			'ta_CE2',
			'diagnostico_CE',
			'plan_CE',
			'consentimiento_info',
			) 

class AvanceRapidoForm(forms.ModelForm):

	class Meta:
		model = avanceRapido
		fields = (
			'diagnostico_AR',
			'peso_AR',
			'talla_AR',
			'imc_AR',
			'ta_AR1',
			'ta_AR2',
			'fc_AR',
			'fr_AR',
			'bioquimicos_AR',
			)
class EvolConsultaExterna(forms.ModelForm):

	class Meta:
		model = evolucionConsultaExterna
		fields = (
			'signos',
			)

class ValoracionEditForm(forms.ModelForm):

	class Meta:
		model = valoracionInicial
		fields = (
			'nombre_paciente_VI',
			'edad',
			'nota_medica',
			'peso_CE',
			'talla_CE',
			'imc_CE',
			'cintura_CE',
			'icc_CE',
			'peso_ideal_CE',
			'fc_CE',
			'fr_CE',
			'ta_CE1',
			'ta_CE2',
			'diagnostico_CE',
			'plan_CE',
			'consentimiento_info',
			) 

class ReferenciaForm(forms.ModelForm):

	class Meta:
		model = refContraRef
		fields = (
			'urgencia',
			'unidad_a_referir',
			'servicio',
			'temperatura',
			'motivo',
			'impresion', 
			)

