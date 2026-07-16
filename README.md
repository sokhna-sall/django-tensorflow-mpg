# 🚗 Django TensorFlow MPG Predictor (UCAD - M1ILIA)

Ce projet est une application web Django qui intègre un modèle de réseau de neurones profonds (Deep Learning) développé avec **TensorFlow/Keras** afin de prédire la consommation de carburant d'un véhicule (exprimée en MPG - Miles Per Gallon) en fonction de ses caractéristiques techniques.

---

## 🛠️ Architecture du Projet
* **Framework Web** : Django 6.0.7
* **Moteur d'IA** : TensorFlow / Keras (Modèle pré-entraîné `dnn_model.keras`)
* **Interface Utilisateur** : HTML5 / Tailwind CSS (Responsive Design)
* **Serveur de Production** : Nginx (Reverse Proxy) + Gunicorn (WSGI Server)
* **Hébergement** : Instance AWS EC2 (Debian)

---

## 🚀 Guide d'Installation et Lancement Local

1. **Cloner le projet** :
   ```bash
   git clone <url_de_votre_depot>
   cd tensorflow_django
