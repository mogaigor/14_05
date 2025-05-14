def calcola_costo(peso, temperatura):
    if temperatura not in [40, 60, 90]:
        return "Temperatura non valida"
    
    if peso < 5:
        if temperatura == 40:
            return peso * 0.50
        elif temperatura == 60:
            return peso * 0.75
        elif temperatura == 90:
            return peso * 1.00
    else:
        if temperatura == 40:
            return peso * 0.75
        elif temperatura == 60:
            return peso * 1.00
        elif temperatura == 90:
            return peso * 1.50