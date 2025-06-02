"""modulo de extract necessárias para consolidar os dados de entrada."""

import glob
import os
import pandas as pd

#input_folder='C:/Projetos/projeto-estrutura/data/input'
input_folder='C:/Users/guilherme.barbosa/Documents/meu_git/projeto-estrutura/data/input'

def extract_excel(input_folder):
    """
    função para extrair dados de arquivos Excel.

    type: input_folder: str
    """
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))
    if not files:
        raise ValueError("No Excel files found in the specified folder")
    all_data = [pd.read_excel(file) for file in files]
    return all_data

if __name__ == '__main__':
    df = extract_excel(input_folder)
    print (df)


    