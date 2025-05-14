def clienti_con_piu_di_5kg(clienti):
    return [cliente["codice"] for cliente in clienti if cliente["kg"] > 5]

print("Clienti che hanno lavato più di 5 kg:", clienti_con_piu_di_5kg(clienti))
