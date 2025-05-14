codice_correto = 232346

codice_inserito = input("Inserisci il codice per aprire la porta: ")

if len(codice_inserito) != 6:
    print("Il codice deve essere composto da 6 cifre")
elif int(codice_inserito) == codice_correto:
    print("Porta aperta")
else:
    print("Codice errato")