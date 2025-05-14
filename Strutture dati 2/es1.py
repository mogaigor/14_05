clienti = []

while True:
    codice = int(input("Inserisci il codice cliente (999999 per terminare): "))
    if codice == 999999:
        break
    kg = float(input("Inserisci i kg lavati: "))
    euro = float(input("Inserisci gli euro pagati: "))
    clienti.append({"codice": codice, "kg": kg, "euro": euro})

totale_kg = sum(cliente["kg"] for cliente in clienti)
media_kg = totale_kg / len(clienti) if clienti else 0
totale_euro = sum(cliente["euro"] for cliente in clienti)
massimo_pagato = max(cliente["euro"] for cliente in clienti)
clienti_massimo = [cliente["codice"] for cliente in clienti if cliente["euro"] == massimo_pagato]


print(f"Totale kg lavati: {totale_kg}")
print(f"Media kg lavati per cliente: {media_kg:.2f}")
print(f"Totale pagato dai clienti: {totale_euro}")
print(f"Cliente/i che ha/hanno pagato di più: {clienti_massimo}")
