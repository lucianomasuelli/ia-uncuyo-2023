random_prediction <- function(data) {
  # Generar valores aleatorios entre 0 y 1
  data$prediction_prob <- runif(nrow(data))
  return(data)
}

random_classifier <- function(random_prediction, data) {
  new_dataframe <- random_prediction(data)
  # Convertir la probabilidad en 0 o 1
  new_dataframe$prediction_class <- ifelse(new_dataframe$prediction_prob > 0.5, 1, 0)
  return(new_dataframe)
}

#data <- read.csv("/home/luciano/Documentos/Facultad/3ro/2_semestre/Inteligencia_artificial_1/ia-uncuyo-2023/tp7-ml/data/arbolado-mendoza-dataset-validation.csv")

#new_dataframe <- random_classifier(random_prediction, data)

# Mostrar los primeros 10 resultados
#head(new_dataframe, 10)

#predictions <- new_dataframe$prediction_class
#actual <- new_dataframe$inclinacion_peligrosa

# Crear una tabla de contingencia
#confusion_table <- table(predictions, actual)

# Convertir la tabla en una matriz
#confusion_matrix <- as.matrix(confusion_table)

# Imprimir la matriz de confusión
#print(confusion_matrix)

