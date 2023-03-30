# Minería de datos Hoja de trabajo 4: Segmentación de Especies con Cluster Analysis

## Autores
- Guillermo Furlán
- Luis Pedro Gonzalez Aldana
## Repositorio
https://github.com/LPELCRACK896/DM-hdt4-iris-clustering.git
## Resumen
El conjunto de datos de la flor Iris es uno de los más populares para el Aprendizaje de Máquina (ML). Si no lo conocen, pueden leer sobre él en:

https://en.wikipedia.org/wiki/Iris_flower_data_set

El conjunto de datos iris.csv tiene cuatro variables:

- sepal length (longitud del sépalo),
- sepal width (ancho del sépalo),
- petal length (longitud del pétalo),
- petal width (ancho del pétalo).
## Sección 1:

1. Visualicen los datos para ver si pueden detectar algunos grupos. Ayuda: utilicen la forma del sépalo:
2. Creen 2 "clusters" utilizando K_Means Clustering y grafiquen los resultados.
3. Estandaricen los datos e intenten el paso 2, de nuevo. ¿Qué diferencias hay, si es que lo hay?
4. Utilicen el método del "codo" para determinar cuantos "clusters" es el ideal. (prueben un rango de 1 a 10)
5. Basado en la gráfica del "codo" realicen varias gráficas con el número de clusters (unos 3 o 4 diferentes) que Uds creen mejor se ajusten a los datos.
6. Comparen sus soluciones con los datos reales, archivo: iris-con-respuestas.csv

Obviamente solo hay tres especies, porque ese es el archivo de datos reales! ¿Funcionó el clustering con la forma del sépalo?

## Sección 2:

Repitan el proceso pero ahora utilizando la forma del pétalo. Respondan a las mismas preguntas. 

## Sección 3:

Utilicen la librería "kneed" y vean si el resultado coincide con el método del "codo" que hicieron manualmente. ¿A que podría deberse la diferencia, si la hay? ¿Les dió el número correcto de clusters, comparado a los datos reales?

Basado en los resultado que tuvieron, ¿A qué conclusiones llegaron?