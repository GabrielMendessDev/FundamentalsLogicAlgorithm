num=int(input("Digite o número que você deseja saber se está na lista:"))
lista=[0,1,2,1,3,4,9,11,2,2]
v=lista.count(num)
print("-")
print("-")
if(num in lista):
    print("O número {} está na lista. A quantidade de vezes que ele apareceu foi: {} vezes".format(num,v))
else:
    print("O número {} não está na lista.".format(num))
