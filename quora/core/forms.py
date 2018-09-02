from django import forms
from .models import User
from questans.models import Questions, Answers
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'username']

class LoginForm(forms.ModelForm):
	#username = forms.CharField()
	class Meta:
		model = User
		fields=['username','password']

class QuestionForm(forms.ModelForm):

	class Meta:
		model = Questions
		fields=['question']

class AnswerForm(forms.ModelForm):

	 class Meta:
	 	model=Answers
	 	fields=['answer_text']