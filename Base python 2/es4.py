def converti(kg, tasso_conversione):
    return round(kg / tasso_conversione, 2)

# Esempio di uso:
kg = 8
libbre = converti(kg, 0.453592)
print(f"{kg} kg equivalgono a {libbre} libbre")