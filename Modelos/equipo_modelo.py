# ==============================================================================
# CAPA MODELO: modelos/equipo_modelo.py
# Responsabilidad: Gestionar los datos, validaciones y reglas del inventario.
# ==============================================================================

def limpiar_texto(texto):
    """Función reutilizable para estandarizar cadenas de texto."""
    return texto.strip().lower()

def buscar_equipo_por_codigo(codigo, inventario):
    """
    Función transversal reutilizada en registro, préstamo y devolución.
    Busca un equipo por su código y retorna su diccionario o None.
    """
    codigo_limpio = limpiar_texto(codigo)
    for equipo in inventario:
        if limpiar_texto(equipo["codigo"]) == codigo_limpio:
            return equipo
    return None

def agregar_equipo(inventario, codigo, nombre, categoria):
    """Registra un nuevo equipo tras validar campos, formato de código y duplicados."""
    if not codigo.strip() or not nombre.strip() or not categoria.strip():
        return False, "Todos los campos son obligatorios (no se permiten datos vacíos)."

    if "@" in codigo:
        return False, "El código del equipo no puede contener '@'."

    if nombre.strip().isdigit() or categoria.strip().isdigit():
        return False, "El nombre y la categoría no pueden ser solo números."

    if buscar_equipo_por_codigo(codigo, inventario):
        return False, f"El código '{codigo}' ya se encuentra registrado en el sistema."

    nuevo = {
        "codigo": codigo.strip().upper(),
        "nombre": nombre.strip(),
        "categoria": categoria.strip(),
        "estado": "Disponible",
        "estudiante": "Ninguno",
        "fecha": "Ninguna"
    }
    inventario.append(nuevo)
    return True, f"Equipo '{nombre.strip()}' registrado exitosamente."

def procesar_prestamo(inventario, codigo, estudiante, fecha):
    """Valida existencia, disponibilidad y datos para ejecutar un préstamo."""
    if not codigo.strip() or not estudiante.strip() or not fecha.strip():
        return False, "Debe completar código, estudiante y fecha."

    if estudiante.strip().isdigit():
        return False, "El nombre del estudiante no puede ser solo números."

    equipo = buscar_equipo_por_codigo(codigo, inventario)
    if not equipo:
        return False, "El código de equipo ingresado no existe."

    if equipo["estado"] != "Disponible":
        return False, f"El equipo no está disponible (prestado a {equipo['estudiante']})."

    equipo["estado"] = "No Disponible"
    equipo["estudiante"] = estudiante.strip()
    equipo["fecha"] = fecha.strip()
    return True, f"Préstamo registrado: {equipo['nombre']} asignado a {equipo['estudiante']}."

def procesar_devolucion(inventario, codigo):
    """Valida existencia y estado prestado para restituir un equipo."""
    if not codigo.strip():
        return False, "El código del equipo no puede estar vacío."

    equipo = buscar_equipo_por_codigo(codigo, inventario)
    if not equipo:
        return False, "El código de equipo no existe en el inventario."

    if equipo["estado"] == "Disponible":
        return False, "El equipo ya figura como disponible (no tiene préstamo activo)."

    equipo["estado"] = "Disponible"
    equipo["estudiante"] = "Ninguno"
    equipo["fecha"] = "Ninguna"
    return True, f"Equipo '{equipo['nombre']}' devuelto y disponible nuevamente."

def contar_disponibles_categoria(inventario, categoria):
    """Calcula el total y los disponibles de una categoría específica."""
    cat_limpia = limpiar_texto(categoria)
    total = 0
    disponibles = 0
    for eq in inventario:
        if limpiar_texto(eq["categoria"]) == cat_limpia:
            total += 1
            if eq["estado"] == "Disponible":
                disponibles += 1
    return total, disponibles