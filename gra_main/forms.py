from django import forms
from .models import Registration

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=100, 
        widget= forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Username'
        })     
    )
    email = forms.CharField(
        max_length=100, 
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder': 'Email'
        })
    )
    phone = forms.CharField(
        max_length=100,
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder': 'Phone'
        })
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder': 'Password'
        })
    )
    location = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Location'
        })
    )
    
# Modal Form created based on the registration Model
class RegistrationModelForm(forms.ModelForm):
    class Meta:
        model = Registration
        
        fields = [
            'username', 
            'email', 
            'phone', 
            'password',
            'location'
        ]
        
        widgets = {
           'username':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Username'
            }),
            
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder': 'Email'
            }),
            
            'phone':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder': 'Phone'
            }),
            
            'password':forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder': 'Password'
            }),
            
            'location':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Location'
            })
        }
            