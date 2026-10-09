# 🚗 AutoPrix : prédiction du prix de voitures d'occasion

🔗 **[Essayer l'application en ligne]([https://TON_LIEN.streamlit.app](https://car-price-predictor-gs4apphxmzrdrqtpxbtygni.streamlit.app/))**

![Capture d'écran](capture.png)

## Problème
Estimer le prix de revente d'une voiture d'occasion à partir de ses caractéristiques.

## Données
CarDekho (Kaggle) : voitures d'occasion du marché indien, 2003 à 2018.
Prix convertis en TND à titre indicatif.

## Méthode
Nettoyage, encodage, régression linéaire, évaluation (R², MAE), application Streamlit.

## Résultats
R² (test) : X · MAE : X

## Lancer en local
pip install -r requirements.txt
streamlit run app.py
