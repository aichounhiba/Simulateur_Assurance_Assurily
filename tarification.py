def calculer_prime_auto(age, puissance_fiscale, historique_sinistres):
    prime = 15000
    if age < 25: prime += 3000
    if historique_sinistres == "aucun": prime -= 1500
    return {"prime_base": 15000, "coefficient_total": 1.0, "prime_totale_dzd": prime, "justifications": ["Calcul simplifié"]}