from django import forms
from .models import Review

class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="Ім'я")
    last_name = forms.CharField(max_length=50, label="Прізвище")
    email = forms.EmailField(label="Email")
    number_of_items = forms.IntegerField(min_value=1, label="Кількість")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text']
        labels = {
            'name': "Ваше ім'я",
            'text': "Відгук",
        }