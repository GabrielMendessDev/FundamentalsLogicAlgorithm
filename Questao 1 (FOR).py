print("Contagem regressiva -- Fogos de Artifício")
for n in range (10,-1,-1):
    if(n==5):
        v=input("Deseja pausar a contagem? Se sim, digite P ou p. Se não, digite Não.")
        if (v=='P') or (v=='p'):
            print("Contagem pausada")
            break
    print(n)

if(v!='P') and (v!='p'):
        print("Os fogos foram estourados!")

    
    
    
        
    
