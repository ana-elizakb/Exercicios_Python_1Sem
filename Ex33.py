valores = []

valor = int(input("Defina um valor de 1 a 20: "))

if(valor > 20 or valor < 1):
    valor = int(input("Erro! valor máximo é 20. Por favor defina novamente: "))

for i in range(valor):
    num = int(input("Digite um número: "))
    valores.append(num)

print(valores)
v = int(input("Escreva um número: "))



for v in valores:
        print(v)

   