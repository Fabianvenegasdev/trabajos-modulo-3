import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("🔹 Lección 4: Limpieza de datos - Nulos y Outliers")

# Cargar datos consolidados
df = pd.read_csv("datos/datos_consolidados.csv")

# Verificar nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Imputar valores nulos
for col in df.columns:
    if df[col].dtype == 'object':
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].median(), inplace=True)

# Detectar outliers con IQR
def detectar_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    return df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]

outliers_edad = detectar_outliers(df, "Edad")
print(f"\nOutliers en Edad: {len(outliers_edad)} registros")

# Eliminar outliers extremos
df_limpio = df[~df.index.isin(outliers_edad.index)]

# Visualización opcional
plt.figure(figsize=(10, 4))
sns.boxplot(data=df_limpio[['Edad', 'Monto_Total']])
plt.title("Boxplot después de eliminar outliers")
plt.show()

# Guardar datos limpios
df_limpio.to_csv("datos/datos_limpios.csv", index=False)
print("\nDataFrame limpio guardado como 'datos/datos_limpios.csv'")