from django import forms
from models import DocenteAlumno, PerfilDocente

OPCIONES = (

		('Com', 'Com'),
		('N.Com', 'N.Com'),
		('C.Con', 'C.Con'),
		('Fam', 'Fam'),
		)

OPCIONES2 = (

		('Con.A', 'Con.A'),
		('Sin. A', 'Sin.A'),
		('Pm.A', 'P/m.A'),
		('Tm.A', 'T/m.A'),
		
		)


class FormularioDocenteForm(forms.ModelForm):

	class Meta:
		model = DocenteAlumno

		fields = (
			'alumno',
			'dias',
			'asistencia',
			'calificacion',

			)
	historia_clinica = forms.ChoiceField(label = 'Elabora Historia Clinica', choices=OPCIONES, widget=forms.RadioSelect())
	hist_clinica = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	diagnosticos = forms.ChoiceField(label = 'Emite Disgnosticos', choices=OPCIONES, widget=forms.RadioSelect())
	diag = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	rec_deriva = forms.ChoiceField(label = 'Rec.Deriva Patol. Buc', choices=OPCIONES, widget=forms.RadioSelect())
	rec_der = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	rec_edo = forms.ChoiceField(label = 'Rec. Edo San Pat.C.De', choices=OPCIONES, widget=forms.RadioSelect())
	rec_edo2 = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	mat_dental = forms.ChoiceField(label = 'Manipula Material Dental', choices=OPCIONES, widget=forms.RadioSelect())
	mat_dent = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	asis_faseII = forms.ChoiceField(label = 'Asis.Tto.Perio.FaseII', choices=OPCIONES, widget=forms.RadioSelect())
	as_faseII = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	aplica_anestesia = forms.ChoiceField(label = 'Aplica Tec. de Anestesia', choices=OPCIONES, widget=forms.RadioSelect())
	apli_anes = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	tec_rx = forms.ChoiceField(label = 'Tec. Rx e Interpreta', choices=OPCIONES, widget=forms.RadioSelect())
	tec_rx2 = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	obt_permanentes = forms.ChoiceField(label = 'Obt. Mat. Permanentes', choices=OPCIONES, widget=forms.RadioSelect())
	obt_perm = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	extrae_dientes = forms.ChoiceField(label = 'Extrae Dientes', choices=OPCIONES, widget=forms.RadioSelect())
	ext_dientes = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	tto_conductos = forms.ChoiceField(label = 'Tto. De Conductos', choices=OPCIONES, widget=forms.RadioSelect())
	tto_conduct = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	cirujia_d_b = forms.ChoiceField(label = 'A. Cirugia Tej. D y B', choices=OPCIONES, widget=forms.RadioSelect())
	cirujua_db = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	ind_dise_tot = forms.ChoiceField(label = 'Ind.Dise.Ajus.Prot.Tot', choices=OPCIONES, widget=forms.RadioSelect())
	ind_dise_tot2 = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	ind_dise_fij = forms.ChoiceField(label = 'Ind.Dise.Ajus.Prot.Fij', choices=OPCIONES, widget=forms.RadioSelect())
	ind_dise_fij2 = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	ind_dise_rem = forms.ChoiceField(label = 'Ind.Dise.Ajus.Prot.Rem', choices=OPCIONES, widget=forms.RadioSelect())
	ind_dise_rem2 = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	ind_desprogram = forms.ChoiceField(label = 'Ind.Dis.Desprogram', choices=OPCIONES, widget=forms.RadioSelect())
	ind_desprog = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	real_tinciones = forms.ChoiceField(label = 'Realiza Tinciones', choices=OPCIONES, widget=forms.RadioSelect())
	real_tinc = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	feruliza = forms.ChoiceField(label = 'Feruliza', choices=OPCIONES, widget=forms.RadioSelect())
	feruliza2 = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())
	practica_biops = forms.ChoiceField(label = 'Practica Toma Biops.', choices=OPCIONES, widget=forms.RadioSelect())
	pract_biops = forms.ChoiceField(choices=OPCIONES2, widget=forms.RadioSelect())

class DocenteForm(forms.ModelForm):
	class Meta:
		model = PerfilDocente

		fields = (
			'imagen_docente',

			)
	 