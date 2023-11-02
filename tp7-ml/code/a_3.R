# Cargar el conjunto de datos
datos_train <- read.csv("/home/luciano/Documentos/Facultad/3ro/2_semestre/Inteligencia_artificial_1/ia-uncuyo-2023/tp7-ml/data/arbolado-mendoza-dataset-train.csv")

library(ggplot2)

# Generar histogramas con diferentes números de bins
num_bins <- c(10, 20, 30)

for (n in num_bins) {
  p <- ggplot(datos_train, aes(x = circ_tronco_cm, fill = factor(inclinacion_peligrosa))) +
    geom_histogram(binwidth = (max(datos_train$circ_tronco_cm) - min(datos_train$circ_tronco_cm)) / n, color = "black", alpha = 0.7, position = "identity") +
    labs(title = paste("Histograma de circ_tronco_cm con", n, "bins"),
         x = "Circunferencia del Tronco (cm)",
         y = "Frecuencia") +
    scale_fill_manual(values = c("blue", "red")) +
    theme_minimal()
  print(p)
}


# Definir los puntos de corte para las categorías
cut_points <- c(0, 125, 250, 375, Inf)  # Define los puntos de corte

# Crear la nueva variable categórica
datos_train$circ_tronco_cm_cat <- cut(datos_train$circ_tronco_cm, 
                                      breaks = cut_points, 
                                      labels = c("bajo", "medio", "alto", "muy alto"), 
                                      include.lowest = TRUE)

# Guardar el nuevo dataframe como arbolado-mendoza-dataset-circ_tronco_cm-train.csv
write.csv(datos_train, file = "/home/luciano/Documentos/Facultad/3ro/2_semestre/Inteligencia_artificial_1/ia-uncuyo-2023/tp7-ml/data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv", row.names = FALSE)
