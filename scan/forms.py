from django import forms

class QRCodeForm(forms.Form):
    qr_code_image = forms.ImageField()
