from fastapi import FastAPI
import uvicorn
from bson.objectid import ObjectId
from typing import List, Optional
import psycopg2
from fastapi.responses import JSONResponse
import random


app = FastAPI()

conn = psycopg2.connect(dbname="d88b17qa0na59j", host="ec2-34-253-148-186.eu-west-1.compute.amazonaws.com", user="parcwjlwsvhmfh", password="a552d46d7f7a144c6e344530d727d46939c9c4d5588bf470c37ec4b37d7767b1")
cursor = conn.cursor()


@app.get("/")
async def root():
	return {"message": "Bienvenue sur l'API des Imprimantes 3D!"}

@app.get("/videos")
async def get_all_videos():
	cursor.execute("""SELECT * FROM videos;""")
	videos = cursor.fetchall()
	video_list = []
	for video in videos:
		video_list.append({"id: ":video[0], "titre: ":video[1], "publiée le: ":video[2], "durée: ":video[3], "mots-clés: ":video[4], "lien: ":video[5]})
	return JSONResponse(video_list)

@app.get("/filaments")
async def get_all_filaments():
	cursor.execute("""SELECT * FROM filaments;""")
	filaments = cursor.fetchall()
	filaments_list = []
	for fils in filaments:
		filaments_list.append({"id: ":fils[0], "nom: ":fils[1], "description: ":fils[2], "temp. extrusion: ":fils[3], "temp. plateau: ":fils[4], "vitesse impr.: ":fils[5]})
	return JSONResponse(filaments_list)

@app.get('/plans')
async def get_all_plans():
	cursor.execute("""SELECT index, name, absolute_url, obj_img, material from plans;""")
	plans = cursor.fetchall()
	plans_list = []
	for plan in plans:
		plans_list.append({"id: ":plan[0], "nom: ":plan[1], "url: ":plan[2], "obj_img: ":plan[3], "materiel: ":plan[4]})
	return JSONResponse(plans_list)

@app.get('/plans/random')
async def get_all_plans_random():
    cursor.execute("""SELECT index, name, absolute_url, obj_img, material from plans;""")
    plans = cursor.fetchall()
    plans_list = []
    for plan in plans:
        plans_list.append({"id: ":plan[0], "nom: ":plan[1], "url: ":plan[2], "obj_img: ":plan[3], "materiel: ":plan[4]})
    return JSONResponse(random.choice(plans_list))

@app.get("/key_word/filament/{nomfilament}")
async def get_filament_from_keywords(nomfilament):
	cursor.execute(f"""
		SELECT filaments.nom_fil, filaments.description, filaments.temp_extrusion, filaments.temp_plateau, filaments.vitesse_impr 
		FROM key_word 
		JOIN filaments_key 
			ON filaments_key.key_word_id = key_word.index 
		JOIN filaments
			ON filaments.id = filaments_key.filaments_id 
		WHERE key_word.words = '{nomfilament}';"""
	)
	filament = cursor.fetchall()
	if filament :
		return filament
	else :
		return f"Aucun fil nommé {nomfilament}. Êtes-vous sûr-e-s de l'orthographe?"

@app.get("/key_word/glossaire/{mot_glossaire}")
async def get_glossaire_from_keywords(mot_glossaire):
	cursor.execute(f"""
		SELECT glossaire.words, glossaire.part01, glossaire.part02 
		FROM key_word 
		JOIN glossaire_key 
			ON key_word_id = key_word.index 
		JOIN glossaire 
			ON glossaire_key.glossaire_id = glossaire.index 
		WHERE key_word.words LIKE '%{mot_glossaire}%';"""
	)
	mot = cursor.fetchall()
	if mot :
		return mot
	else :
		return f"Aucun {mot_glossaire} dans le glossaire. Êtes-vous sûr-e-s de l'orthographe?"

@app.get("/key_word/videos/{video_key}")
async def get_video_from_keywords(video_key):
	cursor.execute(f"""
		SELECT videos.titre_video, videos.tags_video 
		FROM key_word 
		JOIN videos_key 
			ON key_word_id = key_word.index 
		JOIN videos 
			ON videos_key.videos_id = videos.id 
		WHERE key_word.words LIKE '%{video_key}%';"""
	)
	mot = cursor.fetchall()
	if mot :
		return mot
	else :
		return f"Impossible de trouver {video_key}! Êtes-vous sûr-e-s de l'orthographe?"

@app.get("/plans/materiel/{fil}")
async def get_plan_from_keywords(fil):
	cursor.execute(f"""
		SELECT plans.index, plans.name, plans.absolute_url, plans.obj_img, plans.material 
		FROM key_word 
		JOIN plantags 
			ON plantags.key_word_id = key_word.index 
		JOIN plans 
			ON plans.index = plantags.plans_id 
		WHERE words LIKE '%{fil}%';
		"""
	)
	mot = cursor.fetchall()
	if mot :
		return mot
	else :
		return f"Aucun {fil} ne correspond au terme précisé dans les plans. Êtes-vous sûr-e-s de l'orthographe?"

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)
