import pandas as pd

print("🔹 Lección 5: Aplicando Data Wrangling")

# Cargar datos limpios
df = pd.read_csv("datos/datos_limpios.csv")

# Eliminar duplicados
df.drop_duplicates(subset=["ID"], keep="first", inplace=True)

# Renombrar columnas para legibilidad
df.rename(columns={"Total_Compras": "Transacciones", "Monto_Total": "Ingreso_Total"}, inplace=True)

# Crear nuevas columnas derivadas
df["Gasto_Promedio"] = df["Ingreso_Total"] / df["Transacciones"].replace(0, np.nan)
df["Rango_Edad"] = pd.cut(df["Edad"], bins=[18, 30, 45, 60, 100], labels=["Joven", "Adulto", "Maduro", "Mayor"])

# Aplicar función personalizada
def nivel_cliente(transacciones):
    if transacciones > 10:
        return "Alto"
    elif transacciones > 5:
        return "Medio"
    else:
        return "Bajo"

df["Nivel_Cliente"] = df["Transacciones"].apply(nivel_cliente)

# Guardar datos optimizados
df.to_csv("datos/datos_optimizados.csv", index=False)
print("\nDataFrame optimizado guardado como 'datos/datos_optimizados.csv'")