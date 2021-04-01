from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UsernameField(forms.EmailField):
    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs['disabled'] = True
        return attrs


class CreateUserForm(UserCreationForm):
    def __init__(self, email=None, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = []
        # field_classes = {"username": UsernameField}
