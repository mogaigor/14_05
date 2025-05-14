def calcola_resto(prezzo, banconota):
    resto = banconota - prezzo
    euro = int(resto)
    centesimi = round(resto - euro, 2)
    return (euro, centesimi)
