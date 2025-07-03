import pandas as pd

print("🔹 Lección 3: Combinando datos de distintas fuentes...")

# Cargar datos del CSV generado
df_csv = pd.read_csv("datos/datos_pandas.csv")

# Cargar datos adicionales desde Excel
df_excel = pd.read_excel("clientes_ecommerce (1).xlsx")

# Extraer datos de una tabla web (ejemplo público)
url_ejemplo = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_ (nominal)"
tablas = pd.read_html(url_ejemplo)
df_web = tablas[0].rename(columns={0: "País", 1: "Region", 2: "PIB_millones_USD"})

# Mostrar ejemplo de datos web
print("\nDatos extraídos de la web (PIB por país):")
print(df_web.head())

# Ajustar nombres de columnas para compatibilidad
df_excel.rename(columns={"Total_Compras": "Total_Compras_E", "Monto_Total": "Monto_Total_E"}, inplace=True)

# Unificar datasets (usamos ID como clave común)
df_unificado = pd.merge(df_csv, df_excel, on="ID", how="outer")

# Guardar dataset consolidado
df_unificado.to_csv("datos/datos_consolidados.csv", index=False)
print("\nDataFrame consolidado guardado como 'datos/datos_consolidados.csv'")