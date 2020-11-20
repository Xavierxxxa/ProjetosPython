Dados = []
arq = open("VENDAS.txt", "r")
s = arq.readline()
while s != "":
    s = s.rstrip()
    t = s.split(";")
    t[0] = int(t[0])
    t[1] = int(t[1])
    t[2] = float(t[2])
    Dados.append(list(t))
    s = arq.readline()
arq.close()
for i in Dados:
    print (i)

N = int(input("Digite o código: "))
while N != 0:
    for i in Dados:
        if N in i:
           Total = i[1] * i[2]
           print("Total vendido do produto {} = ".format(i[0]), "R$ {:.2f}".format(Total))
           Cod = True
    N = int(input("Digite o código: "))
