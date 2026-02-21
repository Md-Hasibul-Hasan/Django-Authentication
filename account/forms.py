from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password:',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password',
                'class': "mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-rose-500 focus:border-rose-500 sm:text-sm"
            }
        )
        )
    confirm_password = forms.CharField(
        label='Confirm Password:',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm your password',
                'class': "mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-rose-500 focus:border-rose-500 sm:text-sm"
            }
        )
        )
    class Meta:
        model = User
        fields = ['name','email']

        labels = {
            'name': 'Name:',
            'email': 'Email:',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your name',
                    'class': "mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-rose-500 focus:border-rose-500 sm:text-sm"
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter your email',
                    'class': "mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-rose-500 focus:border-rose-500 sm:text-sm"
                }
            ),
            
        }


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password', 'Password does not match')
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email
    

class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder':'you@example.com'
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                ('No account is associated with is email.')
            )
        return email

    