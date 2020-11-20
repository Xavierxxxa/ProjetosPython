def CalcMedia(N1, N2, N3):
    MF = (4*N1 + 4*N2 + 2*N3)/10
    return MF

def Media(M):
    if M >=6:
        Situacao = "Aprovado"
    else:
        Situacao = "Reprovado"
    return Situacao

Dados = []
arq = open("ALUNOS.txt", "r")
s = arq.readline()
c = 0
maiorPalavra=0
while s != "":
    s = s.rstrip()
    t = s.split(";")
    t[0] = int(t[0])
    t[1] = float(t[1])
    t[2] = float(t[2])
    t[3] = float(t[3])
    T = CalcMedia(t[1], t[2], t[3])
    St = Media(T)
    Dados.append(list(t))
    Dados[c].append(T)
    Dados[c].append(St)
    tamanho=len(t[4])
    if tamanho>maiorPalavra:
        maiorPalavra=tamanho
    s = arq.readline()
    c += 1
arq.close()
print("Matrícula:     Nome do Aluno: "," "*(maiorPalavra-15),"Média Final:   Situação:")
for item in Dados:
    espaco=" "*(maiorPalavra-len(item[4]))
    br = " "*10
    print("{} {}{} {:.1f}{}   {}".format(item[0],item[4],espaco,item[5], br,item[6]))

    













