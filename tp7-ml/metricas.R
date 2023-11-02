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