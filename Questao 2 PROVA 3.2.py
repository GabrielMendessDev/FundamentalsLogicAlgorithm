nota1=int(input("Digite a média do primeiro bimestre de 10 a 100:"))
nota2=int(input("Digite a média do segundo bimestre de 10 a 100:"))
nota3=int(input("Digite a média do terceiro bimestre de 10 a 100:"))
nota4=int(input("Digite a média do quarto bimestre de 10 a 100:"))

media=nota1*2+nota2*2+nota3*3+nota4*3
somap=2+2+3+3
r=media/somap

if(r>=70):
    print("O aluno está aprovado=(média:{})".format(r))
else:
    print("O aluno está reprovado=(média:{})".format(r))
