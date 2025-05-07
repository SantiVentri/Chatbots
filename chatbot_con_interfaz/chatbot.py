import tkinter as tk
import pandas as pd
import difflib

# Cargar CSV
df = pd.read_csv('preguntas.csv')
preguntas_lista = df['preguntas'].tolist()

# Función para insertar texto con espacio
def insertar_mensaje(mensaje):
    chat.config(state='normal')
    chat.insert(tk.END, mensaje + "\n", "espaciado")
    chat.config(state='disabled')
    chat.see(tk.END)

# Validar input antes de responder
def es_input_valido(texto):
    return len(texto.strip()) >= 8 or len(texto.strip().split()) >= 2

# Función principal del chatbot
def responder():
    comando = entrada.get().strip()
    entrada.delete(0, tk.END)

    if comando.lower() == "salir":
        ventana.destroy()
        return

    if not es_input_valido(comando):
        insertar_mensaje("🤖: Por favor, escribí una consulta más clara (mínimo 8 caracteres o 2 palabras).")
        return

    insertar_mensaje(f"Tú: {comando}")

    coincidencias = df[df['preguntas'].str.contains(comando, case=False, na=False)]

    if not coincidencias.empty:
        respuesta = coincidencias.iloc[0]['respuestas']
        insertar_mensaje(f"🤖: {respuesta}")
    else:
        similar = difflib.get_close_matches(comando, preguntas_lista, n=1, cutoff=0.5)
        if similar:
            sugerida = similar[0]
            respuesta = df[df['preguntas'] == sugerida].iloc[0]['respuestas']
            insertar_mensaje(f"🤖: Tal vez quisiste decir: '{sugerida}'")
            insertar_mensaje(f"🤖: {respuesta}")
        else:
            insertar_mensaje("🤖: No encontré una respuesta parecida. ¿Podés reformular la pregunta?")

# Crear ventana
ventana = tk.Tk()
ventana.title("Chatbot UADE")
ventana.geometry("500x600")
ventana.resizable(False, False)
ventana.iconbitmap('logo.ico')

# Área de chat
chat = tk.Text(ventana, height=30, width=58, state='disabled', wrap='word')
chat.pack(pady=10)
chat.tag_configure("espaciado", spacing3=5)

# Mensaje inicial
insertar_mensaje("🤖: Bienvenido al chatbot de la UADE. ¿En qué te puedo asistir hoy?")

# Campo de entrada
entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=5)
entrada.focus()

# Botón de enviar
boton = tk.Button(ventana, text="Enviar", command=responder)
boton.pack()

# Enviar con Enter
ventana.bind('<Return>', lambda event: responder())

ventana.mainloop()
