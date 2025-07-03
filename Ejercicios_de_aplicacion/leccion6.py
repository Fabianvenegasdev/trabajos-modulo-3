# 🎯 Desafío: Agrupamiento, Pivotado y Fusión de Datos
# Este script realiza manipulación avanzada de datos con Pandas.


import pandas as pd

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
# 🔁 2. Agrupamiento de datos
# ==========================================================================

print("\n🔹 2. Realizando agrupamientos...")

# Renombrar 'Vistante' a 'Visitante' para legibilidad
df.rename(columns={"Vistante": "Visitante"}, inplace=True)

# Agrupar por equipo local y calcular estadísticas
agrupado_local = df.groupby("Local").agg(
    promedio_goles=("Goles Local", "mean"),
    total_goles=("Goles Local", "sum"),
    partidos_jugados=("Local", "count")
).reset_index()

print("\nPromedio de goles por equipo como local:")
print(agrupado_local.sort_values(by="promedio_goles", ascending=False).head())

# Función personalizada: cantidad de partidos ganados como local
def contar_victorias_local(grupo):
    return grupo[grupo["Resultado"] == "Home"].shape[0]

victorias_locales = df.groupby("Local").apply(contar_victorias_local).reset_index(name="Victorias_Local")

print("\nVictorias por equipo como local:")
print(victorias_locales.sort_values(by="Victorias_Local", ascending=False).head())

# ==========================================================================
# 🔄 3. Pivotado y despivotado de datos
# ==========================================================================

print("\n🔹 3. Realizando pivotado y despivotado...")

# Crear tabla dinámica: promedio de goles por equipo local/visitante
tabla_pivote = pd.pivot_table(
    df,
    values=["Goles Local", "Goles Visitante"],
    index=["Local", "Visitante"],
    aggfunc="mean"
).reset_index()

print("\nTabla dinámica (promedio de goles por encuentro):")
print(tabla_pivote.head())

# Despivotar los goles locales y visitantes
df_despivotado = pd.melt(
    df,
    id_vars=["Fecha", "Local", "Visitante"],
    value_vars=["Goles Local", "Goles Visitante"],
    var_name="Tipo_Gol",
    value_name="Cantidad"
)

print("\nDatos despivotados (goles por tipo):")
print(df_despivotado.head())

# ==========================================================================
# 🔗 4. Combinación y fusión de datos
# ==========================================================================

print("\n🔹 4. Realizando combinaciones de datos...")

# Ejemplo: crear un segundo DataFrame con datos de otro torneo
data_extra = pd.DataFrame({
    "Equipo": ["Barcelona", "Real Madrid", "Atl. Madrid", "Betis"],
    "Posicion_Liga": [1, 2, 3, 6],
    "Puntos": [89, 87, 80, 65]
})

# Simular datos como si fueran del mismo torneo pero estructura diferente
df_home = df[["Local", "Goles Local", "Fecha"]]
df_away = df[["Visitante", "Goles Visitante", "Fecha"]]

# Concatenar dos DataFrames con mismas columnas
df_concatenado = pd.concat([
    df_home.rename(columns={"Local": "Equipo", "Goles Local": "Goles"}),
    df_away.rename(columns={"Visitante": "Equipo", "Goles Visitante": "Goles"})
], ignore_index=True)

print("\nDatos concatenados (goles anotados como local y visitante):")
print(df_concatenado.head())

# Fusionar con merge() - Unir con el DataFrame extra
df_merged = pd.merge(
    agrupado_local,
    data_extra,
    left_on="Local",
    right_on="Equipo",
    how="inner"
)

print("\nFusión con datos adicionales:")
print(df_merged[["Local", "promedio_goles", "Posicion_Liga", "Puntos"]].head())

# ==========================================================================
# 💾 5. Exportación de datos
# ==========================================================================

print("\n🔹 5. Exportando datos procesados...")

# Guardar el dataset final (agrupado) en formato CSV y Excel
df_merged.to_csv("liga_espanola_datos_agrupados.csv", index=False)
df_merged.to_excel("liga_espanola_datos_agrupados.xlsx", index=False)

print("\n✅ ¡Desafío completado exitosamente!")
print("Archivo guardado como:")
print(" - liga_espanola_datos_agrupados.csv")
print(" - liga_espanola_datos_agrupados.xlsx")