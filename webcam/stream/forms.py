from django import forms

class checkForm(forms.Form):
    blueCheck = forms.CheckboxInput
    greenCheck = forms.CheckboxInput
    redCheck = forms.CheckboxInput