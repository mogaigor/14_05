def modifica(clienti, codice, nuovi_kg, nuovi_euro):
    for cliente in clienti:
        if cliente["codice"] == codice:
            cliente["kg"] = nuovi_kg
            cliente["euro"] = nuovi_euro
            return True
    return False

codice_cliente = int(input("Inserisci il codice cliente da modificare: "))
nuovi_kg = float(input("Inserisci i nuovi kg: "))
nuovi_euro = float(input("Inserisci i nuovi euro: "))
if modifica(clienti, codice_cliente, nuovi_kg, nuovi_euro):
    print("Modifica effettuata con successo.")
else:
    print("Cliente non trovato.")
