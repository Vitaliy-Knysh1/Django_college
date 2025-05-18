from django import forms

class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="Ім'я")
    last_name = forms.CharField(max_length=50, label="Прізвище")
    email = forms.EmailField(label="Email")
    number_of_items = forms.IntegerField(min_value=1, label="Кількість")