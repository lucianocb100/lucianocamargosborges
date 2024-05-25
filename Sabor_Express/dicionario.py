dict = {'nome': 'Luciano',
        'idade': 30,
        'cidade': 'Osasco'}

dict['idade'] = 31
dict['profissao'] = 'data_scientist'
del dict['cidade']

print(dict)

def chave(arg):
    if arg in dict:
        print(f'A chave {arg} existe no dicionário')
    else:
        print(f'A chave {arg} não existe no dicionário')

chave('casa')

def frequencia_frase(frase):
    palavras = frase.split()
    frequencia_palavras = {}

    for palavra in palavras:
        if palavra in  frequencia_palavras:
            frequencia_palavras = 1
        else:
            frequencia_palavras[palavra] = 1

    for palavra, frequencia in  frequencia_palavras.items():
        print(f'A palavra {palavra} aparece {frequencia} vezes na frase')

frequencia_frase('O Cruzeiro é o maior time de Minas Gerais e isto é fato!')