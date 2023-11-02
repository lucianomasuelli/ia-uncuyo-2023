list.files()
# Cargar el conjunto de datos
datos_train <- read.csv("arbolado-mendoza-dataset-train.csv")

library(ggplot2)
library(dplyr)

# Crear un gráfico de barras
ggplot(datos_train, aes(x = factor(inclinacion_peligrosa))) +
  geom_bar(fill = "blue", color = "black", alpha = 0.7) +
  labs(title = "Distribución de Inclinación Peligrosa",
       x = "Inclinación Peligrosa",
       y = "Frecuencia") +
  scale_x_discrete(labels = c("No", "Sí")) +  # Cambiar etiquetas del eje x
  theme_minimal()

# Filtrar los datos para inclinacion_peligrosa = 1
datos_filtrados <- datos_train %>%
  filter(inclinacion_peligrosa == 1)

# Crear el gráfico
ggplot(datos_filtrados, aes(x = factor(inclinacion_peligrosa), fill = factor(seccion))) +
  geom_bar(position = "dodge", color = "black", alpha = 0.7) +
  labs(title = "Distribución de Inclinación Peligrosa por Sección",
       x = "Secciones",
       y = "Frecuencia inclinación peligrosa") +
  scale_x_discrete(labels = c("")) +  # Cambiar etiquetas del eje x
  theme_minimal()

# Gráfico de porcentaje de árboles con inclinación peligrosa por sección
datos_train %>%
  group_by(seccion) %>%
  summarise(total_arboles = n()) %>%  # Contar la cantidad de árboles por sección
  left_join(datos_train %>%
              filter(inclinacion_peligrosa == 1) %>%
              group_by(seccion) %>%
              summarise(datos_filtrados = n()),
            by = "seccion") %>%
  mutate(porcentaje_inclinacion_peligrosa = datos_filtrados / total_arboles * 100) %>%
  ggplot(aes(x = factor(seccion), y = porcentaje_inclinacion_peligrosa)) +
  geom_bar(stat = "identity", fill = "blue", color = "black", alpha = 0.7) +
  geom_text(aes(label = sprintf("%.1f%%", porcentaje_inclinacion_peligrosa)),
            vjust = -0.5, size = 3, color = "black") +
  labs(title = "Porcentaje de árboles con inclinación peligrosa por sección",
       x = "Secciones",
       y = "Porcentaje") +
  scale_x_discrete(labels = datos_train$nombre_seccion, breaks = datos_train$seccion) +
  theme_minimal()


