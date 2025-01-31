import math

def Consejo():
    print("Si introduces un número, podemos decirte el número máximo aproximado de intentos que necesitas para adivinarlo.\nPor ejemplo, si el rango es del 1 al 512, introduce 512.")

    numero_rango = int(input())
    resultado = math.log2(numero_rango)
    print(f"""Necesitarás aproximadamente un máximo de {math.ceil(resultado)} intentos""")

# Seguramente se pueda afinar mucho más esta parte. Al final opte por math.ceil() en lugar de round() porque si log2(n) no da un número entero, 
# a la mínima que tenga un decimal ya implicaría la posibilidad de necesitar un intento adicional para adivinar el número.