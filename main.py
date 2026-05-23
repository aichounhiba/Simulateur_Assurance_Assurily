{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dfadc34a-3d47-4be7-9741-95c28e8aac7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fichier : main.py\n",
    "from fastapi import FastAPI\n",
    "from tarification import calculer_prime_auto\n",
    "\n",
    "# Création de l'application FastAPI\n",
    "app = FastAPI(title=\"API Tarification Assurily\")\n",
    "\n",
    "@app.get(\"/\")\n",
    "def accueil():\n",
    "    return {\"message\": \"Bienvenue sur l'API de simulation d'assurance !\"}\n",
    "\n",
    "@app.post(\"/simulateur/devis\")\n",
    "def générer_devis(age: int, puissance: int, sinistres: str):\n",
    "    \"\"\"\n",
    "    Route qui reçoit les données du client et renvoie le prix calculé.\n",
    "    \"\"\"\n",
    "    # Appel de notre fonction actuarielle (Etape 2)\n",
    "    resultat = calculer_prime_auto(\n",
    "        age=age, \n",
    "        puissance_fiscale=puissance, \n",
    "        historique_sinistres=sinistres\n",
    "    )\n",
    "    \n",
    "    # Message important guidant le client vers l'agence pour la signature physique\n",
    "    message_agence = \"Votre devis est enregistré avec succès. Veuillez vous présenter dans l'agence la plus proche muni de vos documents pour finaliser et signer votre contrat définitif.\"\n",
    "    resultat[\"instruction_client\"] = message_agence\n",
    "    \n",
    "    return resultat"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
