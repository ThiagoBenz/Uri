resp = 1
inter = 0
gremio = 0
empate = 0
quant = 0
while resp == 1:
    entrada = input().split()
    
    if int(entrada[0]) > int(entrada[1]):
        inter += 1
    elif int(entrada[0]) < int(entrada[1]):
        gremio += 1
    else:
        empate += 1

    quant += 1

    print ("Novo grenal (1-sim 2-nao)")
    resp = int(input())
    if resp == 2:
        print (quant, "grenais")
        print ("Inter:{}".format(inter))
        print ("Gremio:{}".format(gremio))
        print ("Empates:{}".format(empate))
        if inter > gremio:
            print ("Inter venceu mais")
        elif inter < gremio:
            print ("Gremio venceu mais")
        else:
            print ("Nao houve vencedor")
        break