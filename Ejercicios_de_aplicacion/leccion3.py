# 📚 Desafío: Manipulación de Datos con Pandas
# Este script realiza las siguientes operaciones:
# - Carga de datos desde archivos CSV y Excel.
# - Visualización básica del contenido (primeras filas).
# - Verificación de tipos de datos y valores nulos.
# - Selección y transformación de columnas.
# - Eliminación de filas con valores críticos faltantes.
# - Conversión de tipos de datos (ejemplo: fechas).
# - Lectura de tablas desde la web.
# - Exportación de datos procesados a formatos CSV y Excel.

import pandas as pd

# ==========================================================================
# 1️⃣ Carga de datos desde archivos
# ==========================================================================

# Importar archivo CSV con datos de resultados de la Liga Española
# Nota: El archivo usa punto y coma (;) como separador
csv_path = "LigaEspanola2023-2024-Resultados (1).csv"
df_csv = pd.read_csv(csv_path, sep=";")

print("✅ Paso 1: Archivo CSV cargado correctamente.")

# Mostrar las primeras 5 filas del DataFrame CSV
print("\n🔹 Primeras 5 filas del archivo CSV:")
print(df_csv.head())

# Verificar los tipos de datos y valores nulos
print("\n🔹 Tipos de datos y valores nulos en el CSV:")
print(df_csv.info())
print(df_csv.isnull().sum())

# ==========================================================================
# 2️⃣ Manejo y transformación de datos
# ==========================================================================

# Seleccionar solo las columnas relevantes para el análisis
columnas_relevantes = ["Fecha", "Local", "Vistante", "Goles Local", "Goles Visitante", "Total Goles", "Resultado"]
df_seleccionado = df_csv[columnas_relevantes]

# Eliminar filas con valores nulos en columnas críticas (por ejemplo, 'Fecha' o 'Local')
df_limpiado = df_seleccionado.dropna(subset=["Fecha", "Local"])

# Convertir la columna 'Fecha' al tipo datetime para facilitar su uso posteriormente
df_limpiado["Fecha"] = pd.to_datetime(df_limpiado["Fecha"])

print("\n🔹 Columnas seleccionadas y datos limpiados:")
print(df_limpiado.head())

print("\n🔹 Tipos de datos después de la transformación:")
print(df_limpiado.dtypes)

# ==========================================================================
# 3️⃣ Lectura de datos desde la web (usando pandas)
# ==========================================================================

# Ejemplo: Leer una tabla desde Wikipedia o cualquier sitio web público con tablas HTML
# En este caso usamos una página de ejemplo con tablas (puedes cambiarla por otra URL relevante)
url_ejemplo = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_ (nominal)"

# Usamos read_html() para extraer todas las tablas de la página
tablas = pd.read_html(url_ejemplo)

# Seleccionamos la primera tabla (índice 0)
df_web = tablas[0]

# Limpiar nombres de columnas (opcional, para mejorar legibilidad)
df_web.columns = ["País", "Region", "PIB_millones_USD", "Año"]

# Mostrar las primeras filas de esta tabla
print("\n🔹 Tabla extraída desde la web (PIB por país):")
print(df_web.head())

# ==========================================================================
# 4️⃣ Exportación de datos procesados
# ==========================================================================

# Guardar el DataFrame limpiado en formato CSV y Excel
df_limpiado.to_csv("liga_espanola_resultados_limpios.csv", index=False)
df_limpiado.to_excel("liga_espanola_resultados_limpios.xlsx", index=False)

print("\n✅ Paso 4: Datos exportados a CSV y Excel sin incluir el índice.")

# Opcional: Exportar también a JSON como parte del Plus
df_limpiado.to_json("liga_espanola_resultados_limpios.json", orient="records")
print("📁 Archivo también exportado a formato JSON.")

# ==========================================================================
# ✅ ¡Fin del script!
# ==========================================================================

print("\n🎉 ¡Análisis completado con éxito!")
print("Los archivos procesados han sido guardados en tu carpeta actual.")