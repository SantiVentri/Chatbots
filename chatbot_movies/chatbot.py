import pandas as pd

# Leer el archivo csv
df = pd.read_csv('movies.csv')

# Función de buscar película en el archivo
def buscarPelicula(busqueda):
    # Crea un filtro si el parámetro que recibió coincide con algún título, año de estreno, género o director
    # case=False hace que no importen las mayúsculas al buscar y na=False hace que si no aparecen no tiré error
    filtro = df[
        df['title'].str.contains(busqueda, case=False, na=False) |
        df['release'].astype(str).str.contains(busqueda, case=False, na=False) |
        df['genre'].str.contains(busqueda, case=False, na=False) |
        df['director'].str.contains(busqueda, case=False, na=False)
    ]

    # Devuelve la variable filtro
    return filtro

# Función de agregar una película al archivo
def agregarPelicula(title, release, genre, director):

    # Crea una varibale con los parámetros que recibió
    nueva_pelicula = {
        'title': title,
        'release': release,
        'genre': genre,
        'director': director
    }

    # Vuelve a df (la variable del archivo) en una variable global
    global df

    # Concatena la nueva película al DataFrame (tabla de archivo)
    df = pd.concat([df, pd.DataFrame([nueva_pelicula])], ignore_index=True)
    df.to_csv('movies.csv', index=False)

    print(f'Película "{title}" agregada correctamente.')

# Función main con el menú
def main():
    comando = ""
    while comando.lower() != "salir":
        print('\n\n\n')
        print('*************************************************************************************'.center(150))
        print('Bienvenido a al chatbot de IMDB, encontrá la pelicula que estas buscando en segundos.'.center(150))
        print('*************************************************************************************'.center(150))

        print('****** Menú de opciones ******'.center(150))
        print('1. Buscar película'.center(150))
        print('2. Agregar película'.center(150))
        print('\n\n\n')

        print('Ingresar comando (1, 2 o "salir" para salir)')
        comando = input('$ ')

        if comando.lower() == 'salir':
            print('Hasta luego!')
        elif comando == '1':
            print('Buscá tu película por nombre, director, año de estreno o género')
            busqueda = input('$ ')

            # Se usa la variable "busqueda" como parámetro de la función buscarPelícula() y se guarda en otra variable llamada "resultado"
            resultado = buscarPelicula(busqueda)
            
            # Si resultado está vacío, se muestra un mensaje, sino se muestran los resultados.
            if resultado.empty:
                print('Ups... No encontramos lo que estabas buscando.')
            else:
                print(f'Resultados:\n{resultado}')

        elif comando == '2':
            
            # Formulario para agregar una película
            print('Agregá una película a la base de datos.')
            title = input('Título de película: ').title()
            release = int(input('Año de estreno: '))
            genre = input('Ingresar género de la película: ').title()
            director = input('Director de película: ').title()

            # Se llama a la función de agregar película y se le pasan los valores del formulario como parámetros
            agregarPelicula(title, release, genre, director)
        else:
            print('Ingresar un comando válido\n\n\n')

# Esto se asegura que el menú o la función main solo se ejecute si este archivo se ejecuta directamente.
if __name__ == "__main__":
    main()