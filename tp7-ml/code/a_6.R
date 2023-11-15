
get_confusion_matrix <- function(dataframe) {
  predictions <- dataframe$prediction_class
  actual <- dataframe$inclinacion_peligrosa
  
  # Crear una tabla de contingencia
  confusion_table <- table(predictions, actual)
  
  # Convertir la tabla en una matriz
  confusion_matrix <- as.matrix(confusion_table)
  
  #agregar fila de ceros
  confusion_matrix <- rbind(confusion_matrix, c(0,0))
  
  
  return(confusion_matrix)
}

# Función para calcular la exactitud (accuracy)
calcular_exactitud <- function(confusion_matrix) {
  TP <- confusion_matrix[1,1]
  TN <- confusion_matrix[2,2]
  FP <- confusion_matrix[2,1]
  FN <- confusion_matrix[1,2]
  
  accuracy <- (TP + TN) / (TP + TN + FP + FN)
  return(accuracy)
}

# Función para calcular la precisión (precision)
calcular_precision <- function(confusion_matrix) {
  TP <- confusion_matrix[1,1]
  FP <- confusion_matrix[2,1]
  
  precision <- TP / (TP + FP)
  return(precision)
}

# Función para calcular la sensibilidad (sensitivity o recall)
calcular_sensibilidad <- function(confusion_matrix) {
  TP <- confusion_matrix[1,1]
  FN <- confusion_matrix[1,2]
  
  sensitivity <- TP / (TP + FN)
  return(sensitivity)
}

# Función para calcular la especificidad (specificity)
calcular_especificidad <- function(confusion_matrix) {
  TN <- confusion_matrix[2,2]
  FP <- confusion_matrix[2,1]
  
  specificity <- TN / (TN + FP)
  return(specificity)
}

source("/home/luciano/Documentos/Facultad/3ro/2_semestre/Inteligencia_artificial_1/ia-uncuyo-2023/tp7-ml/code/a_5.R")
source("/home/luciano/Documentos/Facultad/3ro/2_semestre/Inteligencia_artificial_1/ia-uncuyo-2023/tp7-ml/code/a_4.R")
source("/home/luciano/Documentos/Facultad/3ro/2_semestre/Inteligencia_artificial_1/ia-uncuyo-2023/tp7-ml/metricas.R")

data <- read.csv("/home/luciano/Documentos/Facultad/3ro/2_semestre/Inteligencia_artificial_1/ia-uncuyo-2023/tp7-ml/data/arbolado-mendoza-dataset-validation.csv")

new_dataframe01 <- biggerclass_classifier(data)
new_dataframe02 <- random_classifier(random_prediction, data)

confusion_matrix01 <- get_confusion_matrix(new_dataframe01)
confusion_matrix02 <- get_confusion_matrix(new_dataframe02)

print("Biggest class classifier")
print("Matriz de confusión para biggerclass_classifier")
print(confusion_matrix01)
print("Exactitud para biggerclass_classifier")
print(calcular_exactitud(confusion_matrix01))
print("Precisión para biggerclass_classifier")
print(calcular_precision(confusion_matrix01))
print("Sensibilidad para biggerclass_classifier")
print(calcular_sensibilidad(confusion_matrix01))
print("Especificidad para biggerclass_classifier")
print(calcular_especificidad(confusion_matrix01))

print("Random classifier")
print("Matriz de confusión para random_classifier")
print(confusion_matrix02)
print("Exactitud para random_classifier")
print(calcular_exactitud(confusion_matrix02))
print("Precisión para random_classifier")
print(calcular_precision(confusion_matrix02))
print("Sensibilidad para random_classifier")
print(calcular_sensibilidad(confusion_matrix02))
print("Especificidad para random_classifier")
print(calcular_especificidad(confusion_matrix02))



