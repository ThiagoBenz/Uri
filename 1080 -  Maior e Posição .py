cont = 0
num = 0
maior = 0
posicao = 1
while cont <100:
    num = int(input())
    if num > maior:
        maior = num
        posicao = cont + 1
    cont += 1

print(maior)
print(posicao)