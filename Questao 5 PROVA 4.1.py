qv=int(input("Digite a quantidade de veículos:"))
codigo=int(input("Digite o código de bloqueio de 0 à 9:"))
l=[]

for n in range(qv,0,-1):
    placa=(input("Digite o número da placa - (ex:9873):"))
    l.append(placa)

for i in range(0,len(l)):
    if int((l[i])[-1])==codigo:
        print("Veículo pribido de rodar. Número da placa: {}".format(l[i]))
    else:
        print("Veículo liberado de rodar. Número da placa: {}".format(l[i]))


