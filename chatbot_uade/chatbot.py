import pandas as pd
import difflib

df = pd.read_csv('preguntas.csv')  # Lee el archivo 'preguntas.csv'
preguntas_lista = df['preguntas'].tolist()

# Función para validar que el input tenga al menos 8 letras o 2 palabras
def es_input_valido(texto):
    return len(texto.strip()) >= 8 or len(texto.strip().split()) >= 2

def main():
    comando = ""

    while comando.lower() != "salir":
        print('\n\n')
        print('Bienvenido al chatbot de la UADE. ¿En qué te puedo asistir hoy?'.center(150))
        print('\n')
        comando = input('$ ').strip()

        if comando.lower() == "salir":
            print('\n>> Hasta luego\n')
            return

        if not es_input_valido(comando):
            print(">> Por favor, escribí una consulta más clara (mínimo 8 letras o 2 palabras).")
            continue

        # Buscar coincidencias exactas o parciales
        coincidencias = df[df['preguntas'].str.contains(comando, case=False, na=False)]

        if not coincidencias.empty:
            print(f">> {coincidencias.iloc[0]['respuestas']}")
        else:
            similar = difflib.get_close_matches(comando, preguntas_lista, n=1, cutoff=0.5)

            if similar:
                respuesta = df[df['preguntas'] == similar[0]].iloc[0]['respuestas']
                print(f">> Tal vez quisiste decir: '{similar[0]}'")
                print(f">> {respuesta}")
            else:
                print(">> No encontré una respuesta parecida. ¿Podés reformular la pregunta?")

if __name__ == "__main__":
    main()