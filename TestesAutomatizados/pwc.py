def endereco(logradouro):
    simplificado = logradouro.split()
    if len(simplificado) == 2:
        solucao = {'logradouro': simplificado[0], 'numero': simplificado[1]  }
        return solucao
        
    if 'No ' in logradouro:
        lista = logradouro.split(' No ')
        solucao = {'logradouro': lista[0], 'numero': 'No ' + lista[1]}
        return solucao

print(endereco('Calle 44 No 1991'))
print(endereco('Miritiba 339'))