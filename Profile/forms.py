from django import forms
from .models import Profile,User

class Registration_Form(forms.ModelForm):

    def save(self, *args, **kw):

        return self.instance

    class Meta:

        model = Profile

        fields = ('name','image','bio','location', 'career')

