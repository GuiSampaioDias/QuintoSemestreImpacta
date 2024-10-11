def obter_peso_ideal(altura, sexo):
    if sexo != 'M' and sexo != 'F':
        return 'valor inválido'
    if altura < 1 or altura > 2.5:
        return 'Altura inválida'      

    if sexo == 'M':
        return (72.7 * altura) - 58
    else:
        return (62.1 * altura) - 44.7
    