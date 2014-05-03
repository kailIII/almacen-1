from django import forms
class AreaForm(forms.Form):
	nombre=forms.CharField(max_length=100, required=True)

