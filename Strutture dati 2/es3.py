def converti_in_dollari(euro):
    return round(euro / 0.89, 2)

prezzi_in_dollari = list(map(lambda cliente: {**cliente, "euro": converti_in_dollari(cliente["euro"])}, clienti))
print("Prezzi convertiti in dollari:", prezzi_in_dollari)
