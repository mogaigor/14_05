
def converti_in_dollari(euro):
        tasso_conversione = 0.89
        return euro / tasso_conversione

clienti_in_dollari = list(map(lambda cliente: {
    "codice": cliente["codice"],
    "kg": cliente["kg"],
    "euro": cliente["euro"],
    "dollari": converti_in_dollari(cliente["euro"])
}, clienti))

print("--- Clienti con prezzi in dollari ---")
for cliente in clienti_in_dollari:
        print(f"Codice: {cliente['codice']}, Kg: {cliente['kg']}, Euro: {cliente['euro']}, Dollari: {cliente['dollari']}")
else:
    print("Nessun cliente registrato oggi.")
