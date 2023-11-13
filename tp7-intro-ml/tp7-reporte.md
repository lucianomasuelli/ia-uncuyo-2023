# Ejercicio 1
## a) El tamaño de la muestra n es extremadamente grande y el número de predictores p es pequeño.
En este caso, un método flexible tendrá un mejor desempeño que uno inflexible, ya que un gran tamaño de muestra beneficia su capacidad para aprender patrones más complejos y sutiles debido a su mayor capacidad para ajustarse a relaciones no lineales. Por otro lado, a un método inflexible puede jugarle en contra el gran tamaño de muestra, llevándolo a un sobreajuste y provocando un peor desempeño.
## b) El número de predictores p es muy grande, y el número de observaciones n es pequeño.
Este caso es inverso al anterior, un método flexible tendrá un peor desempeño debido a que al tener un numero bajo de observaciones en relación a la cantidad de predictores no podrá explotar su capacidad de apredizaje. Esto lo puede llevar también a un sobreajuste. Los métodos inflexibles, al ser menos susceptibles al sobreajuste, pueden ser más apropiados en esta situación, ya que tienden a ser menos sensibles a la alta dimensionalidad de los datos.
## c) La relación entre los predictores y la respuesta es altamente no lineal.
Esperaríamos que un método flexible tenga un mejor desempeño ya que los inflexibles asumen relaciones lineales y pueden perderse patrones importantes y no ser capaces de ajustarse adecuadamente a la complejidad de los datos. Los métodos flexibles tienen la capacidad de adaptarse a relaciones no lineales.
## d) La varianza de los términos de error, es extremadamente alta.
En este caso los métodos flexibles pueden sufrir un sobreajuste ya que tratarían de adaptarse a la gran variabilidad, por otro lado, los métodos inflexibles al ser más simples y menos sensibles a la complejidad de los datos, pueden tener un mejor desempeño ante una alta varianza de error.


