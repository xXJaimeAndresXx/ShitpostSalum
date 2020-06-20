
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
verbo=random_line('verbos.txt')
verboIndicativo=random_line('verbo_indicativo.txt')
randomWord=random_line('random_word.txt')
ilustres=random_line('ilustres.txt')

message= "Salum "+ verboIndicativo + " " + verbo +" "+ randomWord+ " con "+ ilustres + " en Durango Capital"
print(message)
value = randint(1, 5)
image= Image.open('/Users/Jaime Andres/Desktop/SalumBot/IMGsalum/salum'+str(value)+'.jpg')
font_type= ImageFont.truetype('arial.ttf',14)
draw= ImageDraw.Draw(image)
draw.text(xy=(18,290),text= message, fill=(0,0,0),font=font_type)
image.show()

token='EAAH2K85Qh8MBAHZA5dyH2ZCmeVW7SvpvT8Q6prbJdYQXYXqU66FWBQGDhiZCeV1PKV3KAD2sEm7ese1bjnHrfZAIxhV48MXdXMEZBeu4Rx11MkQQMurEhmOBPHPlweUOWp3Cmc60M5eXThmdZCBKIRt4bXtUBtej4cCHLpW1vnUZAZBdDvrM4ry5wMCdZARTcO2cYntFg8Ib0ZBh3b0GCVuJaClMqM3C994ymDfeVJZCuvAxQZDZD'
fb=facebook.GraphAPI(access_token=token)
fb.put_object(parent_object='me',connection_name='feed', message="Vamos con doña irma")




