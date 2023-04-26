import tkinter as tk
from PIL import Image, ImageTk
import pygame
from mutagen.mp3 import MP3
import os
import time

#  TODO:
# set music fades to sound sum
# next scene - repeat
# title screen for scene0
# menu later if at all

width = 1280
height = 720

root = tk.Tk()
canvas = tk.Canvas(root, width = width, height = height)
canvas.pack()
pygame.init()


x = os.path.exists("scene0")
print(x)
y = os.path.isfile("scene0/0.wav")
print(y)
song = MP3("scene0/music.mp3")
print(song.info.length)

sceneCount = 1
imgCount = 3
soundCount = 3
# will need array of time triggers for dialog
# slide change triggers can be soundLenSum/imgCount
# timer must be constantly watching for either trigger
soundLenSum = 18


for i in range (sceneCount):
    pygame.mixer.music.load("scene0/music.mp3")
    pygame.mixer.music.set_volume(.2)
    pygame.mixer.music.play()
    img = ImageTk.PhotoImage(Image.open("scene0/"+str(0)+".jpg"))
    canvas.create_image(width/2, height/2, image=img)

    for j in range (imgCount):
        img = ImageTk.PhotoImage(Image.open("scene0/"+str(j)+".jpg"))
        canvas.create_image(width/2, height/2, image=img)
        print("starting music")
        print("starting img: "+str(j))
        dialog = pygame.mixer.Sound("scene0/"+str(j)+".wav")
        dialog.set_volume(.3)
        pygame.mixer.Sound.play(dialog)
        print("starting dialog: "+str(j))
        time.sleep(soundLenSum/imgCount)


root.mainloop()

