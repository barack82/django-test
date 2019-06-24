from django import forms
from .models import User

class new_form(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'