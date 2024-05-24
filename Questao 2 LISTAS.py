lista_o=[1,1,2,3,5,8,13]
lista_1=lista_o.copy()
lista_1[1]=lista_1[1]*3
lista_1[3]=lista_1[3]*3
lista_1[5]=lista_1[5]*3

lista_2=lista_o.copy()
lista_2[0]=lista_2[0]*2
lista_2[2]=lista_2[2]*2
lista_2[4]=lista_2[4]*2
lista_2[6]=lista_2[6]*2


print("LISTA ORIGINAL:", lista_o)
print("PRIMEIRA CÓPIA:", lista_1)
print("SEGUNDA CÓPIA:", lista_2)
