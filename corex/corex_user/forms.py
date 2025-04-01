from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class Step1Form(forms.Form):
    fitness_goals = forms.MultipleChoiceField(
        choices=[
            ('Physical health and fitness', 'Physical health and fitness'),
            ('Building a Better Body', 'Building a Better Body'),
            ('Increase confidence', 'Increase confidence'),
            ('Stress and relaxation', 'Stress and relaxation'),
            ('Increase Stamina', 'Increase Stamina'),
            ('Social aspects', 'Social aspects'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="What is your goal?"
    )

class Step2Form(forms.Form):
    age = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(16, 101)],  # Ages 16 to 100
        widget=forms.Select,
        required=True,
        label="What is your age?"
    )

class Step3Form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'height', 'weight', 'gender']
        widgets = {
            'password': forms.PasswordInput(),
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Phone number", max_length=15)
    remember_me = forms.BooleanField(required=False, label="Remember me")