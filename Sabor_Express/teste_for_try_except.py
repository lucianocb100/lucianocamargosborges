encomendas = []

encomenda = input("Adicione uma encomenda: ")
encomendas.append(encomenda)

try:
    for encomenda in encomendas:
        print(f'Encomenda {int(encomenda)} armazenada com sucesso!')
except ValueError:
    print(f'Erro de tipo de dados com a encomenda {encomenda}!')