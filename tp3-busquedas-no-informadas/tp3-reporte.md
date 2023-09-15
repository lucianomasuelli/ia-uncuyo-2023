## Media y desviación estandar para cada algoritmo
Se ejecutó cada algoritmo 30 veces en el mismo escenario aleatorio de 100x100.
![media_desviacion](https://github.com/lucianomasuelli/ia-uncuyo-2023/assets/83616746/0be95fc8-e495-4f08-9148-d2a278f65c21)

## Boxplot
![boxplot](https://github.com/lucianomasuelli/ia-uncuyo-2023/assets/83616746/84e5ffd9-968f-4c93-b580-38e739da7821)

Creo que el algoritmo más adecuado para resolver el problema es BFS, ya que en promedio llega a una solución recorriendo menos estados que DFS.
Aunque la diferencia de estados recorridos con DFS no es muy grande, BFS además encuentra un camino óptimo para llegar al objetivo (el camino mas corto en este caso) 
mientras que DFS no.
Dado que se trata de un problema en el que no hay un costo asociado al cambio de un estado a otro, y el entorno no es muy extenso, BFS es la mejor opción, aunque UCS tiene un comportamiento similar al BFS, realiza algunas operaciones innecesarias al buscar el camino con el costo más pequeño.
