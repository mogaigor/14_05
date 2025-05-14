cliente1 = [3, 5, 6, 18, 19, 23, 30]
cliente2 = [1, 5, 6, 18, 20, 23, 30]
cliente3 = [2, 5, 6, 18, 19, 23, 30]

tutti_presenti = set(cliente1) & set(cliente2) & set(cliente3)
nessuno_presente = set(range(1, 31)) - (set(cliente1) | set(cliente2) | set(cliente3))
almeno_uno_presente = set(cliente1) | set(cliente2) | set(cliente3)

print("Giorni in cui si sono presentati tutti e tre i clienti:", tutti_presenti)
print("Giorni in cui non si è presentato nessuno:", nessuno_presente)
print("Giorni in cui si è presentato almeno uno:", almeno_uno_presente)
