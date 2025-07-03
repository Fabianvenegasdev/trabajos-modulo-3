import pandas as pd
import numpy as np

print("🔹 Lección 2: Cargando y explorando datos con Pandas")

# Cargar datos desde el archivo .npz
datos = np.load('datos/datos_ficticios.npz')
df = pd.DataFrame({
    'ID': datos['ids'],
    'Edad': datos['edades'],
    'Total_Compras': datos['compras'],
    'Monto_Total': datos['montos']
})

# Exploración inicial
print("\nPrimeras filas del DataFrame:")
print(df.head())

print("\nÚltimas filas del DataFrame:")
print(df.tail())

print("\nInformación general del DataFrame:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

# Filtro condicional: mayores de 50 años
mayores_50 = df[df["Edad"] > 50]
print("\nClientes mayores de 50 años:")
print(mayores_50.head())

# Guardar en CSV
df.to_csv("datos/datos_pandas.csv", index=False)
print("\nDataFrame guardado como 'datos/datos_pandas.csv'")