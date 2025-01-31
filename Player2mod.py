import getpass
from GuardarExcelMod import guardar_resultados

def Players2():
    
    def Submenu2():
        opcion1 = print("1. Fácil (20 intentos)")
        opcion1 = print("2. Medio (12 intentos)")
        opcion1 = print("3. Difícil (5 intentos)")

    def Valida3(minimo, maximo):
        opcion = 0
        while opcion < minimo or opcion > maximo:
            opcion = int(input("Por favor, selecciona una opción válida del Menú: "))
            return opcion


    def Players2F():

        num1 = int(getpass.getpass("Introduce un número entre el 1 y el 1000: "))

        while (num1 < 1 or num1 > 1000):
            print("El número está fuera de rango.")
            num1 = getpass.getpass("Introduce un número entre el 1 y el 1000: ")

        contador = 0
        victoria = 0
        derrota = 0
        num2 = 0
        while num2 != num1 and contador < 20:
            print("Adivina el número: ")
            num2 = int(input())
            contador = contador + 1
            if num2 == num1:
                print("¡Has acertado!")
                victoria = victoria + 1
            elif contador == 20:
                print(f"""Has perdido. El número que buscabas era {num1}""")
                derrota = derrota + 1
            elif num2 > num1:
                print("El número que buscas es menor")
            elif num2 < num1:
                print("El número que buscas es mayor")

        nombre = input("Introduce tu nombre: ")
        guardar_resultados(nombre, contador, victoria, derrota)
        
    def Players2M():
        
        num1 = int(getpass.getpass("Introduce un número entre el 1 y el 1000: "))

        while (num1 < 1 or num1 > 1000):
            print("El número está fuera de rango.")
            num1 = getpass.getpass("Introduce un número entre el 1 y el 1000: ")

        contador = 0
        victoria = 0
        derrota = 0
        num2 = 0
        while num2 != num1 and contador < 12:
            print("Adivina el número: ")
            num2 = int(input())
            contador = contador + 1
            if num2 == num1:
                print("¡Has acertado!")
                victoria = victoria + 1
            elif contador == 12:
                print(f"""Has perdido. El número que buscabas era {num1}""")
                derrota = derrota + 1
            elif num2 > num1:
                print("El número que buscas es menor")
            elif num2 < num1:
                print("El número que buscas es mayor")

        nombre = input("Introduce tu nombre: ")
        guardar_resultados(nombre, contador, victoria, derrota)
    
    def Players2D():
        num1 = int(getpass.getpass("Introduce un número entre el 1 y el 1000: "))

        while (num1 < 1 or num1 > 1000):
            print("El número está fuera de rango.")
            num1 = getpass.getpass("Introduce un número entre el 1 y el 1000: ")

        contador = 0
        victoria = 0
        derrota = 0
        num2 = 0
        while num2 != num1 and contador < 5:
            print("Adivina el número: ")
            num2 = int(input())
            contador = contador + 1
            if num2 == num1:
                print("¡Has acertado!")
                victoria = victoria + 1
            elif contador == 5:
                print(f"""Has perdido. El número que buscabas era {num1}""")
                derrota = derrota + 1
            elif num2 > num1:
                print("El número que buscas es menor")
            elif num2 < num1:
                print("El número que buscas es mayor")

        nombre = input("Introduce tu nombre: ")
        guardar_resultados(nombre, contador, victoria, derrota)
    
    Submenu2()
    opcion = Valida3(1, 3)

    if opcion == 1:
        Players2F()
    elif opcion == 2:
        Players2M()
    elif opcion == 3:
        Players2D()