import pandas as pd
from sqlalchemy import create_engine, text
import os

def main():
    user = 'postgres'
    password = 'admin'
    host = 'localhost'
    port = '5432'
    database = 'postgres'

    db_url = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(db_url)

    pasta_trust = './staging/trust/'
    os.makedirs(pasta_trust, exist_ok=True)

    print("Lendo tabela 'students_habits' do banco...")
    df = pd.read_sql_table('students_habits', con=engine)

    # ===================== Dimensão 1: Hábitos de Estudo =====================
    dim_estudo = df[['study_hours_per_day', 'extracurricular_participation', 'attendance_percentage']].drop_duplicates()
    dim_estudo.to_sql('dim_estudo', engine, index=False, if_exists='replace')
    dim_estudo.to_csv(pasta_trust + 'dim_estudo.csv', index=False)

    # ===================== Dimensão 2: Qualidade/Saúde =====================
    dim_saude = df[['sleep_hours', 'mental_health_rating', 'exercise_frequency', 'diet_quality']].drop_duplicates()
    dim_saude.to_sql('dim_saude', engine, index=False, if_exists='replace')
    dim_saude.to_csv(pasta_trust + 'dim_saude.csv', index=False)

    # ===================== Dimensão 3: Redes Sociais =====================
    dim_redes = df[['social_media_hours', 'netflix_hours']].drop_duplicates()
    dim_redes.to_sql('dim_redes', engine, index=False, if_exists='replace')
    dim_redes.to_csv(pasta_trust + 'dim_redes.csv', index=False)

    # ===================== Dimensão 4: Perfil =====================
    dim_perfil = df[['age', 'gender', 'part_time_job']].drop_duplicates()
    dim_perfil.to_sql('dim_perfil', engine, index=False, if_exists='replace')
    dim_perfil.to_csv(pasta_trust + 'dim_perfil.csv', index=False)

    print("ETL3 finalizado: dimensões salvas no banco e na pasta /trust")

if __name__ == "__main__":
    main()
