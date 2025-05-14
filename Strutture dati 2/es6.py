import random

numeri_vincita = random.sample(range(100000, 999999), 100)
codice_cliente = int(input("Inserisci il tuo codice cliente: "))

if codice_cliente in numeri_vincita:
    print("Hai vinto!")
else:
    print("Mi dispiace, non hai vinto.")