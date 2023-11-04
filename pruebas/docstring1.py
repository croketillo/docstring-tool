import os
import argparse
import re
import sys

def agregar_docstring_a_archivos(directorio, archivo_texto, recursivo, archivo_cnf="docstring.cnf"):
    try:
        # Leer el contenido del archivo de configuración
        with open(archivo_cnf, 'r') as f:
            config_text = f.read()

        # Buscar etiquetas y valores en el archivo de configuración
        etiquetas = dict(re.findall(r'\[(\w+)\]=([^[\n]+)', config_text))

        # Leer el contenido del archivo de texto
        with open(archivo_texto, 'r') as f:
            docstring_texto = f.read()

        # Reemplazar etiquetas en el contenido del archivo de texto
        for etiqueta, valor in etiquetas.items():
            etiqueta_format = f"[{etiqueta}]"
            valor_formateado = formatear_etiqueta(valor)
            docstring_texto = docstring_texto.replace(etiqueta_format, valor_formateado)

    except FileNotFoundError:
        respuesta = input("'docstring.cnf' no encontrado. ¿Desea continuar? (S/N): ").strip().lower()
        if respuesta == "s":
            with open(archivo_texto, 'r') as f:
                docstring_texto = f.read()
        else:
            print("No se han realizado cambios en los archivos.")
            sys.exit(0)

    if recursivo:
        for root, _, files in os.walk(directorio):
            for file in files:
                if file.endswith('.py'):
                    archivo_py = os.path.join(root, file)

                    with open(archivo_py, 'r') as f:
                        contenido_py = f.read()

                    # Verificar si el archivo .py ya tiene un docstring al inicio
                    if contenido_py.strip().startswith('"""'):
                        print(f'El archivo ya tiene un docstring, se omite: {archivo_py}')
                        continue

                    try:
                        # Abrir el archivo .py en modo escritura y agregar el docstring al inicio
                        with open(archivo_py, 'w') as f:
                            f.write(f'"""{docstring_texto}"""\n\n')
                            f.write(contenido_py)
                    except Exception as e:
                        print(f"Error al escribir en el archivo .py: {archivo_py}\nError: {str(e)}")
                        continue

                    print(f'Se agregó docstring al archivo: {archivo_py}')
    else:
        for file in os.listdir(directorio):
            if file.endswith('.py'):
                archivo_py = os.path.join(directorio, file)

                with open(archivo_py, 'r') as f:
                    contenido_py = f.read()

                # Verificar si el archivo .py ya tiene un docstring al inicio
                if contenido_py.strip().startswith('"""'):
                    print(f'El archivo ya tiene un docstring, se omite: {archivo_py}')
                    continue

                try:
                    # Abrir el archivo .py en modo escritura y agregar el docstring al inicio
                    with open(archivo_py, 'w') as f:
                        f.write(f'"""{docstring_texto}"""\n\n')
                        f.write(contenido_py)
                except Exception as e:
                    print(f"Error al escribir en el archivo .py: {archivo_py}\nError: {str(e)}")
                    continue

                print(f'Se agregó docstring al archivo: {archivo_py}')

def formatear_etiqueta(etiqueta):
    etiqueta_formateada = ""
    palabras = etiqueta.split()
    linea_actual = palabras[0]

    for palabra in palabras[1:]:
        if len(linea_actual) + len(palabra) + 1 <= 80:
            linea_actual += " " + palabra
        else:
            etiqueta_formateada += linea_actual + "-\n"
            linea_actual = palabra

    etiqueta_formateada += linea_actual

    return etiqueta_formateada

def main():
    parser = argparse.ArgumentParser(description='Agrega docstrings a archivos .py')
    parser.add_argument('directorio', help='Ruta del directorio donde se encuentran los archivos .py')
    parser.add_argument('archivo_texto', help='Ruta del archivo externo con el texto para el docstring')
    parser.add_argument('-r', '--recursivo', action='store_true', help='Búsqueda recursiva de archivos .py')

    args = parser.parse_args()

    try:
        agregar_docstring_a_archivos(args.directorio, args.archivo_texto, args.recursivo)
    except Exception as e:
        print(f"Error general: {str(e)}")

if __name__ == '__main__':
    main()
