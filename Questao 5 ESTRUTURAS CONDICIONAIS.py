num1=int(input("Digite um número:"))
num2=int(input("Digite um número:"))

if num1==0 or num2==0:
     print("Não é possível dividir por 0")
elif (num1%num2==0):
     print("O número {} é divisível pelo número {}".format(num1,num2))
elif (num2%num1==0):
     print("O número {} é divisível pelo número {}".format(num2,num1))
else:
     print("Entre os números digitados, nenhum é divisível um pelo outro")
