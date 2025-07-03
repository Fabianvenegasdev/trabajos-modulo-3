import numpy as np

# ================== CREACIÓN Y MANIPULACIÓN DE ARRAYS ==================
print("=== CREACIÓN Y MANIPULACIÓN DE ARRAYS ===")

# Generar un array unidimensional de 20 números aleatorios entre 1 y 100
arr = np.random.randint(1, 101, size=20)
print("Array original:", arr)

# Calcular suma, promedio, máximo y mínimo
print("Suma:", np.sum(arr))
print("Promedio:", np.mean(arr))
print("Máximo:", np.max(arr))
print("Mínimo:", np.min(arr))

# Ordenar el array en forma ascendente y descendente
arr_ascendente = np.sort(arr)
arr_descendente = -np.sort(-arr)  # Otra forma de ordenar descendente
print("Ordenado ascendente:", arr_ascendente)
print("Ordenado descendente:", arr_descendente)

# Extraer todos los valores pares
pares = arr[arr % 2 == 0]
print("Valores pares:", pares)

# Reemplazar todos los valores impares por -1
arr_impares_a_menos_uno = np.where(arr % 2 != 0, -1, arr)
print("Array con impares reemplazados:", arr_impares_a_menos_uno)

# ====================== OPERACIONES CON MATRICES ======================
print("\n=== OPERACIONES CON MATRICES ===")

# Crear dos matrices (4x4) de números enteros aleatorios entre 1 y 50
matriz1 = np.random.randint(1, 51, size=(4, 4))
matriz2 = np.random.randint(1, 51, size=(4, 4))
print("Matriz 1:\n", matriz1)
print("Matriz 2:\n", matriz2)

# Suma, resta y multiplicación matricial
suma = matriz1 + matriz2
resta = matriz1 - matriz2
multiplicacion = np.dot(matriz1, matriz2)
print("Suma de matrices:\n", suma)
print("Resta de matrices:\n", resta)
print("Multiplicación matricial:\n", multiplicacion)

# Matriz transpuesta de la primera matriz
transpuesta = matriz1.T
print("Transpuesta de la matriz 1:\n", transpuesta)

# Determinante de la segunda matriz
try:
    determinante = np.linalg.det(matriz2)
    print("Determinante de la matriz 2:", round(determinante, 2))
except np.linalg.LinAlgError:
    print("La matriz 2 no es invertible, no se puede calcular el determinante.")

# Inversa de la segunda matriz (si es invertible)
try:
    inversa = np.linalg.inv(matriz2)
    print("Inversa de la matriz 2:\n", inversa)
except np.linalg.LinAlgError:
    print("La matriz 2 no es invertible.")

# ===================== APLICACIÓN DE FUNCIONES EN NUMPY =====================
print("\n=== APLICACIÓN DE FUNCIONES ===")

# Generar un array de 100 valores distribuidos uniformemente entre 0 y 10
arr_uniforme = np.linspace(0, 10, 100)
print("Primeros 5 elementos del array uniforme:", arr_uniforme[:5])

# Seno y coseno de cada valor
seno = np.sin(arr_uniforme)
coseno = np.cos(arr_uniforme)
print("Seno de los primeros 5 elementos:", seno[:5])
print("Coseno de los primeros 5 elementos:", coseno[:5])

# Función exponencial
exponencial = np.exp(arr_uniforme)
print("Exponencial de los primeros 5 elementos:", exponencial[:5])

# Raíz cuadrada de elementos mayores a 5
raiz_cuadrada = np.sqrt(arr_uniforme[arr_uniforme > 5])
print("Raíz cuadrada de elementos > 5 (primeros 5):", raiz_cuadrada[:5])