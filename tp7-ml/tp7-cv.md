## Ejercicio 7
### Código de funciones `create_folds` y `cross_validation`
```
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
```
### Resultados de las métricas

|                    | Accuracy         | Precision       | Sensitivity     | Specificity      |
|----------------------|--------------------|-------------------|-------------------|--------------------|
| Mean               | 0.618461538461539  | 0.482688770184126 | 0.666827564643315 | 0.587099579721795  |
| Standard deviation | 0.0366304241192837 | 0.22963655451808  | 0.116309010771132 | 0.0541635011109496 |
