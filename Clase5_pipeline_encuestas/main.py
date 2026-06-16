from encuesta.lector import leer_csv
from encuesta.validador import separar_registros
from encuesta.transformador import transformar_registros
from encuesta.analizador import calcular_resumen
from encuesta.escritor import guardar_csv, guardar_json, guardar_reporte_txt


RUTA_ENTRADA = "data/encuesta.csv"
RUTA_SALIDA_CSV = "output/encuesta_limpia.csv"
RUTA_SALIDA_JSON = "output/resumen.json"
RUTA_SALIDA_TXT = "output/reporte.txt"


def main():
    """
    Ejecuta el pipeline completo de análisis de encuesta.
    """

    print("Iniciando pipeline de encuesta...\n")

    registros = leer_csv(RUTA_ENTRADA)

    registros_validos, registros_invalidos = separar_registros(registros)

    registros_limpios = transformar_registros(registros_validos)

    resumen = calcular_resumen(registros_limpios, registros_invalidos)
    

    guardar_csv(RUTA_SALIDA_CSV, registros_limpios)
    guardar_json(RUTA_SALIDA_JSON, resumen)
    guardar_reporte_txt(RUTA_SALIDA_TXT, resumen)

    print("\nResumen del proceso")
    print("-------------------")
    print(f"Registros leídos: {len(registros)}")
    print(f"Registros válidos: {len(registros_validos)}")
    print(f"Registros inválidos: {len(registros_invalidos)}")


    if len(registros_invalidos) > 0:
        print("\nRegistros inválidos encontrados:")
        for error in registros_invalidos:
            print(f"Fila {error['fila']}: {error['error']}")

    print("\nPipeline finalizado correctamente.")



if __name__ == "__main__":
    main()