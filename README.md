---

```markdown
# Application de Prédiction de Consommation MPG (EPT - MILIA1)

Ce projet est une application web Django réalisée dans le cadre du Master 1 IA (M1ILIA) à l'Université Cheikh Anta Diop de Dakar (UCAD). 

Elle utilise un modèle de Deep Learning (réseau de neurones) développé avec **TensorFlow et Keras** pour prédire la consommation d'essence d'un véhicule (en Miles Per Gallon - MPG) selon ses caractéristiques techniques.

---

## Comment fonctionne le projet ?

Le projet est divisé en plusieurs parties simples :
*   **La page web ** : Une page simple créée avec du HTML et stylisée avec CSS.
*   **Le modèle d'IA** : Le fichier `dnn_model.keras` est chargé par Django pour faire le calcul de la prédiction.
*   **La mise en ligne (Production)** : Le projet est hébergé sur un serveur AWS EC2, utilisant Gunicorn et Nginx.

---

## Structure des fichiers du projet

```text
tensorflow_django/
├── db.sqlite3
├── manage.py
├── tensorflow_django/          # Configuration générale de Django
│   ├── settings.py             # Fichier de configuration
│   ├── urls.py
│   └── wsgi.py                 # Liaison avec Gunicorn
├── prediction_app/             # Notre application de prédiction
│   ├── dnn_model.keras         # Le modèle TensorFlow
│   ├── views.py                # Le code qui charge le modèle et prédit
│   ├── urls.py
│   └── templates/
│       └── prediction_app/
│           └── predict.html    # La page du formulaire
├── venv/                       # Environnement virtuel
└── .gitignore                  # Empêche d'envoyer le dossier venv sur GitHub

```

---

## Comment lancer le projet en local (sur votre PC)

### 1. Récupérer le code

```bash
git clone [https://github.com/sokhna-sall/django-tensorflow-mpg.git](https://github.com/sokhna-sall/django-tensorflow-mpg.git)
cd django-tensorflow-mpg

```

### 2. Créer et activer l'environnement virtuel

*Sur Windows (Git Bash) :*

```bash
python -m venv venv
source venv/Scripts/activate

```

*Sur Linux ou Mac :*

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Installer les paquets Python nécessaires

```bash
pip install django tensorflow pandas numpy gunicorn

```

### 4. Lancer le serveur Django

```bash
python manage.py migrate
python manage.py runserver

```

Vous pouvez maintenant ouvrir votre navigateur et aller sur : http://127.0.0.1:8000/predict/
---

## Version en ligne (AWS EC2)

L'application a été déployée sur une instance AWS. Elle fonctionne en tâche de fond (pas besoin de lancer `runserver`) grâce à Gunicorn et Nginx.

* **Lien direct du site** : http://3.92.26.161/predict/
* **Gunicorn** (gère Django) : Tourne en arrière-plan avec Systemd (`sudo systemctl status gunicorn`)
* **Nginx** (redirige le trafic) : Gère les requêtes sur le port 80 (`sudo systemctl status nginx`)

---

## Comment tester l'application ?

### Test : Faire une prédiction classique

1. Allez sur le site : [http://3.92.26.161/predict/](http://3.92.26.161/predict/)
2. Remplissez le formulaire avec ces valeurs de test :
* **Cylindres** : `8`
* **Cylindrée (Displacement)** : `307.0`
* **Puissance (Horsepower)** : `130.0`
* **Poids (Weight)** : `3500.0`
* **Accélération** : `12.0`
* **Année du modèle** : `70` *(pour l'année 1970)*
* **Origine** : `USA` (ou `1`)


3. Cliquez sur **"Prédire la consommation"**.
4. **Résultat attendu** : L'écran doit afficher une prédiction réaliste (généralement entre **15.0 et 25.0 MPG** pour ce type de grosse voiture).



---

**Développé par :** Sokhna Sall (MILIA1 - EPT)
