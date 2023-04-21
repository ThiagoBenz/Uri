casos = int(input())
i = 0
totalDeCobaias = 0
quant = 0
coelho = 0
rato = 0
sapo = 0
animal = ""
entrada = []
for i in range (0,casos):
    entrada = input().split()

    quant, animal = entrada
    quant = int(quant)
    del entrada

    if animal == "C":
        coelho += quant
    elif animal == "R":
        rato += quant
    elif animal == "S":
        sapo += quant
    
    totalDeCobaias += quant

print("Total: {} cobaias".format(totalDeCobaias))
print("Total de coelhos: {}".format(coelho))
print("Total de ratos: {}".format(rato))
print("Total de sapos: {}".format(sapo))
print("Percentual de coelhos: {:.2f} %".format((coelho/totalDeCobaias)*100))
print("Percentual de ratos: {:.2f} %".format((rato/totalDeCobaias)*100))
print("Percentual de sapos: {:.2f} %".format((sapo/totalDeCobaias)*100))

