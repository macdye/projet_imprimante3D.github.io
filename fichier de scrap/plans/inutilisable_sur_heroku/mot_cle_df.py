from ../put_in_dataframe import *
import pandas as pd 

#Liste des materiaux conseiller
list_material_key = df.groupby('material').count().reset_index().material
list_material_key

#Liste des mots présent dans les noms de fichier
list_mots_clé = []
name_of_object = df.groupby('name').count().reset_index().name
for mot in name_of_object:
    word = mot.split()
    for w in word:
        list_mots_clé.append(w)

#Netoyage des données
liste_sans = set(list_mots_clé)
liste_sans = list(liste_sans)
liste_sans.sort()

#Selection des données faisant plus de 3 charactères
bibop = []
for word in liste_sans :
    if len(word) > 3:
        bibop.append(word)
list_of_key_word = []

#Mise en base de donnée & fusion des 2 base de donnée
df_bibop = pd.DataFrame(bibop)
df_key = pd.DataFrame(list_material_key).rename(columns={'material':0})
df_key = df_key.append(df_bibop).reset_index().drop(columns={'index'}).rename(columns={0:'mots'})