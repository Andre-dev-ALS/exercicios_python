nome = input("Digite seu nome completo")

print("Analisando o seu nome")

print(f"O seu nome em maiúsculas é {nome.upper()}")
print(f"O seu nome em minuscúlas é {nome.lower()}")
espaços = nome.count(" ")

print(f"O seu nome completo  tem {nome.__len__() - espaços} letras ")
separador_nome = nome.split()
print(
    f"O seu primeiro nome é {separador_nome[0]} e ele tem {separador_nome[0].__len__()} letras "
)
