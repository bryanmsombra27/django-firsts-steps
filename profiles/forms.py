from django import forms


class ProfileForm(forms.Form):
    # user_image = forms.FileField()
    # SOLO FUNCIONA CON IMAGENES
    user_image = forms.ImageField()
