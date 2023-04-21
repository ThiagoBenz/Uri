x = list(map(int, input().split()))
i = 1
soma = 0

while x[i] <= 0:
    if x[i] <=0:
        i = i + 1
        
    if x[i] > 0:
        break

for aux in range(0,x[i]):
    soma = soma + x[0] + aux
   
print(soma) 