dias = int(input("Quantos dias vocÊ alugou o carro?"))
km = float(input("Quantos kilometros você rodou com o carro?"))
preço = (dias * 60) + (km * 0.15)

print(f"O total a pagar é de {preço:.2f} reais")
