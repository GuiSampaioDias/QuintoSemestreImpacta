def triangulo(a,b,c):
    if type(a) != float and type(a) != int:
        raise TypeError()
    if type(b) != float and type(b) != int:
        raise TypeError()
    if type(c) != float and type(c) != int:
        raise TypeError()
    
    if a < b + c and b < a + c and c < a + b:
        if a == b  and b == c:
            return 'Triângulo Equilátero'
        elif a == b or a == c or b == c:
            return 'Triângulo Isóceles'
        else:
            return 'Triângulo Escaleno'
    else:
        return 'Não é um triângulo'