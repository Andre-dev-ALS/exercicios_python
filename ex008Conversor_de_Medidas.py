medida = float(input("Digite uma  distância em metros"))

km = medida / 1000
hm = medida / 100
dam = medida / 100
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print("A medida de {} metros corresponde a {} kilometros".format(medida, km))
print("A medida de {} metros corresponde a {} hectrômetro".format(medida, hm))
print("A medida de {} metros corresponde a {} decâmetro".format(medida, dam))
print("A medida de {} metros corresponde a {} decimetro".format(medida, dm))
print("A medida de {} em metros corresponde a {} centimetros".format(medida, cm))
print("A medida {} em metros corresponde a {} milimetros".format(medida, mm))
