def validar_registro(registro):
    """
    Valida un registro individual.
    
    Reglas:
    - edad debe ser numérica y estar entre 0 y 100
    - ingreso no debe estar vacío y debe ser numérico
    - satisfacción debe ser entero entre 1 y 5
    - departamente no debe estar vacío
    
    Si el registro es válido, devuelve True.
    Si no es válido, lanza un ValueError.
    """
    if registro["departamento"].strip() == "":
        raise ValueError("El departamento no puede estar vacío.")
    
    try:
        edad = int(registro["edad"])
    except ValueError:
        raise ValueError(f"Edad inválida: {registro["edad"]}")
    
    if edad < 0 or edad > 100:
        raise ValueError(f"Edad fuera de rango: {edad}")
    
    if registro["ingreso"].strip() == "":
        raise ValueError("El ingreso no puede estar vacío")
    
    try:
        ingreso = float(registro["ingreso"])
    except ValueError:
        raise ValueError(f"Ingreso inválido: {registro["ingreso"]}")
    
    if ingreso < 0:
        raise ValueError(f"Ingreso negativo: {ingreso}")
    
    try:
        satisfaccion = int(registro["satisfaccion"])
    except ValueError:
        raise ValueError(f"satisfacción inválida: {registro["satisfaccion"]}")
    
    if satisfaccion < 1 or satisfaccion > 5:
        raise ValueError(f"satisfacción fuera de rango: {satisfaccion}")
    
    return True


def separar_registros(registros):
    """
    Separa registros válidos e inválidos.
    
    Devuelve:
    - lista de registros válidos
    - lista de registros inválidos con número de fila y error
    """
    registros_validos = []
    registros_invalidos = []
    
    for numero_fila, registro in enumerate(registros, start=2):
        try:
            validar_registro(registro)
        except ValueError as error:
            registros_invalidos.append({
                "fila": numero_fila,
                "registro": registro,
                "error": str(error)
            })
        else:
            registros_validos.append(registro)
            
    return registros_validos, registros_invalidos