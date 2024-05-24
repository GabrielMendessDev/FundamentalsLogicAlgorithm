dia=int(input("Digite o dia de 1 até 30:"))
mes=int(input("Digite o mês de 1 até 12:"))

#Estação outono
if(mes>=3) and (mes<=6):
    if(mes==3) and (dia>=20):
        print("De acordo com a data informada, estamos na estação outono.")
    elif(mes==6) and (dia<=20):
        print("De acordo com a data informada, estamos na estação outono.")
    elif(mes==4) or (mes==5):
        print("De acordo com a data informada, estamos na estação outono.")

#Estação inverno
if(mes>=6) and (mes<=9):
    if(mes==6) and (dia>=21):
        print("De acordo com a data informada, estamos na estação inverno.")
    elif(mes==9) and (dia<=21):
        print("De acordo com a data informada, estamos na estação inverno.")
    elif(mes==7) or (mes==8):
        print("De acordo com a data informada, estamos na estação inverno.")

#Estação primavera
if(mes>=9) and (mes<=12):
    if(mes==9) and (dia>=22):
        print("De acordo com a data informada, estamos na estação primavera.")
    elif(mes==12) and (dia<=20):
        print("De acordo com a data informada, estamos na estação primavera.")
    elif(mes==10) or (mes==11):
        print("De acordo com a data informada, estamos na estação primavera.")

#Estação verão
if(mes>=12) or (mes<=3):
    if(mes==12) and (dia>=21):
        print("De acordo com a data informada, estamos na estação verão.")
    elif(mes==3) and (dia<=19):
        print("De acordo com a data informada, estamos na estação verão.")
    elif(mes==1) or (mes==2):
        print("De acordo com a data informada, estamos na estação verão.")
    
