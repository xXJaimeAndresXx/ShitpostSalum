
import random
import os
from PIL import Image,ImageDraw,ImageFont
import sys
from random import randint
import facebook


cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
verbo=random_line('Diccionarios/verbos.txt')
verboIndicativo=random_line('Diccionarios/verbo_indicativo.txt')
randomWord=random_line('Diccionarios/random_word.txt')
ilustres=random_line('Diccionarios/ilustres.txt')

message= "Salum "+ verboIndicativo + " " + verbo +" "+ randomWord+ " con "+ ilustres + " en Durango Capital"
print(message)
value = randint(1, 5)
image= Image.open('/Users/Jaime Andres/Desktop/SalumBot/IMGsalum/salum'+str(value)+'.jpg')
font_type= ImageFont.truetype('arial.ttf',14)
draw= ImageDraw.Draw(image)
draw.text(xy=(18,290),text= message, fill=(0,0,0),font=font_type)
image.show()

token='Insert_Token_Here'
fb=facebook.GraphAPI(access_token=token)
fb.put_object(parent_object='me',connection_name='feed', message="Vamos con doña irma")




