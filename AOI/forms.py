from django import forms
from .models import AOI,Post,Comment



class AOI_FORM(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AOI_FORM, self).__init__(*args, **kwargs)


    def save(self, *args, **kw):
        return self.instance

    class Meta:

        model = AOI

        fields = ['name','summary','thumbnail']



class POST_FORM(forms.ModelForm):

    class Meta:

        model = Post

        fields = ('aoi','title','text','video','image')


        def __init__(self, *args, **kwargs):
            super(POST_FORM, self).__init__(*args, **kwargs)

            self.fields['video'].required = False
            self.fields['image'].required = False



class Comment_Form(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ('post','text', 'image')
