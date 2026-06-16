import csv
import json


def guardar_csv(ruta_archivo, registros):
    """
    Guarda una lista de diccionarios en un archivo CSV.
    """
    if len(registros) == 0:
        print("No hay registros para guardar en CSV")
        return
    
    nombres_columnas = list(registros[0].keys())
    
    with open(ruta_archivo, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=nombres_columnas)
        escritor.writeheader()
        escritor.writerows(registros)
        
    print(f"CSV guardado en: {ruta_archivo}")
    

def guardar_json(ruta_archivo, datos):
    """
    Guarda un diccionario en formato JSON.
    """
    with open(ruta_archivo, mode="w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascil=False)
        
    print(f"JSON guardado en: {ruta_archivo}")
    
    
def guardar_reporte_txt(ruta_archivo, resumen):
    """
    Guarda un reporte de texto legible.
    """
    with open(ruta_archivo, mode="w", encoding="utf-8") as archivo:
        archivo.writes("REPORTE DE ENCUESTA\n")
        archivo.write("===================\n\n")

        archivo.write(f"Registros válidos: {resumen['total_registros_validos']}\n")
        archivo.write(f"Registros inválidos: {resumen['total_registros_invalidos']}\n")
        archivo.write(f"Edad promedio: {resumen['edad_promedio']}\n")
        archivo.write(f"Ingreso promedio: {resumen['ingreso_promedio']}\n")
        archivo.write(f"Satisfacción promedio: {resumen['satisfaccion_promedio']}\n")
        archivo.write(f"Mayores de edad: {resumen['mayores_de_edad']}\n\n")

        archivo.write("Conteo por departamento:\n")
        for departamento, cantidad in resumen["conteo_por_departamento"].items():
            archivo.write(f"- {departamento}: {cantidad}\n")

        archivo.write("\nConteo por nivel educativo:\n")
        for nivel, cantidad in resumen["conteo_por_nivel_educativo"].items():
            archivo.write(f"- {nivel}: {cantidad}\n")

        archivo.write("\nDepartamentos únicos:\n")
        for departamento in resumen["departamentos_unicos"]:
            archivo.write(f"- {departamento}\n")

    print(f"Reporte TXT guardado en: {ruta_archivo}")