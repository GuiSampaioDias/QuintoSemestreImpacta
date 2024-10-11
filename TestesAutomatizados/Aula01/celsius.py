def converte_para_celsius(fahrenheit):
    celsius = (5.0/9.0) * (fahrenheit - 32)
    return celsius

def converte_para_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius +32
    return fahrenheit

def main():
    #teste 1
    numero = 0
    try:
        fahrenheit = 32
        numero += 1
        resultado = converte_para_celsius(fahrenheit)
        assert resultado == 0
        print(f'Teste{numero}: Correto ')

    except AssertionError:
        print(f'Teste{numero}: calculo  Errado!')

#teste 2
    try:
        fahrenheit = 27
        numero += 1
        resultado = converte_para_celsius(fahrenheit)
        assert resultado == 80.6
        print(f'Teste{numero}: Correto ')

    except AssertionError:
        print(f'Teste{numero}: calculo  Errado!')

    #teste 3
    try:
        celsius = 0
        numero += 1
        resultado = converte_para_fahrenheit(celsius)
        assert resultado == 32
        print(f'Teste{numero}: Correto ')

    except AssertionError:
        print(f'Teste{numero}: calculo  Errado!')

#teste 3
    try:
        celsius = 41
        numero += 1
        resultado = converte_para_fahrenheit(celsius)
        assert resultado == 5
        print(f'Teste{numero}: Correto ')

    except AssertionError:
        print(f'Teste{numero}: calculo  Errado!')

    

main()