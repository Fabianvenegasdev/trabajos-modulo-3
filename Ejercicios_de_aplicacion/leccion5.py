# 🎯 Desafío: Data Wrangling con Pandas
# Este script realiza limpieza, transformación y exportación de datos del dataset de la Liga Española.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("🔹 1. Cargando el dataset...")
# Importar el archivo CSV (usamos ';' como separador)
df = pd.read_csv("LigaEspanola2023-2024-Resultados (1).csv", sep=";")

# Mostrar primeras filas para exploración inicial
print("\nPrimeras 5 filas:")
print(df.head())

# Verificar información general del DataFrame
print("\nInformación del DataFrame:")
print(df.info())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe(include='all'))

# Verificar valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# ==========================================================================
# 🔁 2. Ordenamiento, selección y permutación aleatoria
# ==========================================================================

print("\n🔹 2. Realizando ordenamiento y selección de columnas...")

# Seleccionar solo las columnas relevantes
columnas_relevantes = ["Fecha", "Local", "Vistante", "Goles Local", "Goles Visitante", "Total Goles", "Resultado"]
df_seleccionado = df[columnas_relevantes]

# Renombrar columnas para mejorar legibilidad
df_seleccionado.rename(columns={"Vistante": "Visitante"}, inplace=True)

# Ordenar por fecha (de más reciente a más antiguo)
df_ordenado = df_seleccionado.sort_values(by="Fecha", ascending=False)

# Mezclar filas aleatoriamente (permutación aleatoria)
df_aleatorio = df_ordenado.sample(frac=1, random_state=42).reset_index(drop=True)

print("\nDataFrame después de seleccionar y ordenar:")
print(df_aleatorio.head())

# ==========================================================================
# 🧹 3. Detección y eliminación de duplicados
# ==========================================================================

print("\n🔹 3. Buscando y eliminando registros duplicados...")

# Identificar duplicados considerando todas las columnas
duplicados = df_aleatorio.duplicated()
print(f"Número de duplicados antes de eliminar: {duplicados.sum()}")

# Eliminar duplicados
df_sin_duplicados = df_aleatorio.drop_duplicates()

print(f"Número de registros antes: {len(df_aleatorio)}")
print(f"Número de registros después: {len(df_sin_duplicados)}")

# ==========================================================================
# 🔄 4. Reemplazo de valores y discretización
# ==========================================================================

print("\n🔹 4. Corrigiendo inconsistencias y creando categorías...")

# Reemplazar valores inconsistentes en 'Resultado'
df_sin_duplicados["Resultado"] = df_sin_duplicados["Resultado"].replace({
    "Home": "Local",
    "Away": "Visitante",
    "Tie": "Empate"
})

print("\nValores únicos en 'Resultado' después:", df_sin_duplicados["Resultado"].unique())

# Discretizar la columna 'Total Goles' en rangos
bins = [0, 2, 4, 6, 10]
labels = ['Bajo', 'Moderado', 'Alto', 'Muy Alto']
df_sin_duplicados['Nivel_Goles'] = pd.cut(df_sin_duplicados['Total Goles'], bins=bins, labels=labels, include_lowest=True)

print("\nEjemplo de discretización en 'Nivel_Goles':")
print(df_sin_duplicados[['Total Goles', 'Nivel_Goles']].head())

# ==========================================================================
# ➕ 5. Enriquecimiento del dataset
# ==========================================================================

print("\n🔹 5. Agregando nuevas columnas y transformando datos...")

# Función personalizada: tipo de goles (par/impar)
def tipo_goles(total):
    return "Par" if total % 2 == 0 else "Impar"

# Aplicar con .apply()
df_sin_duplicados['Tipo_Goles'] = df_sin_duplicados['Total Goles'].apply(tipo_goles)

# Usar lambda para calcular diferencia absoluta de goles
df_sin_duplicados['Diferencia_Goles'] = df_sin_duplicados.apply(
    lambda row: abs(row['Goles Local'] - row['Goles Visitante']), axis=1
)

print("\nNuevo DataFrame con columnas agregadas:")
print(df_sin_duplicados[['Total Goles', 'Tipo_Goles', 'Diferencia_Goles']].head())

# ==========================================================================
# 🧩 6. Manipulación de la estructura del DataFrame
# ==========================================================================

print("\n🔹 6. Redimensionando y modificando estructura...")

# Eliminar columna innecesaria
df_final = df_sin_duplicados.drop(columns=['Total Goles'])

# Filtrar partidos con diferencia de goles mayor a 1
df_filtrado = df_final[df_final['Diferencia_Goles'] > 1]

print("\nDatos filtrados (Diferencia de goles > 1):")
print(df_filtrado.head())

# ==========================================================================
# 💾 7. Exportación de datos
# ==========================================================================

print("\n🔹 7. Exportando datos procesados...")

# Guardar en formato CSV y Excel
df_filtrado.to_csv("liga_espanola_resultados_limpios.csv", index=False)
df_filtrado.to_excel("liga_espanola_resultados_limpios.xlsx", index=False)

print("\n✅ ¡Desafío completado exitosamente!")
print("Archivo guardado como:")
print(" - liga_espanola_resultados_limpios.csv")
print(" - liga_espanola_resultados_limpios.xlsx")