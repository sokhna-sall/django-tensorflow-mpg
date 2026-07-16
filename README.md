# 🚗 Django TensorFlow MPG Predictor (UCAD - M1ILIA)

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0.7-green.svg)](https://www.djangoproject.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![Nginx](https://img.shields.io/badge/Nginx-Latest-brightgreen.svg)](https://nginx.org/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-26.0-red.svg)](https://gunicorn.org/)

Ce projet consiste en une application web de production développée dans le cadre du Master 1 Intelligence Artificielle et Informatique Décisionnelle (M1ILIA) à l'**Université Cheikh Anta Diop de Dakar (UCAD)**. 

L'application intègre un modèle de réseau de neurones profonds (Deep Learning) préalablement entraîné avec **TensorFlow/Keras** pour résoudre un problème de régression : prédire la consommation de carburant d'un véhicule (exprimée en MPG - *Miles Per Gallon*) à partir de ses spécifications techniques.

---

## 🛠️ Architecture du Projet

Le projet adopte une architecture robuste séparant le développement de la production :
*   **Frontend** : Interface utilisateur moderne et responsive conçue avec **Tailwind CSS**.
*   **Backend** : Framework **Django 6.0.7** assurant le routage, la validation des données et la logique métier.
*   **Moteur d'IA** : Modèle de Deep Learning au format `dnn_model.keras` chargé dynamiquement pour effectuer les inférences en temps réel avec **TensorFlow** et **Pandas**.
*   **Serveur d'Inférence (Production)** : **Gunicorn (WSGI)** géré par un daemon de service **Systemd**.
*   **Serveur Web Frontal** : **Nginx** configuré en Reverse Proxy sur le port 80 avec gestion du temps d'attente (timeout) optimisé pour les modèles de Deep Learning.
*   **Hébergement** : Instance cloud **AWS EC2** sous Debian.

---

## 📂 Structure du Répertoire

```text
tensorflow_django/
├── db.sqlite3
├── manage.py
├── tensorflow_django/          # Configuration globale du projet Django
│   ├── __init__.py
│   ├── settings.py             # Configuration (ALLOWED_HOSTS, etc.)
│   ├── urls.py
│   └── wsgi.py                 # Point d'entrée pour Gunicorn
├── prediction_app/             # Application Django principale
│   ├── dnn_model.keras         # Le modèle TensorFlow pré-entraîné
│   ├── views.py                # Logique de chargement du modèle et d'inférence
│   ├── urls.py
│   └── templates/
│       └── prediction_app/
│           └── predict.html    # Formulaire utilisateur Tailwind CSS
├── venv/                       # Environnement virtuel de production
├── .gitignore                  # Fichiers exclus du contrôle de version (ex: venv)
└── README.md                   # Documentation du projet
🚀 Guide d'Installation et Lancement Local
Suivez ces instructions pour installer et exécuter le projet sur votre machine locale de développement.

1. Clonage du projet
Bash
git clone [https://github.com/sokhna-sall/django-tensorflow-mpg.git](https://github.com/sokhna-sall/django-tensorflow-mpg.git)
cd django-tensorflow-mpg
2. Création et activation de l'environnement virtuel
Bash
# Sous Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Sous Windows (Git Bash)
python -m venv venv
source venv/Scripts/activate
3. Installation des dépendances
Bash
pip install django tensorflow pandas numpy gunicorn
4. Lancement des migrations et du serveur de développement
Bash
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
Accédez ensuite à l'application via votre navigateur à l'adresse suivante : http://127.0.0.1:8000/predict/

🌐 Guide de Déploiement (Production AWS EC2)
L'application est déployée de manière robuste sur AWS en utilisant Gunicorn comme serveur d'application et Nginx comme serveur web frontal (Reverse Proxy sur le Port 80).

Adresse IP Publique du projet : http://3.92.26.161/predict/

Statut du Service Gunicorn : Géré par Systemd (sudo systemctl status gunicorn)

Statut du Service Web : Géré par Nginx (sudo systemctl status nginx)

🧪 Cahier de Recette & Procédures de Test (Pour Évaluation)
Pour valider le bon fonctionnement du déploiement et du modèle de Deep Learning, veuillez suivre les protocoles de tests ci-dessous.

1. Test Manuel via l'Interface Web
Ouvrez votre navigateur et accédez à : http://3.92.26.161/predict/

Saisissez les valeurs de test suivantes dans le formulaire :

Cylindres : 8

Cylindrée (Displacement) : 307.0

Puissance (Horsepower) : 130.0

Poids (Weight) : 3500.0

Accélération : 12.0

Année du modèle : 70 (Pour 1970)

Origine : USA (ou 1)

Cliquez sur le bouton "Prédire la consommation".

Résultat attendu : L'interface doit afficher une valeur de prédiction réaliste (généralement comprise entre 15.0 et 25.0 MPG pour ce profil de véhicule) sans rechargement lourd ou erreur 500.
