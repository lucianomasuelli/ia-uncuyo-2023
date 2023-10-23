# Cargar el conjunto de datos
list.files()
datos <- read.csv("arbolado-mza-dataset.csv")

# Establecer una semilla para reproducibilidad
set.seed(123)

# Seleccionar el 20% de los datos para validación de manera aleatoria
indices_validacion <- sample(nrow(datos), nrow(datos)*0.2)
datos_validacion <- datos[indices_validacion, ]
datos_train <- datos[-indices_validacion, ]

# Guardar los conjuntos de datos en archivos CSV
write.csv(datos_validacion, "arbolado-mendoza-dataset-validation.csv", row.names = FALSE)
write.csv(datos_train, "arbolado-mendoza-dataset-train.csv", row.names = FALSE)

