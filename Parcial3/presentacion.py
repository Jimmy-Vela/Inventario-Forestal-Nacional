# ==========================================
# Capa de Presentación (UI - Tkinter)
# Sistema Inventario Forestal Nacional (IFN)
# ==========================================

import tkinter as tk
from tkinter import messagebox, ttk
from logica import (
    buscar_inspeccion_por_id,
    registrar_nueva_inspeccion,
    contar_total_inspecciones
)

class SistemaIFNApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Inventario Forestal Nacional (IFN) - IDEAM")
        self.root.geometry("500x480")
        self.root.config(bg="#f0f4f8")

        # Título Principal
        titulo = tk.Label(root, text="Inventario Forestal Nacional (IFN)", font=("Arial", 16, "bold"), bg="#f0f4f8", fg="#1f3a60")
        titulo.pack(pady=20)

        subtitulo = tk.Label(root, text="Módulo de Muestreo de Flora y Cobertura Boscosa", font=("Arial", 10, "italic"), bg="#f0f4f8", fg="#4a5568")
        subtitulo.pack(pady=0)

        # Botones del Menú Principal
        btn_consultar = tk.Button(root, text="Consultar Inspección por ID", font=("Arial", 11), bg="#2b6cb0", fg="white", width=30, command=self.vent_consultar)
        btn_consultar.pack(pady=15)

        btn_registrar = tk.Button(root, text="Registrar Nueva Inspección", font=("Arial", 11), bg="#2b6cb0", fg="white", width=30, command=self.vent_registrar)
        btn_registrar.pack(pady=10)

        btn_total = tk.Button(root, text="Ver Total de Inspecciones", font=("Arial", 11), bg="#2b6cb0", fg="white", width=30, command=self.ver_total)
        btn_total.pack(pady=10)

        btn_salir = tk.Button(root, text="Salir", font=("Arial", 11), bg="#c53030", fg="white", width=30, command=root.quit)
        btn_salir.pack(pady=20)

    def vent_consultar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Consultar Inspección de Flora")
        ventana.geometry("450x520")
        ventana.config(bg="#f0f4f8")

        tk.Label(ventana, text="Ingrese ID del Conglomerado:", font=("Arial", 10, "bold"), bg="#f0f4f8").pack(pady=10)
        entry_id = tk.Entry(ventana, font=("Arial", 11), width=25)
        entry_id.pack(pady=5)

        resultado_text = tk.Text(ventana, font=("Arial", 10), width=50, height=18)
        resultado_text.pack(pady=10)
        resultado_text.config(state=tk.DISABLED)

        def buscar():
            id_buscado = entry_id.get().strip()
            encontrado = buscar_inspeccion_por_id(id_buscado)

            resultado_text.config(state=tk.NORMAL)
            resultado_text.delete("1.0", tk.END)

            if encontrado:
                info = (
                    f"--- DATOS DEL CONGLOMERADO ---\n"
                    f"ID Conglomerado : {encontrado['idConglomerado']}\n"
                    f"Ubicación       : {encontrado['ubicacion']}\n"
                    f"Nombre Brigada  : {encontrado['nombreBrigada']}\n"
                    f"N° Científicos  : {encontrado['numCientificos']}\n\n"
                    f"--- CONTEO DE ÁRBOLES (FLORA) ---\n"
                    f"Fustales        : {encontrado['conteoFustales']}\n"
                    f"Latizales       : {encontrado['conteoLatizales']}\n"
                    f"Brinzales       : {encontrado['conteoBrinzales']}\n\n"
                    f"--- MUESTREO BOTÁNICO ---\n"
                    f"Nombre Común    : {encontrado['nombreComunMuestra']}\n"
                    f"Uso             : {encontrado['usoMuestra']}\n"
                    f"Código ID       : {encontrado['codigoIdentificacion']}"
                )
                resultado_text.insert(tk.END, info)
            else:
                resultado_text.insert(tk.END, f"El conglomerado con ID '{id_buscado}' no existe.")
            resultado_text.config(state=tk.DISABLED)

        tk.Button(ventana, text="Buscar", bg="#319795", fg="white", font=("Arial", 10, "bold"), command=buscar).pack(pady=5)

    def vent_registrar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Registrar Inspección - Flora")
        ventana.geometry("460x620")
        ventana.config(bg="#f0f4f8")

        frame_form = tk.Frame(ventana, bg="#f0f4f8")
        frame_form.pack(pady=10, fill=tk.BOTH, expand=True)

        tk.Label(frame_form, text="ID Conglomerado:", font=("Arial", 9), bg="#f0f4f8").grid(row=0, column=0, sticky="w", padx=20, pady=3)
        ent_id = tk.Entry(frame_form, font=("Arial", 9), width=25)
        ent_id.grid(row=0, column=1, padx=20, pady=3)

        tk.Label(frame_form, text="Ubicación:", font=("Arial", 9), bg="#f0f4f8").grid(row=1, column=0, sticky="w", padx=20, pady=3)
        ent_ubi = tk.Entry(frame_form, font=("Arial", 9), width=25)
        ent_ubi.grid(row=1, column=1, padx=20, pady=3)

        tk.Label(frame_form, text="Nombre de la Brigada:", font=("Arial", 9), bg="#f0f4f8").grid(row=2, column=0, sticky="w", padx=20, pady=3)
        ent_brigada = tk.Entry(frame_form, font=("Arial", 9), width=25)
        ent_brigada.grid(row=2, column=1, padx=20, pady=3)

        tk.Label(frame_form, text="Número de Científicos:", font=("Arial", 9), bg="#f0f4f8").grid(row=3, column=0, sticky="w", padx=20, pady=3)
        ent_cientificos = tk.Entry(frame_form, font=("Arial", 9), width=25)
        ent_cientificos.grid(row=3, column=1, padx=20, pady=3)

        tk.Label(frame_form, text="Conteo Fustales:", font=("Arial", 9), bg="#f0f4f8").grid(row=4, column=0, sticky="w", padx=20, pady=3)
        ent_fustales = tk.Entry(frame_form, font=("Arial", 9), width=25)
        ent_fustales.grid(row=4, column=1, padx=20, pady=3)

        tk.Label(frame_form, text="Conteo Latizales:", font=("Arial", 9), bg="#f0f4f8").grid(row=5, column=0, sticky="w", padx=20, pady=3)
        ent_latizales = tk.Entry(frame_form, font=("Arial", 9), width=25)
        ent_latizales.grid(row=5, column=1, padx=20, pady=3)

        tk.Label(frame_form, text="Conteo Brinzales:", font=("Arial", 9), bg="#f0f4f8").grid(row=6, column=0, sticky="w", padx=20, pady=3)
        ent_brinzales = tk.Entry(frame_form, font=("Arial", 9), width=25)
        ent_brinzales.grid(row=6, column=1, padx=20, pady=3)

        tk.Label(frame_form, text="Nombre Común Muestra:", font=("Arial", 9), bg="#f0f4f8").grid(row=7, column=0, sticky="w", padx=20, pady=3)
        ent_nombre = tk.Entry(frame_form, font=("Arial", 9), width=25)
        ent_nombre.grid(row=7, column=1, padx=20, pady=3)

        tk.Label(frame_form, text="Uso Botánico:", font=("Arial", 9), bg="#f0f4f8").grid(row=8, column=0, sticky="w", padx=20, pady=3)
        combo_uso = ttk.Combobox(frame_form, values=["Maderable", "Medicinal", "Alimenticio", "Protección/Ecológico"], font=("Arial", 9), width=23, state="readonly")
        combo_uso.grid(row=8, column=1, padx=20, pady=3)
        combo_uso.current(0)

        tk.Label(frame_form, text="Código ID Muestra:", font=("Arial", 9), bg="f0f4f8" if 'bg' in locals() else "#f0f4f8").grid(row=9, column=0, sticky="w", padx=20, pady=3)
        ent_codigo = tk.Entry(frame_form, font=("Arial", 9), width=25)
        ent_codigo.grid(row=9, column=1, padx=20, pady=3)

        def guardar():
            datos = {
                "idConglomerado": ent_id.get().strip(),
                "ubicacion": ent_ubi.get().strip(),
                "nombreBrigada": ent_brigada.get().strip(),
                "numCientificos": ent_cientificos.get().strip(),
                "conteoFustales": ent_fustales.get().strip(),
                "conteoLatizales": ent_latizales.get().strip(),
                "conteoBrinzales": ent_brinzales.get().strip(),
                "nombreComunMuestra": ent_nombre.get().strip(),
                "usoMuestra": combo_uso.get().strip(),
                "codigoIdentificacion": ent_codigo.get().strip()
            }

            exito, mensaje = registrar_nueva_inspeccion(datos)
            if not exito:
                messagebox.showerror("Error", mensaje)
                return

            messagebox.showinfo("Éxito", "Inspección de flora registrada correctamente.")
            ventana.destroy()

        tk.Button(ventana, text="Guardar Registro", bg="#38a169", fg="white", font=("Arial", 10, "bold"), command=guardar).pack(pady=15)

    def ver_total(self):
        total = contar_total_inspecciones()
        messagebox.showinfo("Estadísticas del IFN", f"Número total de inspecciones de flora registradas: {total}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaIFNApp(root)
    root.mainloop()