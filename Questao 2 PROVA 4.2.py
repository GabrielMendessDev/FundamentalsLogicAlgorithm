a=8
b=2
c=10
d=2


v=range(a)
temp=v[b:c:d]
s=0

for n in temp:
    s=s+n
    print(s)
