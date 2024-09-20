# bus360

Esta aplicación hace un [recorrido virtual](https://bus.us.es/bus360) por las Bibliotecas de la Universidad de Sevilla.
La aplicación ha sido realizada por personal de la BUS con el software [panellum](https://pannellum.org/) y una cámara que permite hacer fotografías de 360º aportada por el [SAV](http://sav.us.es/).


## Pasos seguidos para construir los tours virtuales de Panellum

### PROCEDIMIENTO
- Con una cámara "Insta360 one R" se han realizado fotografías 360º equirectangulares.
- Con el software propio de la camara se han volcado en un ordenador y se han difuminado matrículas y caras y se ha colocado una imagen sobre el trípode.
- Con una imagen docker proporcionada por el autor de pannellum la fotografía equirectangular se ha proyectado sobre un cubo virtual.
- Se han creado los tours virtuales
- Se han ensamblado todos los tours virtuales en una página que les da soporte.

### Tours virtuales
Veamos la creación de un tour virtual realizando  por ejemplo la biblioteca de "Turismo y Finanzas". Todos los ficheros y carpetas implicados tienen como prefijo "TURFIN".
Si vamos a la carpeta donde residen las fotos vemos que se han realizado 15 fotografías de esta biblioteca, desde TURFIN_1 hasta TURFIN_15.
En la carpeta code crearemos los ficheros necesarios para realizar el tour por esta Biblioteca.

```
mkdir code/TURFIN
mkdir code/TURFIN/
touch code/TURFIN/escenas.csv 
echo "idEscena,title,basePath" > code/TURFIN/escenas.csv
touch code/TURFIN/hotspotinfo.csv
echo "idEscena,pitch,yaw,text,URL" > code/TURFIN/hotspotinfo.csv
touch code/TURFIN/hotspotescenas.csv
echo "idEscena,sceneId,pitch,yaw,text,targetYaw,targetPitch" > code/TURFIN/hotspotescenas.csv
```
El procedimiento consiste ahora en ir rellenando cada uno de estos tres ficheros con la información pertinente, es importante conocer como define Pannellun cada uno de los elementos que usa y por ello para una comprensión plena no estaría demás visitar su documentación.

Como ya tenemos las fotografias desensambladas para visualizarlas y encontrar los puntos singulares usaremos el fichero "TURFIN_VisorEscenas.html".




## Han realizado esta aplicación

    - Álvaro Carmona Núñez
    - Patricia Serrano Angorilla
    - Gonzalo Martínez Fernández 
    - Javier Escudero Infante

