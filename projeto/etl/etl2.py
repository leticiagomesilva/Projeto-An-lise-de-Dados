import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os

def main():
    caminho_csv = './staging/raw/student_habits_performance.csv'
    
    user = 'postgres'
    password = 'admin'
    host = 'localhost'
    port = '5432'
    database = 'postgres'  

    db_url = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    
    print('Lendo dataset...')
    df = pd.read_csv(caminho_csv)

    print('Conectando ao PostgreSQL...')
    engine = create_engine(db_url)

    try:
        tabela_destino = 'students_habits'
        df.to_sql(tabela_destino, engine, index=False, if_exists='replace')  
        
        print(f'Dados inseridos na tabela: {tabela_destino}')
    except Exception as e:
        print(f'Erro ao inserir no banco: {e}')

if __name__ == "__main__":
    main()
