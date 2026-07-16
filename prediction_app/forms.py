from django import forms

class CarPredictionForm(forms.Form):
    cylinders = forms.IntegerField(
        label="Nombre de cylindres (Cylinders)", 
        min_value=3, max_value=12, initial=4,
        widget=forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-md'})
    )
    displacement = forms.FloatField(
        label="Cylindrée (Displacement)", initial=150.0,
        widget=forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-md'})
    )
    horsepower = forms.FloatField(
        label="Puissance (Horsepower)", initial=100.0,
        widget=forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-md'})
    )
    weight = forms.FloatField(
        label="Poids (Weight - lbs)", initial=3000.0,
        widget=forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-md'})
    )
    acceleration = forms.FloatField(
        label="Accélération", initial=15.0,
        widget=forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-md'})
    )
    model_year = forms.IntegerField(
        label="Année du modèle (ex: 80 pour 1980)", 
        min_value=70, max_value=82, initial=80,
        widget=forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-md'})
    )
    origin = forms.ChoiceField(
        label="Origine du véhicule",
        choices=[('USA', 'USA'), ('Europe', 'Europe'), ('Japan', 'Japan')],
        initial='USA',
        widget=forms.Select(attrs={'class': 'w-full p-2 border rounded-md bg-white'})
    )
