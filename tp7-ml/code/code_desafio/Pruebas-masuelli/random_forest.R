# Cargar el conjunto de datos
datos_train <- read.csv("datos_submuestreados.csv")
datos_evaluacion <- read.csv("arbolado-mza-dataset-test.csv")

library(randomForest)

# Separar las características (variables independientes) y la variable objetivo
X <- datos_train[, c("altura", "circ_tronco_cm", "long", "lat")]
y <- datos_train$inclinacion_peligrosa

# Entrenar el modelo Random Forest
set.seed(42)  # Para reproducibilidad
modelo_rf <- randomForest(y = as.factor(y), x = X, ntree = 100)

# Ver el resumen del modelo
print(modelo_rf)

# Predecir con el conjunto de entrenamiento
predicciones <- predict(modelo_rf, X)

# Calcular la precisión en el conjunto de entrenamiento
precision <- sum(predicciones == y) / length(y)
cat("Precisión en el conjunto de entrenamiento:", precision, "\n")


# Separar las características y la variable objetivo del conjunto de evaluación
X_evaluacion <- datos_evaluacion[, c("altura", "circ_tronco_cm", "long", "lat")]
y_evaluacion <- datos_evaluacion$inclinacion_peligrosa

# Predecir con el conjunto de evaluación
predicciones_evaluacion <- predict(modelo_rf, X_evaluacion)

# Crear un data.frame con las columnas id y inclinacion_peligrosa
resultados <- data.frame(id = datos_evaluacion$id, inclinacion_peligrosa = predicciones_evaluacion)

resultados$inclinacion_peligrosa <- as.numeric(as.character(resultados$inclinacion_peligrosa))

# Guardar los resultados en un archivo CSV
write.csv(resultados, "resultados_rf.csv", row.names = FALSE)
