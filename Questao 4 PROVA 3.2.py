peso=float(input("Digite seu peso(kg):"))
h=float(input("Digite sua altura(m):"))
imc=peso/(h**2)

#MUITO ABAIXO DO PESO
if(imc<17):
    print("Muito abaixo do peso")

#ABAIXO DO PESO
if(imc>=17) and (imc<=18.49):
    print("Abaixo do peso")

#PESO NORMAL
if(imc>=18.5) and (imc<=24.99):
    print("Peso normal")

#ACIMA DO PESO
if(imc>=25) and (imc<=29.99):
    print("Acima do peso")

#OBESIDADE I
if(imc>=30) and (imc<=34.99):
    print("Obesidade I")

#OBESIDADE II(SEVERA)
if(imc>=35) and (imc<=39.99):
    print("Obesidade II (severa)")

#OBESIDADE III(MÓRBIDA)
if(imc>=40):
    print("Obesidade III (mórbida)")
