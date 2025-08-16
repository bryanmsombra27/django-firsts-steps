from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=100,
#                                 required=True,
#                                 error_messages={
#                                     "required": "Your name is required!", "max_length": "Please enter a shorther name", })
#     review_text = forms.CharField(
#         label="your feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)


# DE ESTA MANERA PODEMOS CONECTAR NUESTRO FORMULARIO CON UN MODELO DE LA BASE DE DATOS OBTENDRA DE FORMA AUTOMATICA LOS CAMPOS QUE TIENE EL MODELO, PERO HAY QUE TENER ENCUENTA QUE TOMA TOOS LOS CAMPOS QUE HAYA EN EL MODELO POR LO QUE HAY QUE TOMAR SOLO AQUELLOS QUE NECESITAMOS QUE RELLENE EL MODELO.
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'review_text', 'rating']
        labels = {
            "user_name": "Your name",
            "review_text": "Your feedback",
            "rating": "Your rating",
        }
        error_messages = {
            "user_name": {
                "required": "Your name is required!",
                "max_length": "Please enter a shorter name"
            },
            "review_text": {
                "max_length": "Please enter a shorter feedback"
            },
            "rating": {
                "min_value": "Please enter a rating between 1 and 5"
            }
        }
