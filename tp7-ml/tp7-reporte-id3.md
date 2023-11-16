## Resultados de evaluación sobre tennis.csv
![decision_tree](https://github.com/lucianomasuelli/ia-uncuyo-2023/assets/83616746/e70a4df1-8c33-4ec9-bd6b-a4fd9192b97e)

## Estrategias de árboles de decisión para datos de tipo real
Los árboles de decisión aplicados a datos de tipo real utilizan diversas estrategias para manejar la complejidad y garantizar una buena generalización a nuevos datos.  
Cuando se tienen datos continuos se utilizan estrategias para dividir los datos de manera que maximicen la homogeneidad dentro de los nodos.  
Las siguientes son algunas estrategias utilizadas:  
### Partición Binaria:
La estrategia más simple es la partición binaria, donde se selecciona un umbral y los datos se dividen en dos conjuntos: aquellos que son menores o iguales al umbral y aquellos que son mayores. 
El árbol de decisión evalúa diferentes umbrales y selecciona el que maximiza la ganancia de información (en clasificación) o reduce la varianza (en regresión).

### Selección del Mejor Umbral:
En cada nodo del árbol, se realiza una búsqueda exhaustiva para encontrar el umbral que optimiza la métrica de división. 
Esto implica evaluar varios umbrales posibles y seleccionar aquel que maximiza la ganancia de información o reduce la varianza. Esta estrategia es efectiva, pero puede ser computacionalmente costosa.

### Criterios de Impureza Ponderada:
Para datos continuos, se utilizan criterios de impureza ponderada, como la varianza en problemas de regresión o el índice de Gini en problemas de clasificación. 
Estos criterios consideran la distribución de las etiquetas en cada subconjunto después de la división, ponderando la impureza por la proporción de datos en cada subconjunto.

### Particionamiento Multi-Nivel:
Algunas implementaciones permiten particionar los datos en más de dos niveles. 
En lugar de simplemente dividir en "menor o igual" y "mayor", se pueden tener múltiples ramas, lo que permite un enfoque más flexible y ajustado a la naturaleza continua de los datos.
