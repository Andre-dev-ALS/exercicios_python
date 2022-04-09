número = int(input("Digite um número"))

print("Analisando o número digitado")
unidade = número / 1 % 10
dezena = número / 10 % 10
centena = número / 100 % 10
milhar = número / 1000 % 10


print(f"A unidade do número {número} é{unidade:.0f} ")
print(f"A dezena do número {número} é {dezena:.0f}")
print(f"A centena do número {número} é {centena:.0f}")
print(f" o milhar do número {número} é {milhar:.0f}")
