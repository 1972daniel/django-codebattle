

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from.models import Submission, User

class SubmissionForm(ModelForm):
	class Meta:
		model = Submission
		fields = ['details']


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User 
		fields = ['username', 'email', 'name', 'password1', 'password2']



