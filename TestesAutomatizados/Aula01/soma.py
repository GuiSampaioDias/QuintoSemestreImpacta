def soma(a,b):
    return(a + b)

def main():
    numero = 0
    #teste 1
    try:
        numero += 1
        resultado = soma(10, 20)
        assert resultado == 30
        print(f'Teste{numero}: Soma Correta')

    except AssertionError:
        print(f'Teste{numero}: Errada!')

    #teste 2
    try:
        numero += 1
        resultado = soma(4, 20)
        assert resultado == 24
        print(f'Teste{numero}: Soma Correta')

    except AssertionError:
        print(f'Teste{numero}: Soma Errada!')


    #teste 2
    try:
        numero += 1
        resultado = soma(18, 20)
        assert resultado == 38
        print(f'Teste{numero}: Soma Correta')

    except AssertionError:
        print(f'Teste{numero}: Soma Errada!')

main()