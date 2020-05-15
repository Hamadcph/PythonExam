import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine

df = pd.read_csv('ram.csv')
print(df)

engine = create_engine('mysql+pymysql://dev:ax2@localhost:3307/ram')
with engine.connect() as conn, conn.begin():
    df.to_sql('ram', conn, if_exists='replace')
