a=int(input("Digite um número:"))
b=int(input("Digite um número:"))
c=int(input("Digite um número:"))

#delta
delta=(b**2)-(4*a*c)

#x 1 linha
x1=-b+(delta**(1/2))
x1r=x1/(2*a)

#x 2 linhas
x2=-b-(delta**(1/2))
x2r=x2/(2*a)

if(delta>=0):
    print("As raízes da equação são {} e {}:".format(x1r,x2r))
else:
    print("Não tem raíz para a equação.")


