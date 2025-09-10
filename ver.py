import pandas as pd

# Ruta a tu CSV real
csv_path = "Extract/file/all_mtg_cards.csv"

# Cargar solo las columnas necesarias
df = pd.read_csv(csv_path, usecols=["name", "colors", "rarity"])

# Ver las primeras filas
print(df.head())

# Guardar en un nuevo CSV con solo esas columnas
df.to_csv("Extract/file/mtg_filtered.csv", index=False)