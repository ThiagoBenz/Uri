const = 100
vetor = [0] * (const+1)
for i in range(const):
    aux = float(input())
    vetor [i] = aux

for i in range(const):
    aux = float(vetor[i])
    if aux <= 10:
        print("A[{}] = {}".format(i, aux))