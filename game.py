import pygame
from pygame.locals import *

import pandas
import random

from pyvidplayer import Video
from mailer import Mailer


pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font("resources/font.ttf", 40)
counterfont = pygame.font.Font("resources/font.ttf", 50)

restriction = 30

# textwrap
textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3

def drawText(surface, text, color, rect, font, align=textAlignLeft, aa=True, bkg=None):
    lineSpacing = -10
    spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

    listOfWords = text.split(" ")
    if bkg:
        imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
        for image in imageList: image.set_colorkey(bkg)
    else:
        imageList = [font.render(word, aa, color) for word in listOfWords]

    maxLen = rect[2]
    lineLenList = [0]
    lineList = [[]]
    for image in imageList:
        width = image.get_width()
        lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
        if len(lineList[-1]) == 0 or lineLen <= maxLen:
            lineLenList[-1] += width
            lineList[-1].append(image)
        else:
            lineLenList.append(width)
            lineList.append([image])

    lineBottom = rect[1]
    lastLine = 0
    for lineLen, lineImages in zip(lineLenList, lineList):
        lineLeft = rect[0]
        if align == textAlignRight:
            lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages)-1)
        elif align == textAlignCenter:
            lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages)-1)) // 2
        elif align == textAlignBlock and len(lineImages) > 1:
            spaceWidth = (rect[2] - lineLen) // (len(lineImages)-1)
        if lineBottom + fontHeight > rect[1] + rect[3]:
            break
        lastLine += 1
        for i, image in enumerate(lineImages):
            x, y = lineLeft + i*spaceWidth, lineBottom
            surface.blit(image, (round(x), y))
            lineLeft += image.get_width() 
        lineBottom += fontHeight + lineSpacing

    if lastLine < len(lineList):
        drawWords = sum([len(lineList[i]) for i in range(lastLine)])
        remainingText = ""
        for text in listOfWords[drawWords:]: remainingText += text + " "
        return remainingText
    return ""

# qnagen
qna = pandas.read_excel("resources/izvucena_pitanja.xlsx", "sheet", usecols = "A,B")
qnad = qna.to_dict('index')




# game window
width = 1280
height = 720
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("КО ЗНА ЗНА - REVAMP")
icon = pygame.image.load('resources/icon.ico')
pygame.display.set_icon(icon)
pygame.display.toggle_fullscreen()

# intro music
music = pygame.mixer.music.load("resources/main/intro.mp3")
pygame.mixer.music.play()

# Game
def Game():
    running = True
    i = 1

    # background image
    bg_img = pygame.image.load('resources/game/game.png')
    pygame.transform.scale(bg_img,(width,height))

    # game buttons
    button0 = pygame.image.load('resources/buttons/game/main_button01-0.png')
    button1 = pygame.image.load('resources/buttons/game/main_button02-0.png')
    button2 = pygame.image.load('resources/buttons/game/main_button03-0.png')
    
    # game music
    music = pygame.mixer.music.load("resources/game/background_music.mp3")
    pygame.mixer.music.play(-1)

    ba = False
    r = random.randint(0, len(qnad))

    while running:
        posm = pygame.mouse.get_pos()

        q = qnad[r]["ПИТАЊЕ"]
        a = font.render(qnad[r]["ОДГОВОР"], True, "white")
        a_rect = a.get_rect(center=(window.get_width()/2, 255))
        it = counterfont.render(str(i), True, "white")
        it_rect = it.get_rect(center=(128-it.get_width()/2,420))

        window.blit(bg_img,(0,0))
        window.blit(button0,(601,477))
        window.blit(button1,(601,541))
        window.blit(button2,(601,605))
        window.blit(it, it_rect) #35
        if ba:
            window.blit(a, a_rect)

        q_rect = pygame.Rect(150, 60, 980, 185)
        drawTextRect = q_rect.inflate(-5, -5)
        drawText(window, q, "white", drawTextRect, font, textAlignCenter, True)

        if restriction+1 == i:
            Main()

        if posm[0] > 601 and posm[0] < 1101 and posm[1] > 477 and posm[1] < 515:
            button0 = pygame.image.load('resources/buttons/game/main_button01-1.png')
        else:
            button0 = pygame.image.load('resources/buttons/game/main_button01-0.png')

        if posm[0] > 601 and posm[0] < 1101 and posm[1] > 541 and posm[1] < 579:
            button1 = pygame.image.load('resources/buttons/game/main_button02-1.png')
        else:
            button1 = pygame.image.load('resources/buttons/game/main_button02-0.png')

        if posm[0] > 601 and posm[0] < 1101 and posm[1] > 605 and posm[1] < 643:
            button2 = pygame.image.load('resources/buttons/game/main_button03-1.png')
        else:
            button2 = pygame.image.load('resources/buttons/game/main_button03-0.png')
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if posm[0] > 601 and posm[0] < 1101 and posm[1] > 477 and posm[1] < 515:
                        ba = True

                    elif posm[0] > 601 and posm[0] < 1101 and posm[1] > 541 and posm[1] < 579:
                        i = i + 1
                        ba = False
                        r = random.randint(0, len(qnad))
                    elif posm[0] > 601 and posm[0] < 1101 and posm[1] > 605 and posm[1] < 643:
                        mail = Mailer(email='koznaznarevamp@hotmail.com', password='bdujetofzsrevmvs')
                        mail.settings(provider=mail.MICROSOFT)
                        mail.send(receiver='matijakljajic173@gmail.com', subject='ПРИЈАВА ГРЕШКЕ', message=("ПИТАЊЕ: %s\n ОДГОВОР: %s" % (q, qnad[r]["ОДГОВОР"])))
        
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
    quit()
 

