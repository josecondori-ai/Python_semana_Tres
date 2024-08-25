""" Las funciones en Python son bloques de código independientes. Cada bloque de código que compone una función tiene a su vez, instrucciones relacionadas entre sí, que se encargan de cumplir con una tarea. Entre las ventajas de usar funciones para nuestro código, encontramos que las funciones nos permiten organizar el código en partes pequeñas. Nos permiten mantener el código ordenado y fácil de entender, y además, evita que repitamos las mismas instrucciones en diferentes partes del código. A esto se le conoce como reusar el código. En Python definimos una función con la sentencia def. Esta le indica a Python que se trata de una función. Luego escribimos el nombre de la función junto a un par de paréntesis. Dentro de los paréntesis escribimos los parámetros que recibe la función. Si la función no requiere parámetros, los dejamos vacíos. Luego escribimos dos puntos, estos nos indican que lo que está indentado en las siguientes líneas va a pertenecer al bloque de la función. Dentro del bloque de la función se escriben las instrucciones que se deben ejecutar cuando se llame la función. Para ejecutar o llamar la función, escribimos su nombre junto a un par de paréntesis. Si la función recibe parámetros, se declaran dentro del paréntesis, de lo contrario, se dejan vacíos. En Python tenemos dos tipos de funciones: las Built-in functions que son funciones que han sido creadas para tareas comunes y no necesitan instalación para poder usarlas, y las User-defined functions son las funciones que como desarrolladores creamos para cada proyecto en el que estamos trabajando. """

APELLIDO='perez'

def mifuncion():
    print('hola soy una funcion')

mifuncion()

def mifuncionNueva():
    print('hola soy una funcion')
    nombre='juan'
    print(nombre,APELLIDO)

mifuncionNueva()

print(APELLIDO)
