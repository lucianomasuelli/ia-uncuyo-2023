# Trabajo Práctico 6
## 1) Formulación CSP para Sudoku
### Variables
El conjunto de variables contiene todas posiciones del tablero donde se pueden colocar números.  
X = {(0,0), (1,1), ..., (8,8)}  

### Dominio
D = {1,2,3,4,5,6,7,8,9}

### Restricciones
C = {(x,y) != (x,w), (y,x) != (w,x), (i,j) != (i',j')}  
con y!=w,  
(i,j) y (i',j') en el mismo bloque.

## 2) 
![ej2](https://github.com/lucianomasuelli/ia-uncuyo-2023/assets/83616746/90d8a418-fc2d-4a00-a1d7-73e01b23f635)


## 3) 
El peor caso de AC-3 teniendo un grafo de restricciones con forma de árbol se da cuando se deben verificar y propagar toda las restricciones entre todas las variables. Entonces si tenemos un CSP con n variables y un dominio de tamaño d se deberán analizar los n-1 arcos y para cada uno de estos se deben revisar todos los pares de valores posibles entre las variables involucradas, lo que lleva a O(d²) operaciones por arco. En total, la inicialización tomará O(nd²) operaciones. Luego, durante la fase de propagación, AC-3 revisa cada arco una sola vez. Para cada arco, se revisa el dominio de las variables involucradas y se elimina cualquier valor inconsistente. En el peor caso, esto también toma O(d²) operaciones por arco. La complejidad total de la propagación es O(nd²).  
Finalmente la complejidad total de AC-3 en un árbol estructurado CSP es O(n²d).

## 4)
Supongamos que llevamos contadores eficientes para cada par de variables, que mantiene la cuenta de cuantos valores del dominio de una variable son consistentes con el valor de la otra variable.  
Entonces, en la fase de inicialización, para cada par de variables (Xk​,Xi​), se deben verificar todas las restricciones entre ellas. En el peor caso, esto toma O(n⋅d²) operaciones, donde n es el número de variables y d es el tamaño del dominio más grande. Además, durante la inicialización, podemos calcular los contadores eficientes en O(n⋅d²) operaciones.  
Durante la propagación, si se elimina un valor del dominio de una variable, la complejidad de la actualización es de O(n²d²) ya que en el peor de los casos todas las variables están conectadas, entonces para cada variable se analizan todos los arcos y para cada arco se actualiza el contador correspondiente a cada valor del dominio.

## 5)
Supongamos que tenemos un CSP cuyo grafo de restricciones es un árbol. Esto significa que no hay ciclos en el grafo de restricciones y que cualquier par de variables está conectado por un único camino.  
Supongamos que tenemos una restricción n-aria en este CSP. Para demostrar que la 2-consistencia implica n-consistencia, vamos a utilizar inducción.  
- Caso base (n = 2): Si tenemos una restricción binaria, entonces 2-consistencia ya es suficiente para garantizar n-consistencia, ya que 2-consistencia asegura que no hay conflictos entre los valores permitidos por la restricción.  
- Paso inductivo (n > 2): Supongamos que para un CSP con restricciones n-arias donde n = k, la 2-consistencia implica k-consistencia. Ahora consideremos un CSP con una restricción (k+1)-aria.  
Dado que el grafo de restricciones es un árbol, podemos ver que cualquier par de variables en una restricción (k+1)-aria están conectadas por un camino único. Podemos dividir esta restricción en k restricciones binarias utilizando el principio del camino único.  
Si aplicamos 2-consistencia a cada una de estas k restricciones binarias, entonces podemos asegurar que no habrá conflictos entre los valores permitidos por estas restricciones. Como asumimos que 2-consistencia implica k-consistencia, sabemos que cada una de estas k restricciones binarias será k-consistente.  
Dado que cada restricción binaria es k-consistente, podemos concluir que la restricción (k+1)-aria es k-consistente, ya que para cada asignación válida de valores a k variables, siempre habrá al menos un valor en el dominio de la última variable que satisface la restricción.  
Por lo tanto, hemos demostrado que la 2-consistencia implica n-consistencia para un CSP cuyo grafo de restricciones es un árbol.
  
La demostración anterior muestra que si aplicamos 2-consistencia en un CSP con un grafo de restricciones que es un árbol, entonces podemos garantizar la n-consistencia para cualquier restricción n-aria en ese CSP.  
Esto es suficiente porque garantizar la n-consistencia para todas las restricciones n-arias en el CSP asegura que no habrá conflictos entre los valores permitidos por estas restricciones, lo que significa que cualquier asignación válida de valores a las variables será una solución válida para el CSP.
