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
