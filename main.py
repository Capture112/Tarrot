import random

from fastapi import FastAPI
from fastapi.responses import FileResponse
from random import SystemRandom
import os

sys_rand = SystemRandom()
app = FastAPI()
images = os.listdir('Tarrot')
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

@app.get('/rand',response_class = FileResponse)
def get_random():
    try:
        rand_image = images[random.randrange(1, 10)]
        return ("Tarrot/" + rand_image)
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='item does not exists')