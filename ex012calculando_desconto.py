produto = float(input("Qual o preço do produto $ ?"))
desconto = produto - (produto * 5 / 100)


print(f"O produto custava {produto:.2f} reais")
print(f"Mas com o desconto de 5% ele passa a custar {desconto:.2f} reais")
