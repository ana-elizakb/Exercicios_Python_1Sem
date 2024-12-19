peso = float(input('Digite o valor do seu peso:'))
altura = float(input('Figite o valor de sua altura:'))

imc = peso/altura

if (imc < 20):
    print(f"O seu imc é {imc:.2f} e vc está abaixo do peso")
elif (20 <= imc < 25):
    print(f"O seu imc é {imc:.2f} e vc está em seu peso ideal")
else:
    print(f"O seu imc é{imc:.2f} e vc está acima do peso")
