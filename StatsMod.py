import openpyxl as pxl
import matplotlib.pyplot as mpl
import pandas as pd
import numpy as np
import GuardarExcelMod

def ScriptStats():

    def Estadisticas_Totales():

        df = pd.read_excel("C:\\Users\\Carlos\\Adivinanzas.xlsx", sheet_name = "Juego_Stats")

        #Convierto a valores numéricos porque me estaba dando error.
        df["Intentos"] = pd.to_numeric(df["Intentos"])
        df["Victoria"] = pd.to_numeric(df["Victoria"])
        df["Derrota"] = pd.to_numeric(df["Derrota"])

        victoria = df.groupby("Nombre")["Victoria"].sum()
        derrota = df.groupby("Nombre")["Derrota"].sum()

        coord = np.arange(len(victoria))
        ancho = 0.30

        fig, ax = mpl.subplots()
        ax.bar(coord - ancho/2, victoria, ancho, color = "green")
        ax.bar(coord + ancho/2, derrota, ancho, color = "red")
        ax.set_xticks(coord)
        ax.set_xticklabels(victoria.index, rotation=45, ha="right")
    
        mpl.xlabel("Nombre del Jugador")
        mpl.ylabel("Número de Victorias")
        mpl.title("Victorias y Derrotas por Jugador")
        mpl.legend(["Victorias", "Derrotas"])
        mpl.show()

        intentos = df.groupby("Nombre")["Intentos"].mean()

        intentos.plot(kind = "bar", color = "purple")
        mpl.xlabel("Nombre del Jugador")
        mpl.ylabel("Número de Intentos")
        mpl.title("Media de intentos por Jugador")
        mpl.show()

    def Stats_filtro_nombre():
        nombre = input("Introduce tu nombre para mostrar solo tus estadísticas: ")

        df = pd.read_excel("C:\\Users\\Carlos\\Adivinanzas.xlsx", sheet_name = "Juego_Stats")

        df_filtrar_nombre = df[df["Nombre"] == nombre]

        if df_filtrar_nombre.empty:
            print("No existen resultados asociados a ese nombre.")
            return

        #Recibo SettingWithCopyWarning, uso .loc para evitarlo siguiendo la documentación de Pandas.
        #Entiendo un poco lo que dice el warning, pero todavía tengo que leer en profundidad para terminar de entenderlo.
        df_filtrar_nombre.loc[:, "Intentos"] = pd.to_numeric(df_filtrar_nombre["Intentos"])
        df_filtrar_nombre.loc[:, "Victoria"] = pd.to_numeric(df_filtrar_nombre["Victoria"])
        df_filtrar_nombre.loc[:, "Derrota"] = pd.to_numeric(df_filtrar_nombre["Derrota"])


        victoria = df_filtrar_nombre.groupby("Nombre")["Victoria"].sum()
        derrota = df_filtrar_nombre.groupby("Nombre")["Derrota"].sum()
   
        coord = np.arange(len(victoria))
        ancho = 0.30

        fig, ax = mpl.subplots()
        ax.bar(coord - ancho/2, victoria, ancho, color = "green")
        ax.bar(coord + ancho/2, derrota, ancho, color = "red")
        #Establezco los xticks porque me desaparecieron los nombres.
        ax.set_xticks(coord)
        ax.set_xticklabels(victoria.index, rotation=45, ha="right")

        mpl.xlabel("Nombre del Jugador")
        mpl.ylabel("Número de Victorias")
        mpl.title("Victorias y Derrotas por Jugador")
        mpl.legend(["Victorias", "Derrotas"])
        mpl.show()

        intentos = df_filtrar_nombre.groupby("Nombre")["Intentos"].mean()

        intentos.plot(kind = "bar", color = "purple")
        mpl.xlabel("Nombre del Jugador")
        mpl.ylabel("Número de Intentos")
        mpl.title("Media de intentos por Jugador")
        mpl.show() 

    def MenuStats():
        opcion1 = print("1. Estadísticas totales")
        opcion2 = print("2. Obtener estadísticas por Jugador")
    
    def ValidaMS(minimo, maximo):
        opcion = 0
        while opcion < minimo or opcion > maximo:
            opcion = int(input("Por favor, selecciona una opción válida del Menú: "))
            return opcion

    MenuStats()
    opcion = ValidaMS(1,2)

    if opcion == 1:
        Estadisticas_Totales()
    elif opcion == 2:
        Stats_filtro_nombre()