nota1=int(input("Digite a primeira nota:"))
nota2=int(input("Digite a segunda nota:"))
nota3=int(input("Digite a terceira nota:"))
nota4=int(input("Digite a quarta nota:"))
nota5=int(input("Digite a quinta nota:"))
nota6=int(input("Digite a sexta nota:"))
nota7=int(input("Digite a sétima nota:"))
nota8=int(input("Digite a oitava nota:"))
nota9=int(input("Digite a nona nota:"))
nota10=int(input("Digite a décima nota:"))
print("-")
lista_notas=[nota1,nota2,nota3,nota4,nota5,nota6,nota7,nota8,nota9,nota10]

media=(nota1+nota2+nota3+nota4+nota5+nota6+nota7+nota8+nota9+nota10)/10
print("A média calculada de acordo com os números recebidos é de {}.".format(media))
print("-")
lm= []
for n in range (0,len(lista_notas)):
    if lista_notas[n]>media:
        lm.append(lista_notas[n])
print("Números acima da média:",lm)
print("-")
ln= []
for m in range (0,len(lista_notas)):
    if lista_notas[m]<media:
        ln.append(lista_notas[m])
print("Números abaixo da média:",ln)
    
