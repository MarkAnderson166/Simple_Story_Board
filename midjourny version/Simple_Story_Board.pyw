
import pygame
import os

width = 1900
height = 1024

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Simple_Story_Board") 
screen = pygame.display.set_mode((width,height))


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
    if os.path.isfile("scene"+str(scene)+"/"+str(count)+".png"):
        count = int(count)+1
        countImg(scene, count)
    else:
        imgCount = count
        return int(count)
    

def getSoundTimes(scene, count):
    #global soundTimes
    if os.path.isfile("scene"+str(scene)+"/"+str(count)+".mp3"):
        a = pygame.mixer.Sound("scene"+str(scene)+"/"+str(count)+".mp3")
        soundTimes.append(round(pygame.mixer.Sound.get_length(a)+soundTimes[count],2))
        count = int(count)+1
        getSoundTimes(scene, count)
    else:
        return int(count)
    

def changeImg(scene, slide):

    img2 = pygame.image.load("scene"+str(scene)+"/"+str(slide)+".png").convert_alpha()
    img2 = pygame.transform.scale(img2,(width,height))
    if slide == 0:
        img1 = img2
    else:
        img1 = pygame.image.load("scene"+str(scene)+"/"+str(slide-1)+".png").convert_alpha()
    img1 = pygame.transform.scale(img1,(width,height))

    alpha1 = 255
    alpha1_change = -1
    alpha2 = 0
    alpha2_change = 1
    while alpha2 < 255: 
        alpha1 += alpha1_change
        alpha2 += alpha2_change
        alpha1 = max(0, min(alpha1, 255))   
        alpha2 = max(0, min(alpha2, 255))   
        alpha1_image = img1.copy()
        alpha2_image = img2.copy()
        alpha1_image.set_alpha(alpha1)    
        alpha2_image.set_alpha(alpha2)    
        screen.blit(alpha2_image, (0, 0))
        pygame.display.flip()


countScenes(0)

for i in range (sceneCount):

    music = pygame.mixer.Sound("scene"+str(i)+"/backing.mp3")
    music.set_volume(.3)
    pygame.mixer.Sound.play(music)

    soundTimes = [0]
    getSoundTimes(i,0)
    countImg(i,0)
    changeImg(i,0)

    # if we have the same number of images as sound files they will sync
    # else, the images get equal time each
    if len(soundTimes)-1 == imgCount:
        imgChangeMode = 'directed'
    else:
        imgChangeMode = 'even'

    sceneStartTime = pygame.time.get_ticks()
    slideTimeEach = (soundTimes[-1]+1)/imgCount
    slideNumber = 1
    soundNumber = 0

    while soundTimes:
        
        currentTime = (pygame.time.get_ticks()-sceneStartTime)/1000

        if currentTime > soundTimes[0]:
            soundTimes.pop(0)
            if soundTimes:
                dialog = pygame.mixer.Sound("scene"+str(i)+"/"+str(soundNumber)+".mp3")
                dialog.set_volume(.3)
                pygame.mixer.Sound.play(dialog)
                soundNumber += 1
                if imgChangeMode == 'directed':
                    changeImg(i, slideNumber-1)
                    slideNumber += 1

        if imgChangeMode == 'even' and currentTime > slideTimeEach*(slideNumber) and soundTimes:
            changeImg(i, slideNumber)
            slideNumber += 1


pygame.quit()
