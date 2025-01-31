import openpyxl as pxl

def guardar_resultados(nombre, contador, victoria, derrota):
    wb = pxl.load_workbook("C:\\Users\\Carlos\\Adivinanzas.xlsx")
    ws = wb["Juego_Stats"]

    if ws.max_row == 1:
        ws.append(["Nombre", "Intentos", "Victoria", "Derrota"])
        wb.save("C:\\Users\\Carlos\\Adivinanzas.xlsx")
    
    ws.append([nombre, contador, victoria, derrota])
    wb.save("C:\\Users\\Carlos\\Adivinanzas.xlsx")