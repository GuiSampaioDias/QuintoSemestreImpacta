def calcular_dosagem(idade, peso):
    if idade > 120 or idade < 1 or peso < 1 or peso > 200:
        raise ValueError
    if idade >= 12:
        if peso >= 60:
            return 1000
        else: 
            return 875
        
    else:
        if peso >= 5 and peso <= 9:
            return 125
        elif peso >= 9.1 and peso <= 16:
            return 250
        elif peso >= 16.1 and peso <= 24:
            return 375
        elif peso >= 24.1 and peso <= 30:
            return 500
        elif peso >= 30.1:
            return 750