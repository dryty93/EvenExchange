from .models import Message
from django import forms


class Message_Form(forms.ModelForm):

    class Meta:

        model= Message
        fields = ('subject','receiver','body')
