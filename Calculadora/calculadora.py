
print("***** Python Calculator *****")


print("Selecione o número da operação desejada:")

print(" 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão")

calculoz = int(input("Digite sua opção (1/2/3/4 :"))

while((calculoz != 1) and (calculoz != 2) and (calculoz != 3) and (calculoz != 4)):
    calculoz = int(input("Digite sua opção (1/2/3/4 :"))


numero1 = int(input("Escolha o primeiro numero: "))


numero2 = int(input("Escolha o segundo numero:  "))



if (calculoz == 1):
    print("{} + {} = ".format(numero1 , numero2)) 
    print(numero1 + numero2)
    
elif(calculoz == 2):
    print("{} - {} = ".format(numero1 , numero2)) 
    print(numero1 - numero2)

elif(calculoz == 3):
    print("{} * {} = ".format(numero1 , numero2)) 
    print(numero1 * numero2)

elif(calculoz == 4):
    print("{} / {} = ".format(numero1 , numero2)) 
    print(numero1 / numero2)
