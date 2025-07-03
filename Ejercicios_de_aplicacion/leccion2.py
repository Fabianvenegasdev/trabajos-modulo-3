# 📚 Desafío: Análisis de Datos de la Liga Española con Pandas
# Este script realiza diversas operaciones de carga, limpieza, análisis y transformación
# de datos utilizando Pandas, partiendo del archivo CSV con resultados de la Liga Española 2023-2024.

import pandas as pd

# ==========================================================================
# 1️⃣ Carga y exploración de datos
# ==========================================================================

# Cargar los datos desde el archivo CSV. El separador es punto y coma (;)
df = pd.read_csv("LigaEspanola2023-2024-Resultados.csv", sep=";")

print("✅ Paso 1: Datos cargados correctamente.")

# Mostrar las primeras 5 filas para entender cómo se estructuran los datos
print("\n🔹 Primeras 5 filas del DataFrame:")
print(df.head())

# Mostrar las últimas 5 filas
print("\n🔹 Últimas 5 filas del DataFrame:")
print(df.tail())

# Mostrar información general del DataFrame (tipos de datos, valores nulos, etc.)
print("\n🔹 Información general del DataFrame:")
print(df.info())

# Estadísticas descriptivas generales
print("\n🔹 Estadísticas descriptivas:")
print(df.describe(include='all'))  # 'include=all' incluye columnas categóricas también

# ==========================================================================
# 2️⃣ Manejo de valores nulos y duplicados
# ==========================================================================

# Identificar y mostrar cantidad de valores nulos por columna
print("\n🔹 Valores nulos por columna:")
print(df.isnull().sum())

# Imputar valores faltantes:
# - Si la columna es numérica, reemplazamos con la media.
# - Si es categórica, usamos la moda (el valor más frecuente).
for col in df.columns:
    if df[col].dtype == 'object':
        df[col].fillna(df[col].mode()[0], inplace=True)  # Moda para categóricas
    else:
        df[col].fillna(df[col].mean(), inplace=True)     # Media para numéricas

# Eliminar filas duplicadas si existen
df.drop_duplicates(inplace=True)

# Confirmar que no hay duplicados después de eliminarlos
print("\n🔹 Número de filas duplicadas después de eliminar:", df.duplicated().sum())

print("✅ Paso 2: Valores nulos imputados y duplicados eliminados.")

# ==========================================================================
# 3️⃣ Filtrado y selección de datos
# ==========================================================================

# Filtrar partidos donde el total de goles sea mayor a 5
partidos_altos_goles = df[df["Total Goles"] > 5]
print("\n🔹 Partidos con más de 5 goles:")
print(partidos_altos_goles[["Fecha", "Local", "Vistante", "Total Goles"]].head())

# Seleccionar solo columnas relevantes para el análisis
columnas_relevantes = ["Fecha", "Local", "Vistante", "Goles Local", "Goles Visitante", "Resultado"]
df_relevante = df[columnas_relevantes]
print("\n🔹 Columnas seleccionadas para análisis:")
print(df_relevante.head())

# Ordenar por fecha (descendente)
df_ordenado = df.sort_values(by="Fecha", ascending=False)
print("\n🔹 Datos ordenados por fecha (más recientes primero):")
print(df_ordenado.head())

print("✅ Paso 3: Datos filtrados, seleccionados y ordenados.")

# ==========================================================================
# 4️⃣ Agrupamiento y operaciones estadísticas
# ==========================================================================

# Agrupar por equipo local y calcular promedio de goles anotados
goles_promedio_local = df.groupby("Local")["Goles Local"].mean()
print("\n🔹 Promedio de goles anotados por equipo local:")
print(goles_promedio_local.sort_values(ascending=False).head())

# Función de agregación personalizada: media, mediana y cantidad de partidos
agregacion_personalizada = df.groupby("Local")["Goles Local"].agg(["mean", "median", "count"])
print("\n🔹 Agregación personalizada (media, mediana, cantidad) de goles por equipo local:")
print(agregacion_personalizada.sort_values(by="mean", ascending=False).head())

print("✅ Paso 4: Agrupamientos realizados exitosamente.")

# ==========================================================================
# 5️⃣ Creación de nuevas columnas y transformación de datos
# ==========================================================================

# Crear nueva columna: diferencia de goles absoluta
df["Diferencia Goles"] = abs(df["Goles Local"] - df["Goles Visitante"])

# Convertir la columna "Fecha" a tipo datetime para facilitar análisis temporal
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Renombrar algunas columnas para mejorar la legibilidad
df.rename(columns={
    "Vistante": "Visitante",
    "Goles Local": "Goles_Local",
    "Goles Visitante": "Goles_Visitante"
}, inplace=True)

# Mostrar el DataFrame final con cambios aplicados
print("\n🔹 DataFrame final con nuevas columnas y nombres mejorados:")
print(df[["Fecha", "Local", "Visitante", "Goles_Local", "Goles_Visitante", "Diferencia Goles"]].head())

print("✅ Paso 5: Nuevas columnas creadas y transformaciones aplicadas.")

# ==========================================================================
# 🎁 Plus: Exportar los datos limpios a otros formatos
# ==========================================================================

# Exportar a Excel
df.to_excel("liga_espanola_resultados_limpios.xlsx", index=False)

# Exportar a JSON
df.to_json("liga_espanola_resultados_limpios.json", orient="records")

print("\n🎁 Archivos exportados a formato Excel y JSON.")

# ==========================================================================
# ✅ ¡Fin del script!
# ==========================================================================

print("\n🎉 ¡Análisis completado con éxito!")
print("Los archivos procesados han sido guardados en tu carpeta actual.")