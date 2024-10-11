def calcular_area_trapezio(B,b,h):
    if B <= 0 or b <= 0 or h <= 0:
        raise ValueError
    
    elif type(B)== str or type(b) == str or type(h) == str:
        raise TypeError
    else:
        area = (B + b) * h / 2
        return area