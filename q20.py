arq = input("Nome do arquivo: ")

lis = []

g = open(arq, "r")

for l in g:
    lis.append(list(l.strip().split(" ")))

g.close()

linhas = []

for i in range(int(lis[0][0])):
    linhas.append(list("1" * int(lis[0][1])))

for j in range(1,int(lis[0][2])+1):
    linhas[int(lis[j][0])][int(lis[j][1])] = "0"
    
for k in linhas:
    for l in k:
        print(l, end=" ")
    print()
