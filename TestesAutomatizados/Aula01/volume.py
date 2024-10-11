def calcula_volume(comprimento, largura, altura):
    return comprimento * largura * altura


def main():
    numero = 0
    #teste 1
    try:
        comprimento = 1
        largura = 1
        altura = 1
        numero += 1
        resultado = calcula_volume(comprimento, largura, altura)
        assert resultado == 1
        print(f'Teste{numero}:  {comprimento} x {largura} x {altura} resultado esperado {resultado}')

    except AssertionError:
        print(f'Teste{numero}: calculo  Errado!')

    #teste 2
    try:
        comprimento = 2
        largura = 4
        altura = 3
        numero += 1
        resultado = calcula_volume(comprimento, largura, altura)
        assert resultado == 24
        print(f'Teste{numero}:  {comprimento} x {largura} x {altura} resultado esperado {resultado}')

    except AssertionError:
        print(f'Teste{numero}: calculo  Errado!')

    #teste 3
    try:
        comprimento = 5
        largura = 5
        altura = 2
        numero += 1
        resultado = calcula_volume(comprimento, largura, altura)
        assert resultado == 100
        print(f'Teste{numero}:  {comprimento} x {largura} x {altura} resultado esperado {resultado}')

    except AssertionError:
        print(f'Teste{numero}: calculo  Errado!')

main()