entrada = []
const = 10
for i in range(const):
    entrada.append(int(input()))

for i in range(const):
    if entrada[i] <= 0:
        entrada[i] = 1
    print("X[{}] = {}".format(i, entrada[i] ))