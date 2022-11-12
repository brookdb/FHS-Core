from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from .models import CustomUser, Profile
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Password confirmation',
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name',)
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
        }


class CustomPasswordResetForm(PasswordResetForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
        labels = {
            'email': 'Email',
        }
class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'customForm-fileinput'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'customForm-textarea'}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location', 'inspo']
