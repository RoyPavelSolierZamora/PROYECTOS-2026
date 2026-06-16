from functools import reduce


def calcular_promedio(valores):
    """
    Calcula el promedio de una lista de valores numéricos.
    """
    if len(valores) == 0:
        return 0
    
    return sum(valores) / len(valores)


def contar_por_campo(registros, campo):
    """
    Cuenta cuántas veces aparece cada valor de un campo.
    """
    conteo = {}
    
    for registro in registros:
        valor = registro[campo]
        
        if valor in conteo:
            conteo[valor] += 1
        else:
            conteo[valor] = 1
    
    return conteo


def obtener_departamentos_unicos(registros):
    """
    Devuelve una lista ordenada de departamentos únicos.
    """
    departamento = set()
    
    for registro in registros:
        departamento.add(registro["departamento"])
        
    return sorted(list(departamento))


def contar_palabras_comentarios(registros):
    """
    Cuenta la frecuencia de palabras en los comentarios.
    """
    frecuencias = {}
    
    for registro in registros:
        comentario = registro["comentario"]
        palabras = comentario.split()
        
        for palabra in palabras:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
                
    return frecuencias


def contar_mayores_edad(registros):
    """
    Cuenta registros de personas mayores o iguales a 18 años usando filter.
    """
    mayores = list(filter(lambda r: r["edad"] >= 18, registros))
    return len(mayores)


def sumar_ingresos_con_reduce(registros):
    """
    Suma ingresos usando reduce.
    
    Esto se muestra como ejemplo educativo.
    En casos simples, sum() suele ser más legible.
    """
    ingresos = [registro["ingresos"] for registro in registros]
    
    if len(ingresos) == 0:
        return 0
    
    return reduce(lambda acumulado, valor: acumulado + valor, ingresos)


def calcular_resumen(registros_limpios, registros_invalidos):
    """
    calcula un resumen general de la encuesta.
    """
    
    edades = [registro["edad"] for registro in registros_limpios]
    ingresos = [registro["ingreso"] for registro in registros_limpios]
    satisfaccion = [registro["satisfaccion"] for registro in registros_limpios]
    
    resumen = {
        "total_registros_validos": len(registros_limpios),
        "total_registros_invalidos": len(registros_invalidos),
        "edad_promedio": round(calcular_promedio(edades), 2),
        "ingreso_promedio": round(calcular_promedio(ingresos), 2),
        "satisfaccion_promedio": round(calcular_promedio(satisfaccion), 2),
        "conteo_por_departamento": contar_por_campo(registros_limpios, "departamento"),
        "conteo_por_nivel_educativo": contar_por_campo(registros_limpios, "nivel_educativo"),
        "departamentos_unicos": obtener_departamentos_unicos(registros_limpios),
        "frecuencia_palabras": contar_palabras_comentarios(registros_limpios),
        "mayores_de_edad": contar_mayores_edad(registros_limpios),
        "suma_ingresos_reduce": sumar_ingresos_con_reduce(registros_limpios)
    }
    
    return resumen