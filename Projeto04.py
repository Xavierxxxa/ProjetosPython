from random import randint
Dados = []
arq = open("PRODUTOS.txt", "r")
s = arq.readline()
c = 0
while s != "":
    s = s.rstrip()
    t = s.split(";")
    t[0] = int(t[0])
    t[2] = float(t[2])
    t[3] = float(t[3])
    t[4] = float(t[4])
    Dados.append(list(t))
    s = arq.readline()
    c += 1
arq.close()
ano = int(input("Digite o ano da venda: "))
mes = int (input("Digite o mês da venda: "))
while ano < 2016 or 0>mes<=12:
    if ano < 2016:
        ano = int(input("Digite o ano da venda(posteriores a 2016): "))
    elif 0 >mes <=12:
        mes = int(input("Digite o mês da venda(meses válidos): "))
NDiaMes = int(input("Digite a quantidade de dias do mês para o qual se deseja gerar vendas: "))
dia = 1
Prod = []
while dia <= NDiaMes:
    QtdeVendasDia = int(input("Digite a quantidade de vendas diárias: "))
    Vendas = 1
    while Vendas <= QtdeVendasDia:
        N = int(input("Digite o código do produto: "))
        ValorVenda = randint(0, 100)
        Qtde = float(input("Quantidade vendida do produto: "))
        for produtos in Dados:
            if N in produtos:
                if  0 <= ValorVenda <=75:
                    Margem = produtos[3] * (produtos[4] /100 +1 )
                elif 75 <= ValorVenda <= 100:
                    Taxa = randint(-8, 8)
                    Margem = produtos[3] * (produtos[4] /100 +1 )*(Taxa/100 +1)                  
                A = [ano, mes, dia, N, Qtde, Margem]
                Prod.append(A)
        Vendas +=1
    dia+=1
arq = open("HISTORICO.txt", "w")
for i in Prod:
    i[1]= mes
    i[2] = dia
    if  1<= dia <= 9 or 1<= mes <= 9:
        if 1<= dia <= 9:
            dia = str(dia)
            arq.write("{};{};{};{};{:.3f};{:.2f}\n".format(i[0], i[1], dia.zfill(2), i[3], i[4], i[5]))
        elif 1<= mes <= 9:
            mes = str(mes)
            arq.write("{};{};{};{};{:.3f};{:.2f}\n".format(i[0], mes.zfill(2), i[2], i[3], i[4], i[5],))
    else:
        arq.write("{};{};{};{};{:.3f};{:.2f}\n".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    print(i)
    dia = int(dia)
    mes = int(mes)
arq.close()
             


