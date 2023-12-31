# Ejercicio 1
## a) El tamaño de la muestra n es extremadamente grande y el número de predictores p es pequeño.
En este caso, un método flexible tendrá un mejor desempeño que uno inflexible, ya que un gran tamaño de muestra beneficia su capacidad para aprender patrones más complejos y sutiles debido a su mayor capacidad para ajustarse a relaciones no lineales. Por otro lado, a un método inflexible puede jugarle en contra el gran tamaño de muestra, llevándolo a un sobreajuste y provocando un peor desempeño.
## b) El número de predictores p es muy grande, y el número de observaciones n es pequeño.
Este caso es inverso al anterior, un método flexible tendrá un peor desempeño debido a que al tener un numero bajo de observaciones en relación a la cantidad de predictores no podrá explotar su capacidad de apredizaje. Esto lo puede llevar también a un sobreajuste. Los métodos inflexibles, al ser menos susceptibles al sobreajuste, pueden ser más apropiados en esta situación, ya que tienden a ser menos sensibles a la alta dimensionalidad de los datos.
## c) La relación entre los predictores y la respuesta es altamente no lineal.
Esperaríamos que un método flexible tenga un mejor desempeño ya que los inflexibles asumen relaciones lineales y pueden perderse patrones importantes y no ser capaces de ajustarse adecuadamente a la complejidad de los datos. Los métodos flexibles tienen la capacidad de adaptarse a relaciones no lineales.
## d) La varianza de los términos de error, es extremadamente alta.
En este caso los métodos flexibles pueden sufrir un sobreajuste ya que tratarían de adaptarse a la gran variabilidad, por otro lado, los métodos inflexibles al ser más simples y menos sensibles a la complejidad de los datos, pueden tener un mejor desempeño ante una alta varianza de error.

# Ejercicio 2
## a)
Es un caso de regresión ya que en base a varios factores queremos obtener una correlación con el comportamiento de un factor (salario) que es una variable continua. Es un problema de inferencia.  
`p` es `500` y `n` es `4`.  
## b)
Este es un problema de predicción, donde se utilizaría un método de clasificación ya que se quiere predecir si el producto será exitoso o no.  
`p` es `20` y `n` es `14`.
## c)
Es un caso de predicción donde se utilizará un método de regresión porque se quiere predecir un valor continuo.  
`p` es `52` y `n` es `4`.

# Ejercicio 5
Cuando se utilizan métodos de regresión o clasificación, una implementación con un método mas flexible puede ser una buena opción si el problema requiere encontrar patrones más complejos, puede adaptarse a relaciones no lineales, capturando patrones que métodos inflexibles no encontrarían. Esto lleva a un mejor ajuste de los datos de entrenamiento y por ende a un rendimiento superior en la predicción.  
La desventaja principal de estos métodos flexibles, es que son muy propensos al sobreajuste, adaptandose de sobremanera a los datos de entrenamiento y afectando el desempeño con datos reales.  
Un enfoque menos flexible puede ser útil cuando se necesita una buena interpretabilidad del modelo para entender los resultados, ya que los flexibles pueden llegar a ser muy difíciles de interprear en algunos casos. Tambén tienen la ventaja de que el sobreajuste puede ser mejor controlado para tener una mejor generalización.  
La desventaja de estos enfoques es su incapacidad para adaptarse a datos complejos o para obtener predicciones complejas.

# Ejercicio 6
El enfoque paramétrico implica hacer suposiciones específicas sobre la forma funcional de la relación entre las variables y asume un número fijo de parámetros que caracterizan dicha relación. Estos modelos, como la regresión lineal, son más simples y fáciles de interpretar, pero su eficacia depende de la precisión de las suposiciones realizadas, lo que puede limitar su capacidad para capturar patrones complejos en los datos.  
Por otro lado, el enfoque no paramétrico no impone suposiciones específicas sobre la forma de la relación y permite que la complejidad del modelo se adapte a la complejidad de los datos. Estos modelos son más flexibles y pueden manejar relaciones no lineales y estructuras de datos más complejas. Aunque pueden ser más robustos en ciertos escenarios, la falta de suposiciones explícitas puede dificultar la interpretación del modelo y requerir conjuntos de datos más grandes para obtener estimaciones precisas.

# Ejercicio 7
## a) Distancia euclidiana
1)  sqrt(0^2 + 3^2 + 0^2) = 3   
2) 	sqrt(2^2 + 0^2 + 0^2) = 2   
3) 	sqrt(0^2 + 1^2 + 3^2) = sqrt(10)  
4) 	sqrt(0^2 + 1^2 + 2^2) = sqrt(10)  
5) 	sqrt((-1)^2 + 0^2 + 1^2) = sqrt(2)    
6) 	sqrt(1^2 + 1^2 + 1^2) = sqrt(3)

## b) 
El vecino mas cercano es la observación 5 ya que tiene una distancia euclidiana de sqrt(2) y una valor de la variable Y = Green, por lo tanto la predicción sera Y = Green.

## c)
Los 3 vecinos mas cercanos son 5,6 y 2. Dos tienen valor Y = Red y uno de Y = Green por lo tanto, como hay mas probabilidad de pertenecer a la clase Red, el valor será Y = Red.

## d)
Si la frontera de decisión de Bayes es altamente no lineal, esperaríamos que el mejor valor para K sea pequeño, ya que esto hará que el modelo sea mas flexible y pueda encontrar características más complejas.

