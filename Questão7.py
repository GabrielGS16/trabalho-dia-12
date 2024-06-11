Aluno = input("Digite o nome do estudante: ")
Materia = input("Nome da materia: ")
n1 = int(input("Digite nota parcial: "))
n2 = int(input("Digite nota bimestral: "))
n = (n1 + n2)/2 
if 10 > n >= 0:
    if 10> n >= 6:
        situacao = ('aprovado')
    else:
        situacao = ('reprovado')
    print(f'O aluno {Aluno} está {situacao} na disciplina {Materia}')
else:
    print('nota inválida!!!')