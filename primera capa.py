# ==========================================
# Sistema de Inventario Forestal Nacional (IFN)
# Capa de persistencia y consulta por ID
# ==========================================

import os

# Nombre del archivo plano donde se guardan los datos
ARCHIVO_DATOS = "inspecciones.txt"

def cargar_inspecciones():
    """
    Simula la capa de persistencia: carga las inspecciones 
    desde el archivo de texto plano y retorna una lista con los registros.
    """
    inspecciones = []
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    # Se asume un formato separado por comas:
                    # id,ubicacion,brigada,num_cientificos,fustales,latizales,brinzales,nombre_muestra,uso,codigo
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

def mostrar_menu():
    print("\n--- SISTEMA INVENTARIO FORESTAL NACIONAL (IFN) ---")
    print("1. Consultar inspección")
    print("2. Total de inspecciones")
    print("3. Salir")

def main():
    continuar = True
    
    # Cargar inspecciones desde el archivo plano al iniciar
    print("Cargando inspecciones desde el archivo de texto plano...")
    lista_inspecciones = cargar_inspecciones()
    total_inspecciones = len(lista_inspecciones)
    print(f"Se cargaron {total_inspecciones} registros correctamente.")
    
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == "1":
            id_buscado = input("\nIngrese el idConglomerado a consultar: ").strip()
            inspeccion_encontrada = None
            
            # Buscar en la lista cargada (Capa de persistencia / Lógica)
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
            print(f"\n[Estadísticas] Número total de inspecciones: {total_inspecciones}")
            
        elif opcion == "3":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            continuar = False
            
        else:
            print("\n[Error] Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()