n = str(input("Digite o seu nome completo")).strip().upper()
nome = n.split()
print(f"O seu primeiro nome é {nome[0]} ")
print(f"O seu último nome é {nome[-1]}")
