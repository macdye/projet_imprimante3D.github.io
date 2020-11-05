from make_df import *
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2

user = input('user :')
password = input('password :')

#Pour mettre toute les donnée du df dans 
sql_engine = create_engine(f'postgresql://{user}:{password}@ec2-34-253-148-186.eu-west-1.compute.amazonaws.com:5432/d88b17qa0na59j', echo=False)
table_name = 'glossaire'
df.to_sql(table_name, sql_engine, if_exists='replace', index=True, index_label='index')

table_name = 'key_word'
df_key.to_sql(table_name, sql_engine, if_exists='replace', index=True, index_label='index')