# ==============================================================================
# CAPA CONTROLADOR: controladores/prestamo_controlador.py
# Responsabilidad: Intermediar entre la Vista y el Modelo.
# ==============================================================================

from Modelos.equipo_modelo import (
    agregar_equipo,
    procesar_prestamo,
    procesar_devolucion,
    contar_disponibles_categoria
)
from Vistas.consola_vista import (
    mostrar_menu_principal,
    pedir_datos_equipo,
    pedir_datos_prestamo,
    pedir_codigo_devolucion,
    pedir_categoria_consulta,
    mostrar_tabla_inventario,
    mostrar_resultado_categoria,
    mostrar_mensaje
)

def ejecutar_sistema():
    """Administra el ciclo principal del programa conectando Vista y Modelo."""
    inventario = [
        {"codigo": "LAP-01", "nombre": "Laptop Lenovo", "categoria": "Laptops", "estado": "Disponible", "estudiante": "Ninguno", "fecha": "Ninguna"},
        {"codigo": "MOU-01", "nombre": "Mouse Óptico", "categoria": "Mouse", "estado": "Disponible", "estudiante": "Ninguno", "fecha": "Ninguna"},
        {"codigo": "CAB-01", "nombre": "Cable HDMI 2m", "categoria": "Cables", "estado": "No Disponible", "estudiante": "Efrén Araujo", "fecha": "13/11/2026"}
    ]

    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            cod, nom, cat = pedir_datos_equipo()
            exito, msg = agregar_equipo(inventario, cod, nom, cat)
            mostrar_mensaje(exito, msg)

        elif opcion == "2":
            cod, est, fec = pedir_datos_prestamo()
            exito, msg = procesar_prestamo(inventario, cod, est, fec)
            mostrar_mensaje(exito, msg)

        elif opcion == "3":
            cod = pedir_codigo_devolucion()
            exito, msg = procesar_devolucion(inventario, cod)
            mostrar_mensaje(exito, msg)

        elif opcion == "4":
            mostrar_tabla_inventario(inventario)

        elif opcion == "5":
            cat = pedir_categoria_consulta()
            if not cat.strip():
                mostrar_mensaje(False, "Debe ingresar una categoría válida.")
            else:
                tot, disp = contar_disponibles_categoria(inventario, cat)
                mostrar_resultado_categoria(cat.strip(), tot, disp)

        elif opcion == "6":
            print("\n[i] Cerrando sistema LabTech MVC. ¡Hasta pronto!")
            break
        else:
            mostrar_mensaje(False, "Opción inválida. Seleccione un número del 1 al 6.")