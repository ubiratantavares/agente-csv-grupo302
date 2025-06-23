import os
import pandas as pd

class CSVLoader:

    def __init__(self, path: str):
        self.path = path

    def load_csv_files(self):
        dados = {}
        
        for filename in os.listdir(self.path):
            if filename.lower().endswith('.csv'):
                path = os.path.join(self.path, filename)
                try:
                    dados[filename] = pd.read_csv(path, encoding='utf-8', sep=',')
                except Exception as e:
                    print(f"Erro ao tentar ler o arquivo {filename}: {e}")
        return dados
    
    def __str__(self):
        return f"{self.path}"