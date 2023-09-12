## Media y desviación estandar para cada algoritmo
Se ejecutó cada algoritmo 30 veces en el mismo escenario aleatorio de 50x50.
![media-y-desviacion](https://github.com/lucianomasuelli/ia-uncuyo-2023/assets/83616746/2fb4b17e-6d52-4bb5-b810-d832f74c582e)
## Boxplot
![boxplot_algorithms](https://github.com/lucianomasuelli/ia-uncuyo-2023/assets/83616746/9ae91495-c6e1-4c54-8f6a-92fc6a8b055c)

Creo que el algoritmo más adecuado para resolver el problema es el BFS, ya que llega a una solución sin recorrer una gran cantidad de estados. 
Dado que se trata de un problema en el que no hay un costo asociado al cambio de un estado a otro, y el entorno no es muy extenso, el BFS es la mejor opción. Aunque UCS tiene un comportamiento similar al BFS, 
realiza algunas operaciones innecesarias al buscar el camino con el costo más pequeño.
