# ==============================================================================
# CAPA VISTA: vistas/consola_vista.py
# Responsabilidad: Interfaz de usuario en consola (entradas y salidas).
# ==============================================================================

def mostrar_menu_principal():
    print("\n" + "=" * 62)
    print("   LABTECH (ARQUITECTURA MVC) - CONTROL DE PRÉSTAMOS")
    print("=" * 62)
    print("1. Registrar Nuevo Equipo")
    print("2. Registrar Préstamo de Equipo")
    print("3. Registrar Devolución de Equipo")
    print("4. Listar Inventario y Disponibilidad")
    print("5. Consultar Disponibilidad por Categoría")
    print("6. Salir del Programa")
    print("-" * 62)
    return input("Seleccione una opción (1-6): ").strip()

def pedir_datos_equipo():
    print("\n--- REGISTRAR NUEVO EQUIPO ---")
    codigo = input("Código del equipo (ej. LAP-02): ")
    nombre = input("Nombre del equipo (ej. Laptop Dell): ")
    categoria = input("Categoría (Laptops, Mouse, Cables, Adaptadores): ")
    return codigo, nombre, categoria

def pedir_datos_prestamo():
    print("\n--- REGISTRAR PRÉSTAMO ---")
    codigo = input("Código del equipo a prestar: ")
    estudiante = input("Nombre del estudiante: ")
    fecha = input("Fecha del préstamo (dd/mm/aaaa): ")
    return codigo, estudiante, fecha

def pedir_codigo_devolucion():
    print("\n--- REGISTRAR DEVOLUCIÓN ---")
    return input("Código del equipo a devolver: ")

def pedir_categoria_consulta():
    print("\n--- CONSULTA POR CATEGORÍA ---")
    return input("Ingrese la categoría a consultar: ")

def mostrar_tabla_inventario(inventario):
    print("\n--- INVENTARIO ACTUAL DEL LABORATORIO ---")
    if not inventario:
        print("[!] No hay equipos registrados.")
        return
    print(f"{'Código':<10} | {'Nombre':<18} | {'Categoría':<12} | {'Estado':<14} | {'Estudiante':<15}")
    print("-" * 78)
    for eq in inventario:
        print(f"{eq['codigo']:<10} | {eq['nombre']:<18} | {eq['categoria']:<12} | {eq['estado']:<14} | {eq['estudiante']:<15}")

def mostrar_resultado_categoria(categoria, total, disponibles):
    print(f"\nResultado para '{categoria}': {disponibles} disponible(s) de {total} registrado(s).")

def mostrar_mensaje(exito, texto):
    prefijo = "[ÉXITO]" if exito else "[ERROR]"
    print(f"\n{prefijo} {texto}")