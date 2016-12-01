from django import forms
from .models import Input, STOCKS

class InputForm(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    stock = forms.ChoiceField(choices=STOCKS, required=True,
                              widget=forms.Select(attrs = attrs)
                              )
    class Meta:

        model = Input
        fields = ['stock']
