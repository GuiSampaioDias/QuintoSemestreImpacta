from dirigir import dirigir

def test_pode_dirigir():
    assert dirigir(18, 's') == 'Pode dirigir'

def test_nao_pode_dirigir():
    assert dirigir(2,'s') == 'Não pode dirigir'

def test_nao_pode_dirigir2():
    assert dirigir(22,'n') == 'Não pode dirigir' 