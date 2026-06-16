# Limpiar textos, convertir tipos y crear variables

def limpiar_texto(texto, modo = "title"):
    """
    Limpia espacios al inicio y final
    """
    texto_limpio = texto.strip()
    
    if modo == "title":
        return texto_limpio.title()
    
    if modo == "lower":
        return texto_limpio.lower()
    
    return texto_limpio


def clasificar_grupo_edad(edad):
    """
    Clasifica la edad en grupos
    """
    
    if edad < 18:
        return "menor_edad"
    elif edad <= 64:
        return "adulto"
    else:
        return "adulto_mayor"


def clasificador_ingreso(ingreso):
    """
    Clasificar el ingreso en categorias simples_
    """
    
    if ingreso < 1000:
        return "bajo"
    elif ingreso < 2000:
        return "medio"
    else:
        return "alto"


def transformar_registros(registro):
    """
    Limpia y transaforma un registro válido
    """
    
    edad = int(registro["edad"])
    ingreso = int(registro["ingreso"])
    satisfaccion = int(registro["satisfaccion"])
    
    registro_limpio = {
        "id": int(registro["id"]),
        "edad": edad,
        "sexo": limpiar_texto(registro["sexo"]),
        "departamento": limpiar_texto(registro["departamento"]),
        "nivel_educativo": limpiar_texto(registro["nivel_educativo"]),
        "ingreso": ingreso,
        "satisfaccion": satisfaccion,
        "comentario": limpiar_texto(registro["comentario"]),
        "grupo_edad": clasificar_grupo_edad(edad),
        "categoria_ingreso": clasificador_ingreso(ingreso),
    }
    
    return registro_limpio


def transformar_registro(registros):
    """
    TRANSFORMAR una lista de registros validos
    """
    
    registros_transformados = []
    
    for registro in registros:
        registros_transformado = transformar_registro(registro)
        registros_transformados.append(registros_transformado)
        
    return registros_transformados