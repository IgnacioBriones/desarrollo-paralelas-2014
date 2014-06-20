
El código secreto de la biblia
==

Con este programa uster podrá analizar el código secreto de cualquier libro, incluida la biblia. Solo debe contar de un cluster e instalación de MPI en cada uno de sus nodos.
=======
funciones que formatean pdf y doc a txt, dejandolo listo para busquedas correspondientes


Forma de uso por linea de comando
==

La linea de comandos es muy simple de usar (si está acostumbrado a usar lineas de comandos), tenemos 4 formas de usar la linea de comandos y estas dependeran de lo que usted quiera obtener de nuestro algoritmo.

* Serial explícito

ejemplo:
<pre><code class="shell">
python shellSerialExplicit.py  ./files/biblia.pdf "ola k ase"
</code></pre>

Considere que siempre las frases deben ir encerradas entre comillas para que python considere que es solo un argumento y no varios.

* Serial implicito

El serial implícito hace busquedas en un diccionario en la cual se encuentran las palabras relacionadas a las más reveladores y terroríficas predicciones de nuestro tiempo

<pre><code class="shell">
python shellSerialImplicit.py  ./files/biblia.pdf
</code></pre>
* Paralelo explícito
<pre><code class="shell">
mpiexec -n 4 --hostfile ./hostfile python shellParallelExplicit.py ./files/biblia.pdf "ola k ase"
</code></pre>

* Paraleo implícito
<pre><code class="shell">
mpiexec -n 4 --hostfile ./hostfile python shellParallelImplicit.py ./files/biblia.pdf
</code></pre>


Todos estos algoritmos generarán en la consola un archivo json que puede ser consumido con el lenguaje servidor que usted prefiera.





Para serial
==

Si usted quiere hacer uso de esto debe
* Clonar o descargar el repositorio en .zip
* Bajar cualquier .pdf de la red y renombrarlo "c.pdf", se debe dejar el archivo pdf en la carpeta examples
* Una vez situado en .../examples ejecutar desde la consola de comandos: "python explicitapdf.py -frase-"


Para el paralelo
==
