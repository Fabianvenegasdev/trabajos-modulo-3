import numpy as np
import os

print("🔹 Lección 1: Generando datos ficticios con NumPy")

# Crear directorio de salida si no existe
os.makedirs('datos', exist_ok=True)

# Definir número de clientes ficticios
num_clientes = 100

# Generar datos ficticios con NumPy
np.random.seed(42)  # Para reproducibilidad

ids = np.arange(1, num_clientes + 1)
edades = np.random.randint(18, 70, size=num_clientes)
compras = np.random.poisson(lam=5, size=num_clientes)
montos = np.round(np.random.uniform(100, 5000, size=num_clientes), 2)

# Guardar datos generados
np.savez('datos/datos_ficticios.npz', ids=ids, edades=edades, compras=compras, montos=montos)

print("\nDatos ficticios generados:")
print(f"IDs: {ids[:5]}...")
print(f"Edades: {edades[:5]}")
print(f"Compras: {compras[:5]}")
print(f"Montos: {montos[:5]}")
print("\nArchivo guardado como 'datos/datos_ficticios.npz'")