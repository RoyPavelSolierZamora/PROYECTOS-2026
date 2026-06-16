import csv

def leer_csv(ruta_archivo, encoding="utf-8"):
    """
    lee un archivo CSV y devuelve una lista de diccionarios.
    
    Cada fila del CSV se convierte en un diccionario.
    Las claves son los nombres de las columnas.
    """
    registros = []
    
    try:
        with open(ruta_archivo, mode="r", encoding=encoding, newline="") as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                registros.append(fila)
    
    except FileNotFoundError:
        print(f"Error: No se encontró al archivo {ruta_archivo}")
        raise
    
    except Exception as error:
        print(f"Ocurrió un error al leer el archivo: {error}")
        raise
    
    else:
        print(f"Archivo leído correctamente: {ruta_archivo}")
    
    finally:
        print("Proceso de lectura finalizada.")
        
    return registros      