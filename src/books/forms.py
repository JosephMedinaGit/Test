from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Full name"}))
	email	= forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Email"}))
	content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "Write your message here ..."}))

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is taken")
		else:
			if (validateEmail(email) == True):

				return email
			else:
				raise forms.ValidationError("inncorrect email format")


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Full name"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Password"}))

class RegisterForm(forms.Form):
	username = forms.CharField()
	email	= forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username is taken")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is taken")
		else:
			if (validateEmail(email) == True):

				return email
			else:
				raise forms.ValidationError("inncorrect email format")

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('passwsord')
		passwsord2 = self.cleaned_data.get('passwsord2')
		if passwsord2 != password:
			raise forms.ValidationError("Passwords must match.")
		return data

class ProfileForm(forms.Form):
	name = forms.CharField()
	nick_name = forms.CharField()
	email = forms.EmailField()
	home_addr = forms.CharField()

	#address
	address_1 = forms.CharField()
	address_2 = forms.CharField()

	city = forms.CharField()
	state = forms.CharField()
	zip_code = forms.CharField()

	#image = forms.ImageField()
	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is taken")
		else:
			if ( validateEmail(email) == True):

				return email
			else:
				raise forms.ValidationError("inncorrect email format")

	def validateEmail(email):
		from django.core.validators import validate_email
		from django.core.exceptions import ValidationError
		try:
			validate_email(email)
			return True
		except ValidationError:
			return False

