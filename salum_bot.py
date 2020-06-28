
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

messageBot= "Salum "+ verboIndicativo + " " + verbo +" "+ randomWord+ " con "+ ilustres + " en Durango Capital"
print(messageBot)
value = randint(1, 5)
image= Image.open('IMGsalum/salum'+str(value)+'.jpg')
font_type= ImageFont.truetype('arial.ttf',14)
draw= ImageDraw.Draw(image)
draw.text(xy=(18,290),text= messageBot, fill=(0,0,0),font=font_type)
image.show()
image.save('IMGsalum/post.png')

token='YOUR_TOKEN'
fb=facebook.GraphAPI(access_token=token)
#fb.put_object(parent_object='me',connection_name='feed', message="Vamos con doña irma")
fb.put_photo(image=open('IMGsalum/post.png', 'rb'),
                message= messageBot )



