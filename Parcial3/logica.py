# ==========================================
# Capa de Lógica de Negocio (BLL)
# Sistema Inventario Forestal Nacional (IFN)
# ==========================================

from datos import leer_inspecciones_archivo, escribir_inspeccion_archivo

def obtener_todas_inspecciones():
    """Procesa las líneas del archivo y las convierte en una lista de diccionarios estructurados."""
    lineas = leer_inspecciones_archivo()
    inspecciones = []
    for linea in lineas:
        datos = linea.split(",")
        if len(datos) == 10:
            inspecciones.append({
                "idConglomerado": datos[0],
                "ubicacion": datos[1],
                "nombreBrigada": datos[2],
                "numCientificos": datos[3],
                "conteoFustales": datos[4],
                "conteoLatizales": datos[5],
                "conteoBrinzales": datos[6],
                "nombreComunMuestra": datos[7],
                "usoMuestra": datos[8],
                "codigoIdentificacion": datos[9]
            })
    return inspecciones

def buscar_inspeccion_por_id(id_buscado):
    """Busca un conglomerado específico por su ID dentro de las reglas del negocio."""
    inspecciones = obtener_todas_inspecciones()
    for item in inspecciones:
        if item["idConglomerado"] == id_buscado:
            return item
    return None

def registrar_nueva_inspeccion(datos_dict):
    """Valida y empaqueta un nuevo registro de flora para enviarlo a persistencia."""
    if not datos_dict.get("idConglomerado") or not datos_dict.get("nombreComunMuestra"):
        return False, "El ID del conglomerado y el nombre común de la muestra son obligatorios."
    
    # Construir la línea en formato CSV para el archivo plano
    linea = ",".join([
        datos_dict["idConglomerado"],
        datos_dict["ubicacion"],
        datos_dict["nombreBrigada"],
        datos_dict["numCientificos"],
        datos_dict["conteoFustales"],
        datos_dict["conteoLatizales"],
        datos_dict["conteoBrinzales"],
        datos_dict["nombreComunMuestra"],
        datos_dict["usoMuestra"],
        datos_dict["codigoIdentificacion"]
    ])
    
    escribir_inspeccion_archivo(linea)
    return True, "Registro guardado exitosamente."

def contar_total_inspecciones():
    """Calcula el número total de inspecciones de flora registradas."""
    return len(obtener_todas_inspecciones())