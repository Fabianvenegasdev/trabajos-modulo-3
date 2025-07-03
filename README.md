# trabajos-modulo-3

En este archivo se encuentran los ejercicios de aplicacion de la leccion 1 a la 6, ademas de el proyecto de preparacion de datos python para el portafolio.


Documento Resumen del Flujo de Trabajo
Proyecto Integrador: Preparación de Datos con Python
Objetivo:
El objetivo principal del proyecto fue desarrollar un proceso automatizado y eficiente para la obtención, limpieza, transformación, análisis y estructuración de datos utilizando las librerías NumPy y Pandas . El dataset final debe estar listo para ser utilizado en análisis o modelos predictivos.

Lección 1: La librería NumPy
Descripción:
Se generaron datos ficticios de clientes y transacciones usando arrays de NumPy , aprovechando su velocidad y capacidad vectorizada.

Tareas realizadas:
Generación de datos sintéticos (IDs, edades, compras, montos).
Uso de funciones aleatorias (np.random) para simular comportamiento real.
Guardado de datos en formato .npz para usarlos posteriormente en Pandas.
Resultado:
Archivo datos_ficticios.npz creado, que servirá como insumo inicial para la siguiente etapa.

 Lección 2: La librería Pandas
 Descripción:
Los datos sintéticos se cargaron en un DataFrame de Pandas para realizar una exploración inicial.

 Tareas realizadas:
Conversión de arrays NumPy a DataFrame.
Visualización de primeras y últimas filas.
Cálculo de estadísticas descriptivas.
Aplicación de filtros condicionales.
Exportación a CSV para uso futuro.
Resultado:
Archivo datos_pandas.csv generado, con datos básicamente limpios pero aún sin tratamiento avanzado.

 Lección 3: Obtención de datos desde archivos
Descripción:
Se integraron múltiples fuentes de datos: CSV, Excel y web.

 Tareas realizadas:
Carga del CSV previo.
Importación de datos adicionales desde archivo Excel (clientes_ecommerce.xlsx).
Extracción de datos de una tabla web pública (ejemplo: PIB por país desde Wikipedia).
Unificación de datasets mediante merge() y concat().
Resultado:
Archivo datos_consolidados.csv creado, conteniendo información combinada de varias fuentes.

Lección 4: Manejo de valores perdidos y outliers
Descripción:
Se identificaron y corrigieron problemas de calidad en los datos: nulos y valores atípicos.

Tareas realizadas:
Identificación de valores nulos con isnull().sum().
Imputación de valores con mediana (numéricos) y moda (categóricos).
Detección de outliers mediante IQR.
Eliminación de registros extremos y visualización opcional con matplotlib/seaborn.
Resultado:
Archivo datos_limpios.csv guardado, ya sin valores nulos ni outliers extremos.

Lección 5: Data Wrangling
 Descripción:
Transformación y enriquecimiento del dataset mediante técnicas avanzadas.

 Tareas realizadas:
Eliminación de duplicados.
Renombrado de columnas para legibilidad.
Creación de nuevas variables derivadas (Gasto_Promedio, Nivel_Cliente).
Discretización de variables (Rango_Edad).
Uso de .apply() y funciones personalizadas.
 Resultado:
Archivo datos_optimizados.csv generado, con datos transformados y enriquecidos.

 Lección 6: Agrupamiento y pivotado de datos
 Descripción:
Organización y reestructuración del dataset para facilitar el análisis.

 Tareas realizadas:
Uso de .groupby() para calcular métricas por segmentos de clientes.
Creación de tablas dinámicas con pivot_table().
Despivotado de datos con melt() para formato largo.
Combinación adicional si fuera necesario con merge() y concat().
Exportación final del dataset en formatos CSV y Excel.

Dataset Final
 Estructura:
El dataset final contiene las siguientes columnas clave:


## Diccionario de Datos

| **Columna**       | **Descripción**                                           |
|-------------------|-----------------------------------------------------------|
| `ID`              | Identificador único del cliente                           |
| `Nombre`          | Nombre del cliente                                        |
| `Edad`            | Edad del cliente                                          |
| `Ciudad`          | Ciudad de residencia                                      |
| `Total_Compras`   | Número total de compras                                   |
| `Monto_Total`     | Dinero invertido en total                                 |
| `Rango_Edad`      | Categorización por edad (Joven, Adulto, etc.)             |
| `Nivel_Cliente`   | Clasificación según frecuencia de compras                 |
| `Gasto_Promedio`  | Promedio de gasto por compra                              |

Hallazgos clave del proceso
NumPy es ideal para generar datos sintéticos gracias a su alto rendimiento numérico.
Pandas permite manipular datos de forma flexible y rápida , especialmente útil para exploración, limpieza y transformación.
La integración de múltiples fuentes es posible con herramientas como read_csv, read_excel y read_html.
Los valores nulos y outliers afectan significativamente los resultados , por lo que su manejo es crítico.
Las técnicas de Data Wrangling y agrupamiento son esenciales para descubrir patrones ocultos y crear variables útiles para análisis posteriores.
 Conclusiones
Este proyecto permitió consolidar habilidades fundamentales en el procesamiento de datos:

Carga y exploración inicial con Pandas
Limpieza de datos: imputación, eliminación de outliers, corrección de inconsistencias
Transformaciones avanzadas: discretización, creación de columnas derivadas
Organización de datos: agrupamiento, pivotado, fusión de fuentes
Como resultado, se entregó un conjunto de datos limpio, confiable y estructurado , listo para ser usado en reportes de negocio, dashboards o modelado predictivo.


## Entregables Finales

| **Archivo**                            | **Descripción**                                   |
|----------------------------------------|---------------------------------------------------|
| `lesson1.py`                           | Generación de datos ficticios                     |
| `lesson2.py`                           | Exploración básica de datos                       |
| `lesson3.py`                           | Integración de múltiples fuentes                  |
| `lesson4.py`                           | Limpieza de datos                                 |
| `lesson5.py`                           | Transformación avanzada                           |
| `lesson6.py`                           | Reestructuración y exportación final              |
| `README.md`                            | Este documento resumen                            |

Recomendaciones y posibles mejoras
-Automatizar el proceso completo : envolverlo en una función modular reusable.
-Integrarlo en una aplicación interactiva : con Streamlit o Dash.
-Ampliar el alcance a más fuentes : incluir APIs, JSON o bases de datos SQL.
-Aplicar validación cruzada de datos : verificar consistencia entre fuentes.
-Agregar control de versiones de datos : con DVC o scripts de migración.