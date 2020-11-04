from put_in_dataframe import *
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2

user = input('user :')
password = input('password :')
sql_engine = create_engine(f'postgresql://{user}:{password}@ec2-34-253-148-186.eu-west-1.compute.amazonaws.com:5432/d88b17qa0na59j', echo=False)

#Pour mettre toute les donnée du df de plans aille dans la db 
table_name = 'plans'
df.to_sql(table_name, sql_engine, if_exists='replace')

#pour tout nos mots clés
# table_name = 'keywords_p'
# df_key.to_sql(table_name, sql_engine, if_exists='replace')