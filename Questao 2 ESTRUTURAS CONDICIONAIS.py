n1=input('Nome do primeiro usuário:')
idade1=int(input('Idade do primeiro usuário:'))
n2=input('Nome do segundo usuário:')
idade2=int(input('Idade do segundo usuário:'))

if (idade1>=idade2):
    print("A diferença de idade entre {} e {} é:".format(n1,n2), (idade1-idade2))
if (idade1<idade2):
    print("A diferença de idade entre {} e {} é:".format(n1,n2), (idade2-idade1))
