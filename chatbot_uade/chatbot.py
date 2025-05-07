import pandas as pd
import difflib

df = pd.read_csv('preguntas.csv') # Lee el archivo 'preguntas.csv' como un DataFrame
preguntas_lista = df['preguntas'].tolist() # Convierte la columna "preguntas" en una lista

def main():
    comando = ""

    while comando.lower() != "salir":
        print('\n\n')
        print('Bienvenido al chatbot de la UADE. ¿En qué te puedo asistir hoy?'.center(150))
        print('\n')
        comando = input('$ ')

        if comando.lower() == "salir":
            print('\n>> Hasta luego\n')
        else:
            # Buscar coincidencias exactas o parciales en la columna "preguntas"
            coincidencias = df[df['preguntas'].str.contains(comando, case=False, na=False)]

            if not coincidencias.empty: # Si hay coincidencias exactas/parciales
                print(f">> {coincidencias.iloc[0]['respuestas']}") # Imprime la primera respuesta que encuentra
            else:
                # Si no encuentra coincidencias exactas, busca la pregunta más parecida usando difflib
                similar = difflib.get_close_matches(comando, preguntas_lista, n=1, cutoff=0.5)

                if similar: # Si encuentra una pregunta similar (al menos 50% parecida)
                    respuesta = df[df['preguntas'] == similar[0]].iloc[0]['respuestas']  # Busca la respuesta correspondiente
                    print(f">> Tal vez quisiste decir: '{similar[0]}'") # Sugiere la pregunta similar
                    print(f">> {respuesta}") # Muestra la respuesta
                else:
                    # Si no hay coincidencias ni similares
                    print(">> No encontré una respuesta parecida. ¿Podés reformular la pregunta?")

# Llama a la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()
