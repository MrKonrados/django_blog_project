from django import forms

from .models import Comment


class CommentForm(forms.ModelForm, forms.Form):

    class Meta:
        model = Comment
        exclude = ('parent', 'post')
        widgets = {
            'name':    forms.TextInput(attrs={'class': 'form-control'}),
            'email':   forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
