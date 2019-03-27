#função para identificar os alunos
#com idade maior ou a 13 anos e
#altura menor do que a média da turma
#retorna a média e a quantidade de
#alunos que atenderam ao critério
def selecao13(data):
    c=0
    s=0
    media=0
    for i in data:
        s+=i[1]
    media=s/len(data)

    for i in data:
        if (i[0]>=13 and i[1]<media):
            c+=1

    return media,c

#programa principal
lista = [[10,1.7],[14,1.62],[13,1.69],[12,1.56]]
#retorna a qtade de alunos
#maior ou igual a 13 anos
#altura menor que a média da turma
media,qtdade=selecao13(lista)
print("Alunos com mais ou igual a 13 anos e\n")
print("altura menor do que a média da turma.\n")
print("Altura média = ",media)
print("Quantidade = ",qtdade)

