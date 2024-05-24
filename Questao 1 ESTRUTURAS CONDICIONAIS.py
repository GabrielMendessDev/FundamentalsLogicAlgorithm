nome1= input("Nome do primeiro usuário:")
idade1= input("Idade do primeiro usuário:")
nome2= input("Nome do segundo usuário:")
idade2= input("Idade do segundo usuário:")

if (idade1>idade2):
    print("O usuário mais velho é:", nome1)
    print("O usuário mais novo é:", nome2)
if (idade2>idade1):
    print("O usuário mais velho é:", nome2)
    print("O usuário mais novo é:", nome1)
