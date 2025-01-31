import openpyxl as pxl

def guardar_resultados(nombre, contador, victoria, derrota):
    wb = pxl.load_workbook("D:\TATE\A-Proyectos Data Analysis\A-Proyectos_Github\Appdivina\\Adivinanzas.xlsx")
    ws = wb["Juego_Stats"]

    if ws.max_row == 1:
        ws.append(["Nombre", "Intentos", "Victoria", "Derrota"])
        wb.save("D:\TATE\A-Proyectos Data Analysis\A-Proyectos_Github\Appdivina\\Adivinanzas.xlsx")
    
    ws.append([nombre, contador, victoria, derrota])
    wb.save("D:\TATE\A-Proyectos Data Analysis\A-Proyectos_Github\Appdivina\\Adivinanzas.xlsx")
