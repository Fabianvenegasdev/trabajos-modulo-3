import pandas as pd

print("🔹 Lección 6: Agrupamiento y Pivotado")

# Cargar datos optimizados
df = pd.read_csv("datos/datos_optimizados.csv")

# Agrupar por nivel de cliente y calcular métricas
agrupado = df.groupby("Nivel_Cliente").agg(
    promedio_edad=("Edad", "mean"),
    total_clientes=("ID", "count"),
    promedio_gasto=("Gasto_Promedio", "mean")
).reset_index()
print("\nResumen por nivel de cliente:")
print(agrupado)

# Pivotado: distribución de gasto por rango de edad y nivel de cliente
tabla_pivote = pd.pivot_table(df, values="Gasto_Promedio", index="Rango_Edad", columns="Nivel_Cliente", aggfunc=np.mean)
print("\nTabla dinámica de gasto promedio:")
print(tabla_pivote)

# Despivotar tabla para formato largo
df_despivoteado = tabla_pivote.reset_index().melt(id_vars="Rango_Edad", var_name="Nivel_Cliente", value_name="Gasto_Promedio")

# Exportar dataset final
df_final = pd.concat([df, df_despivoteado], ignore_index=True)
df_final.to_csv("datos/dataset_final.csv", index=False)
df_final.to_excel("datos/dataset_final.xlsx", index=False)

print("\n✅ Dataset final exportado como CSV y Excel.")