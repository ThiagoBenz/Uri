quantidade = int(input())

for i in range(quantidade):
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])
    if y == 0:
        print("divisao impossivel")
    else:
        print("{:.1f}".format(x/y))