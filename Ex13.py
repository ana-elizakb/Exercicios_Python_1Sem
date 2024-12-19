n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
n3 = float(input("Digite o terceiro número:"))

if (n1 > n2):
    if (n1 > n3):
        print ('O maior núemero' ,n1)
    else: 
        print('O maior número é' ,n3)
elif(n2>n3):    
    print ("O maior número é:",n2)
else:
    print("O maior núemro é:",n3)