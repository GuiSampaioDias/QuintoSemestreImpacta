REQUERER = 'Requerer aposentadoria'
NAO_REQUERER = 'Não requerer'

def verificar_qualificacao_empregado(idade: int, tempo_de_servico: int):
    if type(idade) != int or type(tempo_de_servico) != int: raise TypeError
    if idade <=0 or tempo_de_servico <=0: raise ValueError
    else:
        if idade >= 65:
            return REQUERER
        elif tempo_de_servico >= 30:
            return REQUERER
        elif idade >= 60 and tempo_de_servico >= 25:
            return REQUERER

        return NAO_REQUERER
   