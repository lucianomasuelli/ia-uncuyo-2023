source("/home/luciano/Documentos/Facultad/3ro/2_semestre/Inteligencia_artificial_1/ia-uncuyo-2023/tp7-ml/metricas.R")
library(rpart)

desicion_tree_classifier <- function(data, test_data) {
  # Crear el modelo
  train_formula<-formula(inclinacion_peligrosa~altura+
                           circ_tronco_cm+
                           lat+long+
                           seccion)
  
  model <- rpart(train_formula, data = data, method = "class")
  
  # Predecir la clase de los datos de test
  predictions <- predict(model, test_data, type = "class")
  
  return(predictions)
}

create_folds <- function(data, k) {
  folds <- list()
  fold_size <- floor(nrow(data) / k)
  for (i in 1:k) {
    start <- (i - 1) * fold_size + 1
    end <- min(i * fold_size, nrow(data))
    indices_fold <- start:end
    name_fold <- paste0("Fold", i)
    folds[[name_fold]] <- indices_fold
  }
  return(folds)
}

# Cross validation with decision tree
cross_validation <- function(data, num_folds) {
  folds <- create_folds(data, num_folds)
  accuracy <- list()
  precision <- list()
  sensitivity <- list()
  specificity <- list()
  for (i in 1:num_folds) {
    test_indices <- folds[[paste0("Fold", i)]]  #seleccionar el fold i
    train_indices <- unlist(folds[setdiff(names(folds), paste0("Fold", i))])  #seleccionar los demas folds
    test_data <- data[test_indices,]
    train_data <- data[train_indices,]
    
    predictions <- desicion_tree_classifier(train_data, test_data)
    confusion_matrix <- confusion_matrix(predictions, test_data)
    accuracy[[i]] <- calcular_exactitud(confusion_matrix)
    precision[[i]] <- calcular_precision(confusion_matrix)
    sensitivity[[i]] <- calcular_sensibilidad(confusion_matrix)
    specificity[[i]] <- calcular_especificidad(confusion_matrix)
  }
  return(list(accuracy, precision, sensitivity, specificity))
}

confusion_matrix <- function(predictions, test_data) {
  actual <- test_data$inclinacion_peligrosa
  
  # Crear una tabla de contingencia
  confusion_table <- table(predictions, actual)
  
  # Convertir la tabla en una matriz
  confusion_matrix <- as.matrix(confusion_table)
  
  return(confusion_matrix)
}

data <- read.csv("/home/luciano/Documentos/Facultad/3ro/2_semestre/Inteligencia_artificial_1/ia-uncuyo-2023/tp7-ml/data/datos_submuestreados.csv")
data$especie <- factor(data$especie)
data <- data[order(data$id), ]

cross_validation_results <- cross_validation(data, 10)

accuracy <- cross_validation_results[[1]]
precision <- cross_validation_results[[2]]
sensitivity <- cross_validation_results[[3]]
specificity <- cross_validation_results[[4]]

print("Accuracy")
print(accuracy)
mean_accuracy <- mean(unlist(accuracy))
sd_accuracy <- sd(unlist(accuracy))
print(paste0("Mean accuracy: ", mean_accuracy))
print(paste0("Standard deviation accuracy: ", sd_accuracy))

print("Precision")
print(precision)
mean_precision <- mean(unlist(precision))
sd_precision <- sd(unlist(precision))
print(paste0("Mean precision: ", mean_precision))
print(paste0("Standard deviation precision: ", sd_precision))

print("Sensitivity")
print(sensitivity)
mean_sensitivity <- mean(unlist(sensitivity))
sd_sensitivity <- sd(unlist(sensitivity))
print(paste0("Mean sensitivity: ", mean_sensitivity))
print(paste0("Standard deviation sensitivity: ", sd_sensitivity))

print("Specificity")
print(specificity)
mean_specificity <- mean(unlist(specificity))
sd_specificity <- sd(unlist(specificity))
print(paste0("Mean specificity: ", mean_specificity))
print(paste0("Standard deviation specificity: ", sd_specificity))




