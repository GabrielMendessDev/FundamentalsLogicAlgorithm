a = 0
l = []
while a == 0:
    b = int(input ("Digite um número:"))
    l.append(b)
    if b == 0:
         break

lmaior = []
for i in range (0, len(l)):
        if l[i] > 0:
                lmaior.append(l[i])

lmenor = []
for i in range (0, len(l)):
        if l[i] < 0:
                lmenor.append(l[i])

print("A quantidade de números positivos é de",len(lmaior))
print("A quantidade de números negativos é de",len(lmenor))
