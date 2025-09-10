import os
import sqlite3

class Loader:
    def __init__(self, dataframe, output_csv, db_path):
        self.df = dataframe
        self.output_csv = output_csv
        self.db_path = db_path

    def save_to_csv(self):
        os.makedirs(os.path.dirname(self.output_csv), exist_ok=True)
        self.df.to_csv(self.output_csv, index=False)
        print(f"CSV guardado en {self.output_csv}")

    def save_to_sqlite(self):
        conn = sqlite3.connect(self.db_path)
        self.df.to_sql("mtg_cards", conn, if_exists="replace", index=False)
        conn.close()
        print(f"Datos guardados en la base de datos SQLite: {self.db_path}")
