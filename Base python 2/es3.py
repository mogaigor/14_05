peso_totale = 0
peso_max = 9000  

while True:
    peso = int(input("Inserisci il peso del capo in grammi (0 per terminare): "))
    
    if peso == 0:
        break
    if peso_totale + peso > peso_max:
        print("Errore: il peso totale supera i 9 kg.")
    else:
        peso_totale += peso

print(f"Il peso totale dei capi è: {peso_totale} grammi")