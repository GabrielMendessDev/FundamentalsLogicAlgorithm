num=int(input("Digite um número:"))
total=0
for n in range (1, num + 1):
 if (num % n == 0):
         total= total + 1
         print("o número é divisível por:", n)
print("O número {} pôde ser dividido {} vezes".format(num, total))
if total == 2:
        print("Portanto, ele é primo.")
else:
        print("Portanto, ele não é primo.")
    
