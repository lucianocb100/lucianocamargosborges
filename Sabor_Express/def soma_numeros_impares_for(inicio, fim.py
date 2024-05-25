# Função para calcular a média dos valores em uma lista
def calcular_media(lista):
    try:
        # Verifica se a lista está vazia
        if len(lista) == 0:
            raise ZeroDivisionError("A lista está vazia. Não é possível calcular a média.")
        
        # Calcula a média dos valores na lista
        soma = sum(lista)
        media = soma / len(lista)
        return media
    except ZeroDivisionError as e:
        print(e)
        return None

# Exemplo de uma lista de números
valores = [10, 20, 30, 40, 50]

# Calcula e imprime a média dos valores na lista
media = calcular_media(valores)
if media is not None:
    print("A média dos valores na lista é:", media)