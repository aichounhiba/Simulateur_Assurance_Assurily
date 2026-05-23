# Fichier : app.py
import streamlit as st
# On importe notre fonction de calcul actuariel de l'étape 1
from tarification import calculer_prime_auto

# Configuration de la page avec un titre sympa
st.set_page_config(page_title="simulateur-tarification-auto", page_icon="🚗", layout="centered")

# Titre principal de l'application (style épuré)
st.title("🚗 simulateur-tarification-auto")
st.write("Obtenez une estimation de votre prime d'assurance automobile en quelques clics avant de finaliser votre contrat en agence.")

st.markdown("---")

# Création du formulaire pour le client
st.subheader("📋 Informations du conducteur et du véhicule")

# 1. Case pour l'âge
age = st.number_input("Quel est votre âge ?", min_value=18, max_value=100, value=25, step=1)

# 2. Case pour la puissance du véhicule
puissance = st.number_input("Puissance fiscale de votre véhicule (en CV) :", min_value=1, max_value=30, value=7, step=1)

# 3. Menu déroulant pour les sinistres
sinistres = st.selectbox(
    "Historique de vos sinistres (accidents) au cours des 3 dernières années :",
    options=["aucun", "au_moins_un"],
    format_func=lambda x: "Aucun accident (Bonus)" if x == "aucun" else "Au moins un accident (Malus)"
)

st.markdown("---")

# Bouton pour lancer le calcul actuariel
if st.button("📊 Calculer mon devis dynamique"):
    
    # Appel de la fonction de calcul
    resultat = calculer_prime_auto(age=age, puissance_fiscale=puissance, historique_sinistres=sinistres)
    
    # Affichage du prix de manière très claire et visible
    st.success(f"### Tarification Estimée : {resultat['prime_totale_dzd']:,} DZD / an")
    
    # Affichage du détail des calculs (les justifications)
    st.write("**Détails de l'analyse du risque :**")
    for justification in resultat['justifications']:
        st.write(f"- {justification}")
        
    # Rappel de la règle métier (très important pour votre projet !)
    st.warning(f"💡 **Note importante :** {resultat['prime_base']} DZD est la prime de base. Votre coefficient total est de {resultat['coefficient_total']}. Ce devis est une simulation. Veuillez vous présenter dans l'agence la plus proche pour valider vos documents et signer votre contrat physique définitif.")
