nome=input("Digite seu nome:")
saque=float(input("Digite o valor do saque:"))
saldo=3000.00
vf=saldo-saque

if(saque<=saldo):
    print("Saque efetuado com sucesso. Valor restante da conta: {}".format(vf))
else:
    print("Não foi possível realizar o saque. Tente com um valor menor.")
