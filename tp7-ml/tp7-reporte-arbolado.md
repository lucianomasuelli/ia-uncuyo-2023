# Predicción de peligrosidad del arbolado público de Mendoza
## Preprocesamiento
Al momento de hacer trabajar con el dataset se notó un gran desbalance en la variable que calsifica la inclinación de las muestras como peligrosas o no. Para trabajar este problema se decidió hacer un 
proceso de normalización mediante un algoritmo de `Undersampling` encargado de crear un nuevo dataset que incluye todos los elementos `con inclinación peligrosa` (clase minoritaria) y selecciona la misma 
cantidad de elementos de la clase `sin inclinación peligrosa` de forma aleatoria.  
Se le aplicaron pesos a las clases, dandole un meyor peso a la clase minoritaria (con inclinación peligorsa) brindandole mayor relevancia en el modelo.  
Finalmente se eliminaron algunas variables del dataset, como `id`, `ultima_modificacion`, `area_seccion` y `nombre_seccion` ya que consideramos que no aportaban al reconocimiento de la inclinación peligrosa.

## Resultados en conjuntos de validación
![resultados_predicciones](https://github.com/lucianomasuelli/ia-uncuyo-2023/assets/83616746/be69f3d4-ef08-45d3-80ec-7fb8f0bfbf71)

## Resultados obtenidos en Kaggle

![Resultados_kaggle](https://github.com/lucianomasuelli/ia-uncuyo-2023/assets/83616746/c560429e-9091-4083-8389-ab40c60a97b2)

## Descripción del algoritmo
Para la creacion del modelo predictivo se hizo uso del algoritmos Random Forest, el cual fue programado en R utilizando la libreria original "randomForest" y la libreria "dplyr" para el preprocesamiento de los datos. El algoritmo fue configurado con los siguientes parametros:

    ntree: 700
    mtry: 6
    classwt: matriz_costo (matrix(c(0, 5, -1, 1), nrow = 2, byrow = TRUE))

Posteriormente, los resultados obtenidos con dicho modelo son asginados de la siguiente manera:

    Probalidad < 0.5: No posee inclinacion peligrosa
    Probalidad >= 0.5: Posee inclinacion peligrosa
