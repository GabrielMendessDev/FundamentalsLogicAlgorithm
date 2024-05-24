num=int(input("Digite algum número para descobrir o fatorial dele:"))
vetorial=1
for n in range(num,0,-1):
    vetorial= vetorial*n
print("Fatorial do número ({}!) = {}.".format(num,vetorial))
