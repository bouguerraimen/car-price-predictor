# 🚗 AutoPrix: Used Car Price Prediction

A beginner-friendly machine learning project that predicts the resale price of a used car from features such as fuel type, kilometers driven, year, and seller type. The project covers data exploration, visualization, linear regression, and a web app.

🔗 [Try the live app](https://car-price-predictor-gs4apphxmzrdrqtpxbtygni.streamlit.app/)

## Problem
Estimate the resale price of a used car from its characteristics.

## Data
CarDekho dataset (Kaggle): used cars from the Indian market, from 2003 to 2018. Features used: `Year`, `Present_Price`, `Kms_Driven`, `Fuel_Type`, `Seller_Type`, `Transmission`, `Owner`. Prices are converted to TND (Tunisian dinar) for indicative purposes only.

## Method
1. Data cleaning and exploration
2. Encoding of categorical variables
3. Linear regression
4. Evaluation with R² and MAE
5. Web app built with Streamlit

## Results
- R² (test): to be completed
- MAE: to be completed

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Limitations
- The data comes from the Indian market, so the estimate in TND is only indicative.
- The model is trained on cars from 2003 to 2018.
