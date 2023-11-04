import os
import argparse
import re

def eliminar_docstrings(directorio, recursivo):
    if recursivo:
        for root, _, files in os.walk(directorio):
            for file in files:
                if file.endswith('.py'):
                    archivo_py = os.path.join(root, file)
                    eliminar_docstring_de_archivo(archivo_py)
    else:
        for file in os.listdir(directorio):
            if file.endswith('.py'):
                archivo_py = os.path.join(directorio, file)
                eliminar_docstring_de_archivo(archivo_py)

def eliminar_docstring_de_archivo(archivo_py):
    try:
        with open(archivo_py, 'r') as f:
            contenido_py = f.read()

        # Utilizar una expresión regular para eliminar el docstring (incluyendo comillas iniciales)
        contenido_sin_docstring = re.sub(r'(["\']{3}.*?["\']{3})', '', contenido_py, flags=re.DOTALL)

        # Eliminar líneas en blanco al principio del archivo
        contenido_sin_docstring = contenido_sin_docstring.lstrip('\n')

        with open(archivo_py, 'w') as f:
            f.write(contenido_sin_docstring)

        print(f'Se eliminó el docstring del archivo: {archivo_py}')
    except Exception as e:
        print(f"Error al procesar el archivo .py: {archivo_py}\nError: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Elimina docstrings de archivos .py')
    parser.add_argument('directorio', help='Ruta del directorio donde se encuentran los archivos .py')
    parser.add_argument('-r', '--recursivo', action='store_true', help='Búsqueda recursiva de archivos .py')

    args = parser.parse_args()

    eliminar_docstrings(args.directorio, args.recursivo)

if __name__ == '__main__':
    main()
