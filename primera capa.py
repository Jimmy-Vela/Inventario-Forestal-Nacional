# ==========================================
# Sistema de Inventario Forestal Nacional (IFN)
# Versión final - Funcionalidad completa 
# ==========================================

import os

ARCHIVO_DATOS = "inspecciones.txt"

def cargar_inspecciones():
    """
    Capa de Acceso a Datos: Carga las inspecciones desde el archivo plano.
    """
    inspecciones = []
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
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

def guardar_inspeccion(nueva_inspeccion):
    """
    Capa de Acceso a Datos: Guarda una nueva inspección en el archivo plano.
    """
    with open(ARCHIVO_DATOS, "a", encoding="utf-8") as archivo:
        linea = ",".join([
            nueva_inspeccion["idConglomerado"],
            nueva_inspeccion["ubicacion"],
            nueva_inspeccion["nombreBrigada"],
            nueva_inspeccion["numCientificos"],
            nueva_inspeccion["conteoFustales"],
            nueva_inspeccion["conteoLatizales"],
            nueva_inspeccion["conteoBrinzales"],
            nueva_inspeccion["nombreComunMuestra"],
            nueva_inspeccion["usoMuestra"],
            nueva_inspeccion["codigoIdentificacion"]
        ])
        archivo.write(linea + "\n")

def mostrar_menu():
    print("\n--- SISTEMA INVENTARIO FORESTAL NACIONAL (IFN) ---")
    print("1. Consultar inspección por ID")
    print("2. Registrar nueva inspección")
    print("3. Ver total de inspecciones")
    print("4. Salir")

def main():
    continuar = True
    
    # Carga inicial de datos
    lista_inspecciones = cargar_inspecciones()
    
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            id_buscado = input("\nIngrese el ID del conglomerado a consultar: ").strip()
            inspeccion_encontrada = None
            
            for item in lista_inspecciones:
                if item["idConglomerado"] == id_buscado:
                    inspeccion_encontrada = item
                    break
            
            if inspeccion_encontrada:
                print("\n--- DATOS DE LA INSPECCIÓN ---")
                print(f"ID Conglomerado : {inspeccion_encontrada['idConglomerado']}")
                print(f"Ubicación       : {inspeccion_encontrada['ubicacion']}")
                print(f"Nombre Brigada  : {inspeccion_encontrada['nombreBrigada']}")
                print(f"N° Científicos  : {inspeccion_encontrada['numCientificos']}")
                print("--- CONTEO DE ÁRBOLES ---")
                print(f"Fustales        : {inspeccion_encontrada['conteoFustales']}")
                print(f"Latizales       : {inspeccion_encontrada['conteoLatizales']}")
                print(f"Brinzales       : {inspeccion_encontrada['conteoBrinzales']}")
                print("--- MUESTREO BOTÁNICO ---")
                print(f"Nombre Común    : {inspeccion_encontrada['nombreComunMuestra']}")
                print(f"Uso             : {inspeccion_encontrada['usoMuestra']}")
                print(f"Código ID       : {inspeccion_encontrada['codigoIdentificacion']}")
            else:
                print(f"\n[Aviso] El conglomerado con ID '{id_buscado}' no existe.")
                
        elif opcion == "2":
            print("\n--- REGISTRO DE NUEVA INSPECCIÓN ---")
            nueva = {
                "idConglomerado": input("ID Conglomerado: ").strip(),
                "ubicacion": input("Ubicación: ").strip(),
                "nombreBrigada": input("Nombre de la Brigada: ").strip(),
                "numCientificos": input("Número de científicos: ").strip(),
                "conteoFustales": input("Conteo de Fustales: ").strip(),
                "conteoLatizales": input("Conteo de Latizales: ").strip(),
                "conteoBrinzales": input("Conteo de Brinzales: ").strip(),
                "nombreComunMuestra": input("Nombre común de la muestra: ").strip(),
                "usoMuestra": input("Uso (medicinal, alimenticio, maderable): ").strip(),
                "codigoIdentificacion": input("Código de identificación de la muestra: ").strip()
            }
            
            # Guardar en la lista y en el archivo plano
            lista_inspecciones.append(nueva)
            guardar_inspeccion(nueva)
            print("\n[Éxito] Inspección registrada y guardada correctamente en el archivo plano.")
            
        elif opcion == "3":
            total = len(lista_inspecciones)
            print(f"\n[Estadísticas] Número total de inspecciones registradas: {total}")
            
        elif opcion == "4":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            continuar = False
            
        else:
            print("\n[Error] Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()