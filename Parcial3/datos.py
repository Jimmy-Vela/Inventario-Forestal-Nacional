# ==========================================
# Capa de Acceso a Datos (DAL)
# Sistema Inventario Forestal Nacional (IFN)
# ==========================================

import os

ARCHIVO_DATOS = "inspecciones.txt"

def inicializar_archivo_por_defecto():
    """Crea el archivo plano con registros iniciales de flora si no existe."""
    if not os.path.exists(ARCHIVO_DATOS):
        datos_iniciales = [
            "CONG-001,Sector La Virginia,Brigada Andina 1,4,15,35,80,Guayacán Rosado,Maderable,COL-FL-001\n",
            "CONG-002,Reserva El Candil,Brigada Forestal Sur,3,10,22,54,Cedro,Maderable,COL-FL-002\n"
        ]
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            archivo.writelines(datos_iniciales)

def leer_inspecciones_archivo():
    """Lee todas las líneas del archivo plano y retorna una lista con los textos crudos."""
    inicializar_archivo_por_defecto()
    registros = []
    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                registros.append(linea)
    return registros

def escribir_inspeccion_archivo(linea_datos):
    """Agrega una nueva línea de registro al archivo plano."""
    with open(ARCHIVO_DATOS, "a", encoding="utf-8") as archivo:
        archivo.write(linea_datos + "\n")