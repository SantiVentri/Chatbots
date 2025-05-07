import pandas as pd
import difflib

# Cargar CSV
df = pd.read_csv('preguntas.csv')
preguntas_lista = df['preguntas'].tolist()

def main():
    comando = ""
    while comando.lower() != "salir":
        print('\n\n')
        print('Bienvenido al chatbot de la UADE. ¿En qué te puedo asistir hoy?'.center(150))
        print('\n')
        comando = input('$ ')

        if comando.lower() == "salir":
            print('\nHasta luego\n')
        else:
            # Buscar coincidencias exactas o parciales
            coincidencias = df[df['preguntas'].str.contains(comando, case=False, na=False)]

            if not coincidencias.empty:
                print(f"🤖 {coincidencias.iloc[0]['respuestas']}")
            else:
                # Buscar la pregunta más parecida
                similar = difflib.get_close_matches(comando, preguntas_lista, n=1, cutoff=0.5)

                if similar:
                    respuesta = df[df['preguntas'] == similar[0]].iloc[0]['respuestas']
                    print(f"🤖 Tal vez quisiste decir: '{similar[0]}'")
                    print(f"   {respuesta}")
                else:
                    print("🤖 No encontré una respuesta parecida. ¿Podés reformular la pregunta?")

if __name__ == "__main__":
    main()
