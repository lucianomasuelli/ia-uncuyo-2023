install.packages("rpart")
install.packages("rpart.plot")

library(rpart)
library(rpart.plot)

datos_arbolado <- read.csv("datos_submuestreados.csv")
datos_prueba <- read.csv("arbolado-mza-dataset-test.csv")

modelo_arbol <- rpart(inclinacion_peligrosa ~ seccion + altura, 
                      data = datos_arbolado, 
                      method = "class")


#rpart.plot(modelo_arbol)
#text(modelo_arbol)


predicciones <- predict(modelo_arbol, newdata = datos_prueba, type = "class")

# Crear un nuevo dataframe con 'id' y las predicciones
resultados <- data.frame(id = datos_prueba$id, inclinacion_peligrosa_predicha = predicciones)

# Visualizar los primeros registros del dataframe 'resultados'
head(resultados)

# Guardar el dataframe 'resultados' en un archivo CSV
write.csv(resultados, "resultados_prediccion.csv", row.names = FALSE)


