
<div align="center">
    <img src="images\imagenIntecol.PNG"><img>
</div>
<h1 align="center">App de escritorio para la adquisición de imágenes de la cámara FLIR</h1>

<p>
    <b>Realizado por:</b> Ing. Jaimen Aza
</p>

<h2>Correr la aplicación</h2>

<h3>Configurar el entorno virtual</h3>

<p>
    Trabajaremos sobre un entorno virtual de python3.8 para no tener problemas con las dependecias. Para esto crearemos el entorno y luego instalaremos las librerias que se encuentran en el archivo requirements.txt
</p>

<h3>Creando el entorno virtual </h3>

<p>Para crear el entorno virtual ejecutar la siguiente linea</p>

```
    python3.8 -m venv flirApp-env
```

<p>el nombre puede cambiar y si se desea eliminar el entorno simplemente basta con eliminar la carpeta que se creó.</p>
<p>Para activar el entorno ejecutar:<p>

```
    cd flirApp-env\Scripts\activate.bat
```

<p>ahora la consola cmd cambiará y se ubicara sobre el entorno virtual llamado flirApp-env. A partir de aquí, todo se trabajará con la versión de python con la que creamos el entorno virtual, ya no será necesario poner '3.8' despues del pip o de python para instalar librerias o ejecutar scripts.</p>

<p>El entorno virtual creado anteriormente es OPCIONAL, sin embargo se recomienda usarlo para tener cada proyecto con sus respctivas librerias. Si no se desea trabajar en el entorno virtual, omitir los pasos anteriores</p>

<h3>Descargar repositorio</h3>
<p>Si se trabajó con entorno virtual el repositorio debe ser clonado dentro de este.</p>

```
    git clone https://github.com/Jaza00/DesktopApp-FlirCamera.git
```

<h3>Instalar dependencias</h3>
<p>primero se debe instalar el whl de PySpin que se encuentra adjunto mediante el comando:</p>

```
    cd whlSpinnaker
    python -m pip install spinnaker_python-2.3.0.77-cp38-cp38-win_amd64.whl
```

<p>Despues instalar todas las librerias necesarias con la linea:</p>

```
    pip install -r requirements.txt
```

<p>por último ejecutar la app con el comando</p>

```
    cd src
    python app.py
```

<div align="center">
    <img src="images\capturaWindow.PNG" width="800"><img>
</div>


<p>Crear .exe</p>

```
pyinstaller --hidden-import PySide2.QtXml example.py

pyinstaller --onefile --windowed --hidden-import PySide2.QtXml app.py

```