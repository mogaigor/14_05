codice_correto = 232346
tentativi = 0
massimo_tentativi = 3
accesso_concesso = False

while tentativi < massimo_tentativi:
    codice_inserito = input("Inserisci il codice per aprire la porta: ")
    
    if len(codice_inserito) != 6:
        print("Il codice deve essere composto da 6 cifre")
    elif int(codice_inserito) == codice_correto:
        print("Porta aperta")
        accesso_concesso = True
        break
    else:
        print("Codice errato")
    
    tentativi += 1

if tentativi == massimo_tentativi and not accesso_concesso:
    print("Tentativi esauriti. Impossibile accedere.")