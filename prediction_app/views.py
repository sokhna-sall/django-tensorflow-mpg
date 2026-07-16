import os
import pandas as pd
import numpy as np
import tensorflow as tf
from django.shortcuts import render
from django.conf import settings
from .forms import CarPredictionForm

# Ordre exact des colonnes utilisé lors de l'entraînement de ton modèle
COLUMN_ORDER = ['Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Europe', 'Japan', 'USA']

# Chemin vers dnn_model.keras à la racine du projet
MODEL_PATH = os.path.join(settings.BASE_DIR, 'dnn_model.keras')

try:
    # Chargement unique du modèle au démarrage de Django
    MODEL = tf.keras.models.load_model(MODEL_PATH)
except Exception as e:
    MODEL = None
    print(f"ERREUR : Impossible de charger le modèle Keras : {e}")

def predict_mpg_view(request):
    prediction = None
    error_message = None
    
    if request.method == 'POST':
        form = CarPredictionForm(request.POST)
        if form.is_valid():
            if MODEL is None:
                error_message = "Le modèle de prédiction 'dnn_model.keras' n'a pas pu être chargé au démarrage."
            else:
                data = form.cleaned_data
                
                # Encodage One-Hot manuel de l'origine
                origin_usa = 1.0 if data['origin'] == 'USA' else 0.0
                origin_europe = 1.0 if data['origin'] == 'Europe' else 0.0
                origin_japan = 1.0 if data['origin'] == 'Japan' else 0.0
                
                # Regroupement des caractéristiques saisies
                input_data = {
                    'Cylinders': float(data['cylinders']),
                    'Displacement': float(data['displacement']),
                    'Horsepower': float(data['horsepower']),
                    'Weight': float(data['weight']),
                    'Acceleration': float(data['acceleration']),
                    'Model Year': float(data['model_year']),
                    'Europe': origin_europe,
                    'Japan': origin_japan,
                    'USA': origin_usa,
                }
                
                # Création du DataFrame Pandas dans le bon ordre de colonnes
                input_df = pd.DataFrame([input_data], columns=COLUMN_ORDER)
                input_df = input_df.astype('float32')
                
                try:
                    # Prédiction directe via le modèle (qui intègre déjà la couche de normalisation)
                    prediction_raw = MODEL.predict(input_df)
                    prediction = round(float(prediction_raw[0][0]), 2)
                except Exception as e:
                    error_message = f"Erreur lors de la prédiction : {str(e)}"
    else:
        form = CarPredictionForm()

    return render(request, 'prediction/predict.html', {
        'form': form,
        'prediction': prediction,
        'error_message': error_message
    })
