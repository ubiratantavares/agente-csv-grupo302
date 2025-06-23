import os
import zipfile

class ZipExtractor:

    def __init__(self, zip_file_path:str, extract_path: str):
        self.zip_file_path = zip_file_path
        self.extract_path = extract_path

    def extract(self):
        os.makedirs(self.extract_path, exist_ok=True)
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(self.extract_path)
        print(f"Arquivos extraídos em {self.extract_path}")
