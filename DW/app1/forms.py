from django import forms
from .models import Review

class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    number_of_items = forms.IntegerField(min_value=1)
    card_number = forms.CharField(max_length=19, min_length=13)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text']
        labels = {
            'name': "Ваше ім'я",
            'text': "Відгук",
        }