from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import TextInput,PasswordInput

from .models import Record



# Register User

class CreateForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']



# Login a user
        
class LoginForm(AuthenticationForm):
     
     username = forms.CharField(widget=TextInput())
     password = forms.CharField(widget=PasswordInput())


# Create Record Form
     
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model=Record
        feilds='__all__'
        exclude=['creation_date']


# Update Record Form
     
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model=Record
        feilds='__all__'
        exclude=['creation_date']

















