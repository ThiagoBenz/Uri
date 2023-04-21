x = int(input())
y = int(input())

soma = 0
maior = 0
menor = 0
if x > y:
    maior = x
    menor = y

if x <= y:
    maior = y
    menor = x

i = menor

while i <= maior:
    if i % 13 != 0:
        soma += i
    i += 1

print(soma)