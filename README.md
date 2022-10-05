# Analisis-Algoritmos
Programas y Actividades relacionadas al curso de Análisis de Algoritmos -> PUJ

## Coeficientes Binomiales

Los coeficientes binomiales, números combinatorios o combinaciones son números estudiados en combinatoria que corresponden al número de formas en que se puede extraer subconjuntos a partir de un conjunto dado.

El programa ```coefBin.py``` contiene 3 funciones para calcular el coeficiente binomial usando 3 tecnicas diferentes, a los cuales se les pasa como argumentos dos enteros ```n``` y ```k``` que corresponden a los términos de la combinación.

    * ```binomialC1``` usa la técnica recursiva.
    * ```binomialC2``` usa la técnica de programación dinámica.
    * ```binomialC3``` usa la técnica de programación dinámica mejorada.

La funcion ```getData``` retorna un dataframe que tiene como columnas: ```n``` y ```k```, el resultado de los coeficientes binomiales y los respectivos tiempos de ejecucion para cada tecnica de calculo. Pide como parametros ```N_input``` que corresponde a un arreglo formado por los enteros que se ingresan desde la consola.

La funcion ```extraerDF``` extrae un subconjunto de datos del dataframe general, tomando en cuenta el valor de ```n```.

finalmente la funcion ```graficar``` retorna la gráfica esperada **almacenada de forma local**.