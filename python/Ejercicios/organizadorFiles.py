from pathlib import Path
import shutil
dir_actual = Path.cwd()
destino_imagenes = Path('~/Imágenes/imagenes').expanduser()
destino_pdf = Path('~/Documentos/pdf').expanduser()
destino_manuales = Path('~/Documentos/manuales').expanduser()
#creados manualmente y que no existen en el sistema
destino_imagenes.mkdir(parents=True, exist_ok=True)
destino_pdf.mkdir(parents=True, exist_ok=True)
destino_manuales.mkdir(parents=True, exist_ok=True)
destino_txt = Path('~/Documentos/txt').expanduser().mkdir(parents=True, exist_ok=True)
extensiones_imagenes = ['.png', '.jpg', '.jpeg', '.gif']


def existe(dir_actual=dir_actual, destino_pdf=destino_pdf):
    exist = False
    for i in dir_actual.iterdir():
        if i in destino_pdf.iterdir():
            exist = True
    return exist


print(f"Organizando Archivos en {dir_actual}")

# procedo a leer el directorio
for i in dir_actual.iterdir():
    if i.suffix in extensiones_imagenes:
        print(f"Moviendo imagen: {i.name} --> {destino_imagenes}")
        shutil.move(str(i), str(destino_imagenes))
    elif i.suffix == '.pdf':
        if existe(dir_actual, destino_pdf) == False:
            print(f"el archivo {i.name} ya existe")
            continue
        else:
            shutil.move(str(i), str(destino_pdf))
    elif i.suffix == '.md':
        shutil.move(str(i), str(destino_manuales))
    elif i.suffix == '.docx':
        shutil.move(str(i), str(destino_pdf))
    elif i.suffix == '.txt':
        shutil.move(str(i), str(destino_txt))
      

print("Programa finalizado")

"""
modulo pathlib

  Es un módulo moderno en Python para trabajar con rutas de sistema de
  archivos de una manera orientada a objetos, lo que hace el código más
  legible y menos propenso a errores, independientemente del sistema
  operativo (Windows, macOS, Linux).

   * `pathlib.Path.cwd()` (Current Working Directory)
       * ¿Qué hace?: Devuelve un objeto Path que representa el directorio 
         de trabajo actual, es decir, la carpeta desde donde se está
         ejecutando el script.
       * Ejemplo: Si ejecutas tu script desde la terminal mientras estás
         en /home/usuario/scripts, pathlib.Path.cwd() te dará un objeto
         que apunta a esa ruta.

   * `pathlib.Path.expanduser()`
       * ¿Qué hace?: Convierte una ruta que comienza con el símbolo ~ (el
         cual representa el directorio "home" del usuario) en la ruta
         absoluta completa. Es fundamental para que las rutas que usan ~
         funcionen correctamente en cualquier sistema.
       * Ejemplo: En un sistema Linux,
         pathlib.Path('~/Documentos').expanduser() se convierte en un
         objeto Path que apunta a /home/tu_usuario/Documentos.

   * `pathlib.Path.iterdir()`
       * ¿Qué hace?: Devuelve un "iterador", que funciona como una lista
         que se genera sobre la marcha, con todos los archivos y carpetas
         que se encuentran directamente dentro del directorio. No mira
         dentro de las subcarpetas.
       * Ejemplo: Si una carpeta contiene archivo1.txt y la subcarpeta
         fotos/, iterdir() te dará dos objetos Path: uno para archivo1.txt
         y otro para fotos/.

   * `pathlib.Path.is_file()`
       * ¿Qué hace?: Devuelve True si la ruta apunta a un archivo y False
         si apunta a una carpeta (o si la ruta no existe). Es muy útil
         para asegurarte de que solo procesas archivos.
       * Ejemplo: pathlib.Path('mi_archivo.txt').is_file() devolverá True.


   * `pathlib.Path.suffix`
       * ¿Qué hace?: Devuelve la extensión final del archivo como una
         cadena de texto (string), incluyendo el punto. Si un archivo
         tiene múltiples extensiones (como archivo.tar.gz), solo devuelve
         la última.
       * Ejemplo: Para documento.pdf, .suffix es '.pdf'. Para
         archivo.tar.gz, .suffix es '.gz'.

   * `pathlib.Path.suffixes`
       * ¿Qué hace?: Devuelve una lista de cadenas de texto con todas las
         extensiones del archivo.
       * Ejemplo: Para documento.pdf, .suffixes es ['.pdf']. Para
         archivo.tar.gz, .suffixes es ['.tar', '.gz'].

   * `pathlib.Path.mkdir(parents=True, exist_ok=True)`
       * ¿Qué hace?: Crea el directorio apuntado por el objeto Path.
       * parents=True: Le dice al método que cree también los directorios
         "padre" si no existen. Por ejemplo, si intentas crear a/b/c y la
         carpeta a/b no existe, este parámetro hará que se cree
         automáticamente.
       * exist_ok=True: Evita que el programa lance un error si el
         directorio ya existe. Si ya existe, simplemente no hace nada.

  Módulo shutil (Shell Utilities)

  Es un módulo que proporciona funciones de alto nivel para realizar
  operaciones con archivos y carpetas, como copiar, mover, renombrar o
  eliminar. Su nombre viene de "shell utilities" (utilidades de la
  terminal).

   * `shutil.move(origen, destino)`
       * ¿Qué hace?: Mueve un archivo o una carpeta (origen) a una nueva
         ubicación (destino).
           * Si el destino es una carpeta que ya existe, el archivo se
             mueve dentro de ella.
           * Si el destino no existe, el archivo o carpeta de origen se
             renombra al nombre del destino.
       * Importante: Tradicionalmente, los argumentos origen y destino
         debían ser cadenas de texto (strings), por eso es una práctica
         común y segura convertir los objetos Path con str(), como en
         str(i).
       * Ejemplo: shutil.move('reporte.txt', 'reportes_viejos/') mueve el
         archivo reporte.txt a la carpeta reportes_viejos.
"""
