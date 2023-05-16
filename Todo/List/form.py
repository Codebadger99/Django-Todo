from django import forms

from .models import list


class TodoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'add new task','class': 'form_input'}))
    class Meta:
        model = list
        fields = "__all__"