# 🎯 Desafío: Tratamiento de Valores Nulos y Outliers
# Este script realiza las siguientes operaciones:
# - Carga del dataset desde CSV.
# - Exploración inicial (primeras filas, tipos de datos, valores nulos).
# - Imputación de valores faltantes (numéricos y categóricos).
# - Detección y manejo de outliers mediante IQR.
# - Exportación del dataset limpio.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("✅ Paso 1: Importando el dataset...")

# 🔹 Cargar los datos desde el archivo CSV
# Nota: usamos punto y coma (;) como separador
df = pd.read_csv("LigaEspanola2023-2024-Resultados (1).csv", sep=";")

# Mostrar las primeras 5 filas para explorar el contenido
print("\n🔹 Primeras 5 filas del DataFrame:")
print(df.head())

# Obtener información general del DataFrame
print("\n🔹 Información general del DataFrame:")
print(df.info())

# Verificar estadísticas descriptivas
print("\n🔹 Estadísticas descriptivas:")
print(df.describe(include='all'))

# Verificar la cantidad de valores nulos por columna
print("\n🔹 Cantidad de valores nulos por columna:")
print(df.isnull().sum())

# ==========================================================================
# 2️⃣ Manejo de valores perdidos (nulos)
# ==========================================================================

print("\n✅ Paso 2: Tratando valores nulos...")

# Separar columnas numéricas y categóricas
columnas_numericas = df.select_dtypes(include=np.number).columns
columnas_categoricas = df.select_dtypes(exclude=np.number).columns

# Imputar valores numéricos: reemplazar con la mediana
for col in columnas_numericas:
    df[col].fillna(df[col].median(), inplace=True)

# Imputar valores categóricos: reemplazar con la moda
for col in columnas_categoricas:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Verificar que no haya más valores nulos
print("\n🔹 Valores nulos después de imputar:")
print(df.isnull().sum())

# ==========================================================================
# 3️⃣ Detección y tratamiento de outliers
# ==========================================================================

print("\n✅ Paso 3: Detectando y tratando outliers...")

# Seleccionar solo columnas numéricas para análisis de outliers
df_numeric = df[columnas_numericas]

# Función para detectar y tratar outliers usando IQR
def tratar_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    print(f"\n🔹 Columna '{column}':")
    print(f"   - Limite inferior: {limite_inferior}")
    print(f"   - Limite superior: {limite_superior}")

    # Contar cuántos outliers hay
    outliers = df[(df[column] < limite_inferior) | (df[column] > limite_superior)]
    print(f"   - Número de outliers detectados: {len(outliers)}")

    # Estrategia 1: Eliminar outliers
    df_sin_outliers = df[(df[column] >= limite_inferior) & (df[column] <= limite_superior)]

    return df_sin_outliers

# Aplicar función a cada columna numérica
for col in df_numeric.columns:
    df = tratar_outliers(df, col)

# Opcional: Visualización de boxplots para ver outliers antes y después
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[columnas_numericas])
plt.title("Boxplot de columnas numéricas tras limpieza")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================================================
# 4️⃣ Validación de datos limpios
# ==========================================================================

print("\n✅ Paso 4: Validando datos limpios...")

# Verificar que no haya valores nulos
print("\n🔹 Comprobación final de valores nulos:")
print(df.isnull().sum().sum())  # Debe mostrar 0

# Verificar distribución de datos
print("\n🔹 Distribución de datos tras limpieza:")
print(df[columnas_numericas].describe())

# Graficar histogramas para ver la distribución de los datos
df[columnas_numericas].hist(bins=20, figsize=(12, 6))
plt.tight_layout()
plt.show()

# ==========================================================================
# 5️⃣ Exportación de datos
# ==========================================================================

print("\n✅ Paso 5: Exportando datos limpios...")

# Guardar el DataFrame limpio en un nuevo archivo CSV
df.to_csv("liga_espanola_resultados_limpios.csv", index=False)

print("\n🎉 ¡Desafío completado exitosamente!")
print("El dataset limpio ha sido guardado como 'liga_espanola_resultados_limpios.csv'")