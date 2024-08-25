""" Introducción a los módulos y paquetes en Python


Si seleccionas líneas de la transcripción en esta sección, irás a la marca de tiempo en el vídeo
Los módulos y los paquetes en Python son librerías adicionales al código base de Python que contienen funciones. Los módulos hacen referencia a archivos de Python que pueden contener una o varias funciones. El uso de módulos nos permite mantener el orden. Por otra parte, los paquetes son carpetas que contienen módulos y a su vez nos permiten mantener en orden proyectos que pueden ser demasiado grandes. En Python los paquetes deben contener un archivo de inicialización conocido como init. A lo que conocemos como librerías de Python son paquetes que han sido desarrollados por la comunidad para diferentes aplicaciones. Por ejemplo, paquetes como pandas que han sido desarrollados para la manipulación de datos. """

#una forma
import datetime
horaActual=datetime.datetime.now()
print(horaActual)

#segunda forma
import datetime as dt
hora_actual=dt.datetime.now()
print(hora_actual)

#tercera forma
from datetime import datetime
horaHoy=datetime.now()
print(horaHoy)