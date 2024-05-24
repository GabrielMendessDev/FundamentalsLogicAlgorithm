a = 0
l = []
while a == 0:
    b = int(input ("Digite um número:"))
    l.append(b)
    if b == 0:
         break

lista=l
print("Lista original:",lista)
lista.sort()
print("Lista crescente:",lista)
lista.reverse()
print("Lista decrescente:",lista)


