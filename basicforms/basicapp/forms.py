from django import forms
from django.core import validators


def name_start_z(value):
	if value[0].lower() != 'z':
		raise forms.ValidationError('name need to start with z')

class FormName(forms.Form):
	name = forms.CharField(validators=[name_start_z])
	email = forms.EmailField()
	verify_email = forms.EmailField(label='Enter your email again')
	text = forms.CharField(widget=forms.Textarea)
	botcatcher = forms.CharField(required = False, widget=forms.HiddenInput,
									validators=[validators.MaxLengthValidator(0)])

	'''def clean_botcatcher(self):
		botcatcher = self.cleaned_data['botcatcher']
		if len(botcatcher) > 0:
			raise forms.ValidationError('Got you biatch')
		return botcatcher'''

	def clean(self):
		all_clean_data = super().clean() #return all clean data
		email = all_clean_data['email']
		vmail = all_clean_data['verify_email']
		if email != vmail:
			raise forms.ValidationError('check your email and verified email match')