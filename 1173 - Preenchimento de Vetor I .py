const = 10
vetor = [0] * (const+1)
vetor[0] = int(input())

for i in range(const):
    print("N[{}] = {}".format(i, vetor[i]))
    aux = vetor[i]*2
    if i+1 < const:
        vetor[i+1] = aux
