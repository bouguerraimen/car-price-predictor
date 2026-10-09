import streamlit as st
import pandas as pd
import joblib

TAUX_INR_TND = 0.035   # 1 roupie = 0,035 TND (à mettre à jour)

st.set_page_config(page_title="AutoPrix", page_icon="🚗", layout="centered")

# ---------- Design (CSS) ----------
st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(160deg, #0B1220 0%, #121C35 100%); }
    header[data-testid="stHeader"] { background: transparent; }
    .block-container { padding-top: 3rem; max-width: 760px; }

    .hero { text-align: center; margin-bottom: 2rem; }
    .hero h1 {
        font-size: 3rem; font-weight: 800; margin: 0;
        background: linear-gradient(90deg, #22D3EE, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero p { color: #94A3B8; margin-top: 0.5rem; font-size: 1.05rem; }

    [data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 1.8rem;
    }

    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(90deg, #22D3EE, #6366F1);
        color: #0B1220; border: none; border-radius: 12px;
        padding: 0.7rem 1.5rem; font-weight: 700; width: 100%;
        transition: transform 0.15s ease;
    }
    div[data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-2px); color: #0B1220;
    }

    .resultat {
        margin-top: 1.5rem; padding: 2rem; text-align: center;
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(34,211,238,0.15), rgba(99,102,241,0.15));
        border: 1px solid rgba(34, 211, 238, 0.35);
    }
    .resultat .label { color: #94A3B8; font-size: 0.95rem; letter-spacing: 0.05em; text-transform: uppercase; }
    .resultat .montant { color: #22D3EE; font-size: 3.2rem; font-weight: 800; line-height: 1.2; }
    .resultat .montant span { font-size: 1.2rem; color: #94A3B8; font-weight: 500; }

    .pied { text-align: center; color: #64748B; font-size: 0.85rem; margin-top: 2.5rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Chargement ----------
@st.cache_resource
def charger():
    return joblib.load("model.joblib"), joblib.load("columns.joblib")

model, columns = charger()

# ---------- En-tête ----------
st.markdown(
    """
    <div class="hero">
        <h1>🚗 AutoPrix</h1>
        <p>Estime le prix de revente de ta voiture d'occasion en quelques secondes</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Formulaire ----------
with st.form("formulaire"):
    c1, c2 = st.columns(2)
    year = c1.number_input("Année", min_value=2003, max_value=2018, value=2014)
    present_tnd = c2.number_input("Prix neuf (TND)", min_value=1000, max_value=300000,
                                  value=21000, step=500)

    c3, c4 = st.columns(2)
    kms = c3.number_input("Kilométrage (km)", min_value=0, max_value=500000,
                          value=40000, step=1000)
    owner = c4.selectbox("Propriétaires précédents", [0, 1, 3])

    c5, c6, c7 = st.columns(3)
    fuel = c5.selectbox("Carburant", ["Petrol", "Diesel", "CNG"])
    seller = c6.selectbox("Vendeur", ["Dealer", "Individual"])
    transmission = c7.selectbox("Boîte", ["Manual", "Automatic"])

    envoyer = st.form_submit_button("Estimer le prix")

# ---------- Résultat ----------
if envoyer:
    # TND -> lakhs ₹ (le modèle a été entraîné en lakhs)
    present_price = present_tnd / TAUX_INR_TND / 100000

    X_new = pd.DataFrame([{
        "Year": year,
        "Present_Price": present_price,
        "Kms_Driven": kms,
        "Fuel_Type": fuel,
        "Seller_Type": seller,
        "Transmission": transmission,
        "Owner": owner,
    }])

    # Même encodage qu'à l'entraînement
    X_new = pd.get_dummies(X_new)
    X_new = X_new.reindex(columns=columns, fill_value=0).astype(float)

    prix_lakhs = max(model.predict(X_new)[0], 0)      # sortie du modèle (interne)
    prix_tnd = prix_lakhs * 100000 * TAUX_INR_TND     # lakhs -> roupies -> TND
    montant_tnd = f"{prix_tnd:,.0f}".replace(",", " ")

    st.markdown(
        f"""
        <div class="resultat">
            <div class="label">Prix de revente estimé</div>
            <div class="montant">{montant_tnd} <span>TND</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

