import pandas as pd
from execute_clean import *

df_text = pd.DataFrame(text_dict)
df_word = pd.DataFrame(words)
frames = [df_word, df_text]
df = pd.concat(frames, axis=1, sort=False)

print(df)


mot_clé = df['words']
df_key_glo = pd.DataFrame(mot_clé)

#Creation d'un df a partir d'un fichier txt
f = open('motscles.txt', 'r')
data = f.read()
f.close
df_key = pd.DataFrame(data.split('\n'))
df_key.columns=['words']
#Fusion des 2 Df dans celui du txt
df_key = df_key.append(df_key_glo).reset_index().drop(columns={'index'})

print(df_key)
