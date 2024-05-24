num1=input("Digite um número:")
num2=input("Digite um número:")
num3=input("Digite um número:")

if(num1>num2) and (num1>num3):
    print('O número maior é:', num1)
elif (num2>num1) and (num2>num3):
    print('O número maior é:', num2)
else:
    print('O número maior é:', num3)

#Número menor
if(num1<num2) and (num1<num3):
    print('O número menor é:', num1)
elif(num2<num1) and (num2<num3):
    print('O número menor é:', num2)
else:
    print('O número menor é:', num3)
