clienti = []

print("Benvenuto! Inserisci i dati dei clienti. Digita '999999' come codice cliente per terminare.")

while True:
    try:
        codice = int(input("Inserisci il codice cliente (999999 per terminare): "))
        if codice == 999999:
            break
        kg = float(input("Inserisci i kg lavati: "))
        euro = float(input("Inserisci gli euro pagati: "))
        clienti.append({"codice": codice, "kg": kg, "euro": euro})
    except ValueError:
        print("Errore: Inserisci un valore valido.")
        continue

if clienti:
    totale_kg = sum(cliente["kg"] for cliente in clienti)
    media_kg = totale_kg / len(clienti)
    totale_euro = sum(cliente["euro"] for cliente in clienti)
    massimo_pagato = max(cliente["euro"] for cliente in clienti)
    clienti_massimo = [cliente["codice"] for cliente in clienti if cliente["euro"] == massimo_pagato]

    print("\n--- Riepilogo della giornata ---")
    print(f"Totale kg lavati: {totale_kg}")
    print(f"Media kg lavati per cliente: {media_kg:.2f}")
    print(f"Totale pagato dai clienti: {totale_euro:.2f}")
    print(f"Cliente/i che ha/hanno pagato di più: {', '.join(map(str, clienti_massimo))}")

  


