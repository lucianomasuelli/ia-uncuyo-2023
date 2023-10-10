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
