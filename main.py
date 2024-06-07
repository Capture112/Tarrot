import random

from fastapi import FastAPI
from fastapi.responses import FileResponse
from random import SystemRandom
import os

sys_rand = SystemRandom()
app = FastAPI()

#Директории
tarrot_dir = os.listdir('Tarrot')
tarrot_major_dir = os.listdir('Tarrot_Major')
items = [1,2,3,4,5]

@app.get('/')
def root():
    return {'message': "HI"}

@app.get('/items')
def get_item(item_id: int):
    try:
        return images[item_id -1]
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='item does not exists')


#Tarrot
@app.get('/rand',response_class = FileResponse)
def get_random():
    try:
        rand_image = tarrot_dir[random.randrange(1, 10)]
        return ("Tarrot/" + rand_image)
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='item does not exists')

@app.get('/rand_major',response_class = FileResponse)
def get_random_major():
    try:
        rand_image = tarrot_major_dir[random.randrange(1, 10)]
        return ("Tarrot_Major/" + rand_image)
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='item does not exists')