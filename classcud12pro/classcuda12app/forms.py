from django import forms

class EmailsendForm(forms.Form):
    name=forms.CharField()
    from_email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)