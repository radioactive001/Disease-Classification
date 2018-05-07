from django import forms

class TextForm(forms.Form):
	text = form.CharField()