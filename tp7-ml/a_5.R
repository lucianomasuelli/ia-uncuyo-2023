biggerclass_classifier <- function(datos) {
  # Obtener la clase mayoritaria
  clase_mayoritaria <- as.numeric(names(sort(table(datos$inclinacion_peligrosa), decreasing = TRUE)[1]))
  
  # Asignar siempre la clase mayoritaria en la nueva columna
  datos$prediction_class <- clase_mayoritaria
  
  return(datos)
}

confusion_matrix <- function(dataframe) {
  predictions <- dataframe$prediction_class
  actual <- dataframe$inclinacion_peligrosa
  
  # Crear una tabla de contingencia
  confusion_table <- table(predictions, actual)
  
  # Convertir la tabla en una matriz
  confusion_matrix <- as.matrix(confusion_table)
  

  print(confusion_matrix)
  return(confusion_matrix)
}

#data <- read.csv("/home/luciano/Documentos/Facultad/3ro/2_semestre/Inteligencia_artificial_1/ia-uncuyo-2023/tp7-ml/data/arbolado-mendoza-dataset-validation.csv")

#new_dataframe <- biggerclass_classifier(data)

# Mostrar los primeros 10 resultados
#head(new_dataframe, 10)

#confusion_matrix(new_dataframe)

#print("Matriz de confusión para biggerclass_classifier")
#print(confusion_matrix(new_dataframe))