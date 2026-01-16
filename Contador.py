import tkinter as tk
import pandas as pd
from datetime import datetime


# --- LÓGICA ---
def incrementar():
    valor_actual = int(label_numero["text"])
    label_numero.config(text=str(valor_actual + 1))


def guardar_y_salir():
    # 1. Obtener el dato final
    conteo_final = int(label_numero["text"])
    fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 2. Crear una tabla de datos (Dataframe)
    datos = {"Fecha": [fecha_hoy], "Conteo Final": [conteo_final]}
    df = pd.DataFrame(datos)

    # 3. Guardar en Excel (Como tus reportes de GIS)
    df.to_excel("Reporte_Conteo.xlsx", index=False)
    print("Datos guardados en Reporte_Conteo.xlsx")
    ventana.destroy()


# --- INTERFAZ ---
ventana = tk.Tk()
ventana.title("Contador Pro v1.0")
ventana.geometry("300x250")

label_numero = tk.Label(ventana, text="0", font=("Arial", 50))
label_numero.pack(pady=20)

boton_contar = tk.Button(ventana, text="¡CONTAR!", command=incrementar, bg="green", fg="white", width=15)
boton_contar.pack(pady=5)

# Botón para guardar lo que hiciste (como tus horas H o gastos $)
boton_guardar = tk.Button(ventana, text="Guardar y Salir", command=guardar_y_salir, bg="blue", fg="white")
boton_guardar.pack(pady=10)

ventana.mainloop()