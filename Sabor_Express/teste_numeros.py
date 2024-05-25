numero = int(input('Digite um número? '))

if numero % 2 == 0:
    print('O numero é par')
else:
        print('O numero é ímpar')
    
idade = int(input("Qual é a sua idade? "))

if idade>0 & idade<=12:
    print("Você é uma criança")
elif idade>13 & idade<=18:
    print("Você é um adolescente")
else:
    print("Você é um adulto")

user = str(input("\nDigite o seu usuário? "))
password = str(input("\nDigite a sua senha? "))
user_correto = str("luciano.borges")
password_correto = str("Scala@1234")

if user == user_correto and password == password_correto:
    print("Usuário e senha corretos!")
else:
     print("Usuário e senha incorretos...")


x = float(input("Digite a coordenada x do ponto: "))
y = float(input("Digite a coordenada y do ponto: "))

if x==0 and y==0:
    print("O ponto se encontra no 1º quadrante")
elif x<0 and y>0:
    print("O ponto se encontra no 2º quadrante")
elif x<0 and y<0:
    print("O ponto se encontra no 3º quadrante")
elif x>0 and y<0:
    print("O ponto se encontra no 4º quadrante")
else:
    print("O ponto se encontra no eixo (ou origem)")