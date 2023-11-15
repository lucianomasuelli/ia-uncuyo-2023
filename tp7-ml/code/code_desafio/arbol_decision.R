library(rpart.plot)
library(rpart)
library(dplyr)

# Carga el dataset
arbolado_test <- read.csv("Data/arbolado-mza-dataset-test.csv")
arbolado_dataset <-  read.csv("Data/arbolado-mza-dataset.csv")

# Filtrar todos los arboles con inclinacion peligrosa
muestra_inclinacion_peligrosa <- arbolado_dataset[arbolado_dataset$inclinacion_peligrosa == 1, ]

# Filtrar algunos arboles con inclinacion no peligrosa (la misma cantidad que exita de inclinacion peligrosa para balancear)
muestra_inclinacion_no_peligrosa <- arbolado_dataset %>% filter(inclinacion_peligrosa == 0) %>% sample_n(3500)

# Unir los dos conjuntos de datos
arbolado_dataset_filtrado <- rbind(muestra_inclinacion_peligrosa, muestra_inclinacion_no_peligrosa)

set.seed(123)  # Establece una semilla para reproducibilidad

# Especifica la fórmula para el modelo
arbolado_dataset.formula <- "inclinacion_peligrosa ~ id + altura + circ_tronco_cm + diametro_tronco + long + lat + seccion + nombre_seccion + area_seccion"

# Crea el modelo de árbol de decisión
modelo_arbol <- rpart(arbolado_dataset.formula, data = arbolado_dataset_filtrado, method = "class")

arbolado_test$inclinacion_peligrosa <- 0

# Predicciones en el conjunto de prueba
predicciones <- predict(modelo_arbol, arbolado_test, type = "class")

resultado <- data.frame(arbolado_test$id, predicciones)

resultado <- resultado %>% rename("ID" = "arbolado_test.id")

resultado <- resultado %>% rename("inclinacion_peligrosa" = "predicciones")

head(resultado)

# Utiliza write.csv2() para guardar el dataframe en un archivo CSV con punto y coma como delimitador
write.csv(resultado, file = "resultados.csv", row.names = FALSE,)

# Evalúa el rendimiento
matriz_confusion <- table(observado = arbolado_test$inclinacion_peligrosa, predicho = predicciones)
precision <- (matriz_confusion[1, 1] + matriz_confusion[2, 2]) / sum(matriz_confusion)
sensibilidad <- matriz_confusion[2, 2] / (matriz_confusion[2, 1] + matriz_confusion[2, 2])
especificidad <- matriz_confusion[1, 1] / (matriz_confusion[1, 2] + matriz_confusion[1, 1])

# Visualiza el árbol de decisión
rpart.plot(modelo_arbol)