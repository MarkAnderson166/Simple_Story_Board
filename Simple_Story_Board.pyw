
import pygame
import os

width = 1280
height = 720

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Simple_Story_Board") 
screen = pygame.display.set_mode((width,height))


soundCount = 3
# will need array of time triggers for dialog
# slide change triggers can be soundLenSum/imgCount
# timer must be constantly watching for either trigger
soundLenSum = 4
soundTimes = []

def countScenes(count):
    global sceneCount
    if os.path.exists("scene"+str(count)):
        count = int(count)+1
        countScenes(count)
    else:
        sceneCount = count
        return int(count)
    
def countImg(scene, count):
    global imgCount
    if os.path.isfile("scene"+str(scene)+"/"+str(count)+".jpg"):
        count = int(count)+1
        countImg(scene, count)
    else:
        imgCount = count
        return int(count)
    
def getSoundTimes(scene, count):
    #global soundTimes
    if os.path.isfile("scene"+str(scene)+"/"+str(count)+".wav"):
        a = pygame.mixer.Sound("scene"+str(scene)+"/"+str(count)+".wav")
        soundTimes.append(round(pygame.mixer.Sound.get_length(a)+soundTimes[count],2))
        count = int(count)+1
        getSoundTimes(scene, count)
    else:
        return int(count)
    

countScenes(0)

for i in range (sceneCount):

    pygame.mixer.music.load("scene"+str(i)+"/music.mp3")
    pygame.mixer.music.set_volume(.2)
    pygame.mixer.music.play()

    countImg(i,0)
    soundTimes.clear()
    soundTimes.append(0)
    getSoundTimes(i,0)
    print(soundTimes)

    for j in range (imgCount):

        img = pygame.image.load("scene"+str(i)+"/"+str(j)+".jpg")
        screen.blit(img,(0,0))
        pygame.display.flip()

        dialog = pygame.mixer.Sound("scene"+str(i)+"/"+str(j)+".wav")
        dialog.set_volume(.3)
        pygame.mixer.Sound.play(dialog)
        pygame.time.wait(int((soundLenSum*1000)/imgCount))


pygame.quit()   


#  TODO:
# set music fades to sound sum
# fade between slides
# title screen for scene0
# menu later if at all