from random import choice

def GeraSenha(Tipo, Tam):
        num = "0123456789"    
        alfa = 'ABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijlmnopqrstuwvxyz'
        alfaN = "ABCDEFGHIJKLMNOPQRSTUWVXYZ0123456789"
        alfaM = 'ABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijlmnopqrstuwvxyz0123456789'
        geral =  'ABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijlmnopqrstuwvxyz0123456789!@#$%&*?/\\{}[]"<>:;'
        senha = " "
        for char in range(Tam):
            if Tipo == "a":
                senha += choice(num)
            elif Tipo == "b":
                senha += choice(alfa)
            elif Tipo == "c":
                senha += choice(alfaN)
            elif Tipo == "d":
                senha += choice(alfaM)
            elif Tipo == "e":
                senha += choice(geral)
        return  senha

Dados = []
arq = open("MATR.txt", "r")
s = arq.readline()
while s != "":
    s = s.rstrip()
    t = s.split()
    t[0] = int(t[0])
    Dados.append(list(t))
    s = arq.readline()
arq.close()
print (Dados)
c = 0
Tam = int(input("Informe quantas caracteres a senha deve conter: "))
Tipo = input("Informe o tipo de senha que deve ser gerada: ")
while c < len(Dados):
        T = GeraSenha(Tipo, Tam)
        Dados[c].append(T)
        c += 1
print(Dados)

arq = open("SENHAS.txt", "w")
for s in Dados:
        arq.write("{};{}\n".format(s[0], s[1]))
arq.close()

    
