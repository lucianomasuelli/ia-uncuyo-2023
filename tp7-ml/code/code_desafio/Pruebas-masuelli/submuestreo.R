
datos_original <- read.csv("arbolado-mza-dataset.csv")

# Contar el número de instancias de cada clase
table(datos_original$inclinacion_peligrosa)

# Realizar submuestreo de la clase mayoritaria (inclinacion_peligrosa = 0)
library(dplyr)
datos_submuestreados <- datos_original %>%
  filter(inclinacion_peligrosa == 1) %>%
  bind_rows(datos_original %>% filter(inclinacion_peligrosa == 0) %>%
              sample_n(sum(datos_original$inclinacion_peligrosa == 1)))

# Verificar el nuevo conjunto de datos
table(datos_submuestreados$inclinacion_peligrosa)

# Guardar el nuevo conjunto de datos con submuestreo en un archivo CSV
write.csv(datos_submuestreados, "datos_submuestreados.csv", row.names = FALSE)
