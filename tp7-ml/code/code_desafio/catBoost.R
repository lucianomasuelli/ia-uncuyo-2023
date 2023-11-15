library(xgboost)

data <- read.csv("Data/arbolado-mza-dataset.csv")
data_test <- read.csv("Data/arbolado-mza-dataset-test.csv")

# Transformamos los datos categoricos a numericos
data$especie <- as.numeric(factor(data$especie))
data$altura <- as.numeric(factor(data$altura))
data$diametro_tronco <- as.numeric(factor(data$diametro_tronco))
data$nombre_seccion <- as.numeric(factor(data$nombre_seccion))

X <- data[, c("especie", "altura", "circ_tronco_cm", "diametro_tronco", "lat", "long","seccion")]
X <- as.matrix(X)
Y <- data$inclinacion_peligrosa
Y <- as.matrix(Y)

# Supongamos que tenemos una matriz de características 'X' y un vector de etiquetas 'y'
train_data <- xgb.DMatrix(data = X, label = Y)

# Definir parámetros del modelo
param <- list(
  objective = "reg:squarederror",  # Para regresión
  max_depth = 6,
  eta = 0.3,
  nrounds = 100
)

# Entrenar el modelo
model <- xgboost(params = param, data = train_data, nrounds = 100, verbose = 0)

data_test_matriz <- as.matrix(data_test)

# Supongamos que tenemos datos de prueba en una matriz 'X_test'
result <- xgb.DMatrix(data = data_test_matriz)

# Realizar predicciones
predictions <- predict(model, newdata = test_data)