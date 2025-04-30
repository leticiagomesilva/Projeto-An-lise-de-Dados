import pandas as pd
import os
import shutil

def main():
    caminho_origem = './student_habits_performance.csv' 
    caminho_destino = './staging/raw/student_habits_performance.csv'

    os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)

    try:
        dataset = pd.read_csv(caminho_origem)
        print('Dataset carregado com sucesso.')
    except Exception as e:
        print(f'Erro ao carregar o CSV: {e}')
        return

    try:
        shutil.copy(caminho_origem, caminho_destino)
        print(f'Arquivo movido para {caminho_destino}')
    except Exception as e:
        print(f'Erro ao mover o arquivo: {e}')

if __name__ == "__main__":
    main()