# Settings
def Settings():
    global restriction
    running = True
    
    user_text = "30"
    input_rect = pygame.Rect(280, 300, 600, 75)

    # background image
    bg_img = pygame.image.load('resources/settings/settings.png')
    pygame.transform.scale(bg_img,(width,height))
    
    # setting button
    button0 = pygame.image.load('resources/buttons/settings/main_button01-0.png')
    
    while running:
        posm = pygame.mouse.get_pos()

        window.blit(bg_img,(0,0))
        window.blit(button0,(326,438))
        text = counterfont.render(str(user_text), True, "white")
        window.blit(text, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text.get_width()+10)

        if posm[0] > 326 and posm[0] < 826 and posm[1] > 438 and posm[1] < 476:
            button0 = pygame.image.load('resources/buttons/settings/main_button01-1.png')
        else:
            button0 = pygame.image.load('resources/buttons/settings/main_button01-0.png')

        for event in pygame.event.get():
            if event.type == QUIT:
                restriction = 30
                running = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if posm[0] > 326 and posm[0] < 826 and posm[1] > 438 and posm[1] < 476:
                        if user_text.isdigit():
                            restriction = int(user_text)
                            Main()
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
    
        clock.tick(60)
        pygame.display.flip()

# Transition
def Transition():
    vid = Video("resources/transition/transition.mp4")
    vid.set_size((1280,720))
    while vid.active==True:
        vid.draw(window, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                Game()
    vid.close()
    Game()

# main while loop
def Main():
    running = True
    
    # background image
    bg_img = pygame.image.load('resources/main/main.png')
    pygame.transform.scale(bg_img,(width,height))
    
    # main menu buttons
    button0 = pygame.image.load('resources/buttons/main/main_button01-0.png')
    button1 = pygame.image.load('resources/buttons/main/main_button02-0.png')
    button2 = pygame.image.load('resources/buttons/main/main_button03-0.png')
    
    while running:
        posm = pygame.mouse.get_pos()

        window.blit(bg_img,(0,0))
        window.blit(button0,(140,561))
        window.blit(button1,(660,561))
        window.blit(button2,(1208,17))

        if posm[0] > 140 and posm[0] < 640 and posm[1] > 561 and posm[1] < 599:
            button0 = pygame.image.load('resources/buttons/main/main_button01-1.png')
        else:
            button0 = pygame.image.load('resources/buttons/main/main_button01-0.png')

        if posm[0] > 660 and posm[0] < 1160 and posm[1] > 561 and posm[1] < 599:
            button1 = pygame.image.load('resources/buttons/main/main_button02-1.png')
        else:
            button1 = pygame.image.load('resources/buttons/main/main_button02-0.png')

        if posm[0] > 1208 and posm[0] < 1264 and posm[1] > 17 and posm[1] < 73:
            button2 = pygame.image.load('resources/buttons/main/main_button03-1.png')
        else:
            button2 = pygame.image.load('resources/buttons/main/main_button03-0.png')


        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if posm[0] > 140 and posm[0] < 640 and posm[1] > 561 and posm[1] < 599:
                        pygame.mixer.music.pause()
                        Transition()

                    elif posm[0] > 660 and posm[0] < 1160 and posm[1] > 561 and posm[1] < 599:
                        Settings()

                    elif posm[0] > 1208 and posm[0] < 1264 and posm[1] > 17 and posm[1] < 73:
                        pygame.quit()
                        quit()
    
    
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
    quit()

Main()