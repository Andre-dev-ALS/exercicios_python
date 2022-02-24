import random

aluno1 = input("nome do aluno  1")
aluno2 = input("nome do aluno 2")
aluno3 = input("nome do aluno 3")
aluno4 = input("nome do aluno 4")
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)


print(f"A ordem de apresentação será {alunos}")
