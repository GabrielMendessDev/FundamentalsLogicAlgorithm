v=float(input("Digite a velocidade atual do veículo(Km/h):"))
m=100+(v-80)*7
if (v>=80):
    print("Você ultrapassou os padrões de velocidade permititos! Sua multa é de: R${}".format(m), "reais")
if(v<80):
    print("Você está dentro dos padrões de velocidade permitidos, tenha um bom dia!")
