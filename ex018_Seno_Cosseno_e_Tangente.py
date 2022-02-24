import math

ÂNGULO = float(input("DIGITE AQUI O ÂNGULO QUE VOCê DESEJA "))

RADIANO = math.radians(ÂNGULO)
SENO = math.sin(RADIANO)

COSSENO = math.cos(RADIANO)

TANGENTE = math.tan(RADIANO)
print(f"se o ângulo for de {ÂNGULO:.2f  } graus")
print(f"O seno será de {SENO:.2f}")
print(f"O cosseno será de {COSSENO:.2f}")
print(f"E a tangente será de {TANGENTE:.2f}")
