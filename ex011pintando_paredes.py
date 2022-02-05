largura = float(input("Qual a largura da parede?"))
altura = float(input("Qual a altura da parede"))
área = largura * altura
tinta = área / 2

print(
    "A sua parede tem {} de largura por {} de altura e sua area é de {} ".format(
        largura, altura, área
    )
)


print("Você vai precisar de {} litros de tinta para pintar toda a parede".format(tinta))
