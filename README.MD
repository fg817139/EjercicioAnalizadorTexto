# Ejercicio Analizador de Texto
Para este ejercicio vas a suponer que trabajas para un proyecto donde te asignan la
tarea de construir un analizador de texto que ayude a obtener información sobre el texto
que escriben los autores de blogs.

Para el diseño del analizador se definieron las siguientes tres reglas para el análisis.

## 1. Palabras más usadas
Esta regla debe analizar el texto y devolver una lista con las 10 palabras más usadas. Este
análisis debe tener en cuenta lo siguiente:

- No se debe diferenciar entre mayúsculas y minúsculas. Por ejemplo, las palabras "usted" y
"Usted" deben contar como la misma palabra.
- En el listado deben aparecer primero las palabras con mayor frecuencia, sin embargo, no 
existe un orden específico para listar las palabras que tengan la misma frecuencia.
- Se asume que el texto solo tiene líneas separadas por un salto de línea simple `\n`.

> ### Ejemplo
> Dado el siguiente texto para analizar:
> 
> ***Hola, este es un ejemplo para que usted practique. Usted puede tomar este texto y
> usarlo como su caso de prueba.***
> 
> El resultado del análisis de palabras más usadas debería ser
> 
> 1. este
> 2. usted
> 3. hola
> 4. es
> 5. un
> 6. ejemplo
> 7. para
> 8. que
> 9. practique
> 10. puede
> 
> En este caso, también podría aparecer primero ***usted*** que ***este***, ya
> que ambas palabras aparecen dos veces en el texto

## 2. Conteo de palabras
Esta regla debe analizar el texto e indicar cuántas palabras contiene, sin importar
si son palabras repetidas.

> ### Ejemplo
> Dado el siguiente texto para analizar:
> 
> ***Hola, este es un ejemplo para que usted practique. Usted puede tomar este texto y
> usarlo como su caso de prueba.***
> 
> El resultado del análisis debería indicar que el texto tiene ***21*** palabras.

## 3. Tiempo de lectura
Esta regla debe analizar el texto e indicar cuánto tiempo le tomaría a un usuario
leerlo. Para esto se debe tener en cuenta lo siguiente:

- La tasa promedio de lectura es de ***238*** palabras por minuto
- Se obtiene el total de palabras del texto
- Se divide el total de palabras por 238 y la parte entera de esa división son los minutos.
- Para obtener los segundos, la parte decimal se multiplica por 60 y se toma la parte entera del resultado.

> ### Ejemplo
> Dado un texto que contiene ***783*** palabras. 
> 
> Realizamos la división
> 
> 783 / 238 = 3.289
> 
> Los minutos serían la parte entera de la división. En este caso ***3 minutos***.
> 
> Los segundos serían 0.289 * 60 = 17.34, de lo cual tomamos solo la parte entera.
> En este caso serían ***17 segundos***
>
> El resultado del análisis sería que para leer un texto de 783 palabras, un usuario
> se demora 3 minutos y 17 segundos.

Con base en los requisitos del problema, el arquitecto de software del proyecto realizó el
siguiente diseño para el analizador de texto:

![Modelo de clases](./assets/diagrama_clases.png)

Tu misión es implementar el modelo planteado por el arquitecto de software. Para lograrlo
debes tener en cuenta lo siguiente:

1. La clase `ReglaAnalisis` es una clase abstracta y su método `analizar` es igualmente abstracto.
2. El método inicializador de la clase `ReglaAnalisis` recibe el nombre de la regla como parámetro y
se lo asigna al atributo `nombre`.
3. El método `_separar_palabras` de la clase `ReglaAnalisis` implementa la lógica para separar las palabras
del texto recibido como parámetro y devolverlas como una lista. Las palabras no deben incluir puntuación. Por ejemplo, 
si se separan las palabras del texto `Hola, ¿cómo estás?`, el resultado sería la lista `['Hola', 'cómo', 'estás']`.
Cuando el texto está vacío `''`, el método retorna una lista vacía `[]`.
>**Pista:** puedes utilizar los métodos `lower()`, `split()`, `strip()` y `replace()` de la clase `str`.
4. La clase `ReglaPalabraMasUsada` debe inicializarse pasando como parámetro a la superclase el nombre 
`'palabras_ordenadas'`. El método `analizar` debe retornar una lista de str con las 10 palabras más usadas del texto.  
>**Pista:** puedes utilizar la función `sorted` que sirve para ordenar un iterable.</mark>
> 
> Por ejemplo, si tuvieras el siguiente diccionario
> 
> `my_dict = {'hola': 1, 'es': 2, 'frío': 1, 'mucho': 3}`
> 
> y quisieras ordenarlo por valor de mayor a menor, para que quedara así:
> 
> `{'mucho': 3, 'es': 2, 'hola': 1, 'frío': 1}`
> 
> Podrías utilizar la función `sorted` de la siguiente manera:
> 
> `mi_dict_ordenado = sorted(mi_dict, key=lambda item: item[1], reverse=True)`
> 
> Puedes consultar la documentación de la función `sorted` aquí:
> https://docs.python.org/es/3/library/functions.html#sorted
5. La clase `ReglaConteoPalabras` debe inicializarse pasando como parámetro a la superclase el nombre 
`'conteo_palabras'`. El método `analizar` debe retornar un entero que indica la cantidad de palabras del texto.
6. La clase `ReglaTiempoLectura` debe inicializarse pasando como parámetro a la superclase el nombre
`'tiempo_lectura'`. Esta clase define una constante llamada `TASA_LECTURA` de tipo entero y con el valor 238. Además, 
el método `analizar` debe retornar una tupla de dos enteros, donde el primer valor indica los 
minutos y el segundo valor indica los segundos que se demora una persona en leer el texto. Para este cálculo debes
seguir las indicaciones que se dan en la descripción de la regla de tiempo de lectura.
> **Pista:** puedes utilizar la función `modf` del módulo `math` para obtener la parte entera y la parte decimal 
> de un número
7. La clase `Analizador` tiene un atributo `reglas` que es una lista de objetos de la clase `ReglaAnalisis`.
En la inicialización de la clase se debe agregar un objeto de cada una de las tres reglas de análisis a la lista
de reglas. El método `procesar` debe recorrer la lista de reglas y debe retornar un diccionario donde las claves son
los nombres de las reglas y los valores son los resultados de aplicar la regla (llamar el método `analizar`).

Para realizar la actividad, puedes clonar este repositorio e implementar el código en el archivo `analizador.py` que
se encuentra en el paquete `analizador.modelo`

## Ten en cuenta

* El proyecto incluye un conjunto de pruebas que puedes utilizar para verificar el cumplimiento de los 
requisitos establecidos. Para ejecutar las pruebas, debes instalar la dependencia pytest.
* Para que las pruebas funcionen adecuadamente debes implementar el código respetando los nombres y la 
definición de las clases y los métodos que se presentan en el diagrama.
* La evaluación del ejercicio se hará con base en el cumplimiento de los requisitos que arrojen las 
pruebas. Por lo tanto, cualquier fallo en las pruebas debido a nombres mal escritos o que no concuerden
con el modelo dado se considerará como un requisito no cumplido, afectando la calificación del examen.
