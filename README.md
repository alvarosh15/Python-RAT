# Python-RAT
Remote Administration Tool para Windows escrita en Python, originalmente de https://github.com/FZGbzuw412/Python-RAT. Probado en Windows 11. Por defecto el RAT permite la comunicación con un servidor de comando y control, enviar y recibir comandos, descarga y subida de ficheros, y volcado de credenciales a través de un keylogger, entre otras funcionalidades.

## Modificaciones
Eliminados todos los comandos relacionados con webcam, capturas de pantalla, etc... también los de setwallpaper, volumeup, volumedown, algunos de desactivar teclado, raton... Con el objetivo de evitar la detección a través de funciones que no vamos a necesitar.

Cifrados todos los comandos al enviarlos desde el servidor. De esta forma si alguien analiza los strings del fichero no verá el comando. El cifrado consiste en una especie de cifrado Cesar en la que la letra en la posición i se desplaza i posiciones en el alfabeto.

Ofuscadas todas las cadenas de texto en el cliente, utilizando diversos metodos. Por ejemplo:
output_string = chr(110) + chr(111) + " " + chr(111) + chr(117) + chr(116) + chr(112) + chr(117) + chr(116)
-> no output 
task_manager_str = bytes.fromhex('5461736b204d616e61676572').decode('utf-8')
-> Task Manager
Excepto algunas como "No such file in directory". Sería muy sospechoso tener todas las cadenas ofuscadas.

Añadida la persistencia del binario por defecto al ejecutarse (Añadiendo mi nombre como parse de la persistencia). También está la opción de desactivar la persistencia con un comando. En lugar de usar "persistence" en el cógido aparece como "calculate" para dificultar la detección de la cadena en el código y en el nombre de las funciones.

[No probado] Añadido un comando lsassdump para obtener un dump de lsass a través de procdump.exe y recibirlo en el servidor. Me ha sido imposible probarlo porque cada vez que ejecutaba el comando decía acceso denegado y no he podido arreglarlo, probablemente se deba a que no he sido capaz de desactivar del todo la seguridad de Windows.

## Uso
IMPORTANTE: Antes de ejecutar tanto servidor como cliente es necesario cambiar justo antes del main la ip por defecto por la del atacante.

### Uso
```
# Instalar dependencias
pip3 install -r requirements.txt

# Generar el .exe para el cliente 
python3 -m PyInstaller --onefile client.pyw

# Ejecutar el servidor 
python3 server.py

# (Opcional) En lugar de ejecutar el servidor generar otro .exe 
python3 -m PyInstaller --onefile server.py
```
Junto con los archivos se adjunta un cliente y un servidor ya compilados en formato .exe con dirección ip 127.0.0.1.

