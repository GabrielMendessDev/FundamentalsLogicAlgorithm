print("Escolha um dos códigos abaixo:")
print("Código: CB --- Chá: Chá de Boldo --- Valor: R$ 1,50")
print("Código: CV --- Chá: Chá Verde --- Valor: R$ 1,65")
print("Código: CP --- Chá: Chá Preto --- Valor: R$ 1,99")
print("Código: CE --- Chá: Chá de Ervas --- Valor: R$ 1,00")
print("Código: CM --- Chá: Chá Mate --- Valor: R$ 1,99")
print("-")

a=True

while(a):
    codigo=(input("Digite o código do chá desejado:"))
    if(codigo == 'CB'):
        a=False
        nome= 'Chá de Boldo'
        preco=1.50
    elif(codigo == 'CV'):
        a=False
        nome='Chá Verde'
        preco=1.65
    elif(codigo == 'CP'):
        a=False
        nome='Chá Preto'
        preco=1.99
    elif(codigo == 'CE'):
        a=False
        nome='Chá de Ervas'
        preco=1.00
    elif(codigo == 'CM'):
        a=False
        nome='Chá Mate'
        preco=1.99

quantidade=int(input("Digite a quantidade desejada:"))
print("Código digitado: {} -- Quantidade escolhida: {}".format(codigo,quantidade))

conta=quantidade*preco

if (codigo == 'CB'):
    print("Valor unitário: R$ 1,50 --- Valor total:","R$",conta, "reais")
elif(codigo == 'CV'):
    print("Valor unitário: R$ 1,65 --- Valor total:","R$",conta, "reais")
elif(codigo == 'CP'):
    print("Valor unitário: R$ 1,99 --- Valor total:","R$",conta, "reais")
elif(codigo == 'CE'):
    print("Valor unitário: R$ 1,00 --- Valor total:","R$",conta, "reais")
elif(codigo == 'CM'):
    print("Valor unitário: R$ 1,99 --- Valor total:","R$",conta, "reais")
    
