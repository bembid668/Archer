from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
from Archer_app.models import Archer

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name'}))
    password1 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Retype Password'}))

    def is_valid(self):
        form = super(UserCreateForm, self).is_valid()
        for f, error in self.error.iteritems():
            if f != '_all_':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

    class Meta:
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']
        model = User

class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholders': 'Password'}))

    def is_valid(self):
        form = super(AuthenticateForm, self).is_valid()
        for  f, error in self.errors.iteritems():
            if f != '_all_':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form


class ArcherForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class': 'ArcherText'}))


    def is_valid(self):
        form = super(ArcherForm, self).is_valid()
        for f in self.errors.iterkeys():
            if f != '_all_':
                self.fields[f].widget.attrs.update({'class': 'error ArcherTexts'})
        return forms

    class Meta:
        model = Archer
        exclude =('user',)
