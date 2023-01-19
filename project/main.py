import os
import sys
import random as r

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def arrow(pos, screen):
    image = load_image('arrow.png')
    screen.blit(image, pos)


def start_screen(width, height):
    pygame.mixer.music.load('data/annoying music i hate it evilface.wav')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image(f'fon{0}.png'), (width, height))
    screen.blit(fon, (0, 0))
    k = 0
    kk = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        k += clock.tick() / 1000
        if k >= 0.75:
            kk += 1
            fon = pygame.transform.scale(load_image(f'fon{kk % 2}.png'), (width, height))
            screen.blit(fon, (0, 0))
            k = 0
        pygame.display.flip()


def eggadd(egg, screen):
    if egg == 1:
        image = load_image('Egg.png')
        screen.blit(image, (5, 125))
        return 1, 5, 125
    elif egg == 2:
        image = load_image('Egg.png')
        screen.blit(image, (5, 402))
        return 2, 5, 402
    elif egg == 3:
        image = load_image('Egg.png')
        screen.blit(image, (740, 130))
        return 3, 740, 130
    image = load_image('Egg.png')
    screen.blit(image, (740, 410))
    return 4, 740, 410


def eggmove(eggs, mpos, multi):
    tempeggs = []
    gametype = 0
    for egg, posx, posy in eggs:
        if egg == 1:
            posx += 0.5
            posy += 0.31
            if 200 <= posx <= 264 and 264 >= posy >= 200 and mpos == (225, 275):
                gametype = 1
                continue
            elif posx > 264 or posy > 264:
                gametype = 2
        elif egg == 2:
            posx += 0.3
            posy += 0.07
            if 195 <= posx <= 230 and 474 >= posy >= 410 and mpos == (215, 485):
                gametype = 1
                continue
            elif posx > 230 or posy > 474:
                gametype = 2
        elif egg == 3:
            posx -= 0.5
            posy += 0.31
            if 520 <= posx <= 554 and 284 >= posy >= 220 and mpos == (515, 295):
                gametype = 1
                continue
            elif posx < 520 or posy > 284:
                gametype = 2
        else:
            posx -= 0.3
            posy += 0.06
            if 530 <= posx <= 564 and 479 >= posy >= 415 and mpos == (525, 490):
                gametype = 1
                continue
            elif posx < 530 or posy > 479:
                gametype = 2
        image = load_image('Egg.png')
        screen.blit(image, (posx, posy))
        tempeggs.append((egg, posx, posy))
    return tempeggs, gametype


def movem(pos):
    mis = load_image('miska.png')
    screen.blit(mis, pos)


def game():
    global fontype, oblr, obl, backtype, light, score, stpose, stmove, stx, sty

    fon = pygame.transform.scale(load_image('den.png'), (width, height))
    screen.blit(fon, (0, 0))
    fon = pygame.transform.scale(load_image('Gameplay Fon den.png'), (width, height))
    screen.blit(fon, (0, 0))

    running = True
    pygame.mixer.music.set_volume(0.45)
    tme = 2
    lim = 2
    multi = 1
    eggs = []
    eggtime = pygame.time.Clock()
    sut = pygame.time.Clock()
    fontype = 'den.png'
    backtype = 'Gameplay Fon den.png'
    sme = 0

    gametype = 0

    score = 0

    oblr = r.randint(0, 5)
    if oblr != 0:
        oblt = pygame.transform.scale(load_image(f'obl{oblr}.png'), (width, height))
        mov = r.choice([-1, 1])
        screen.blit(oblt, (20 * mov, 0))
        obl = [20 * mov, mov]

    mpos = (525, 490)

    kdpress = 6994830
    stickmove = pygame.time.Clock()
    stmove = 0
    stpose = 1
    stx = 185
    sty = 370
    kdtime = pygame.time.Clock()
    font = pygame.font.Font(None, 100)
    light = 'Black'

    while running:
        sme += sut.tick() / 1000
        if fontype == 'noch.png' and sme >= 10:
            backtype = 'Gameplay Fon den.png'
            fontype = 'den.png'
            sme = 0
            oblr = r.randint(0, 5)
            mov = r.choice([-1, 1])
            obl = [20 * mov, mov]
            lim = 2
            multi /= 2
            light = 'Black'
        elif sme >= 30:
            backtype = 'Gameplay Fon noch.png'
            fontype = 'noch.png'
            sme = 0
            oblr = r.randint(0, 5)
            mov = r.choice([-1, 1])
            obl = [20 * mov, mov]
            lim = 2
            multi *= 4
            light = 'White'
        fon = pygame.transform.scale(load_image(fontype), (width, height))
        screen.blit(fon, (0, 0))

        if oblr != 0:
            oblt = pygame.transform.scale(load_image(f'obl{oblr}.png'), (width, height))
            screen.blit(oblt, (obl[0] - 0.005 * obl[1], 0))
            obl = [obl[0] - 0.005 * obl[1], obl[1]]

        back = pygame.transform.scale(load_image(backtype), (width, height))
        screen.blit(back, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.QUIT:
                running = False
            key = pygame.key.get_pressed()
            if (key[pygame.K_a] or event.type == pygame.MOUSEBUTTONDOWN and 0 < pygame.mouse.get_pos()[0] <= 400 and 0 <
                pygame.mouse.get_pos()[1] <= 400) and kdpress >= 0.05:
                mpos = (225, 275)
                kdpress = 0
            elif (key[pygame.K_s] or event.type == pygame.MOUSEBUTTONDOWN and 0 < pygame.mouse.get_pos()[
                0] <= 400 and 400 < pygame.mouse.get_pos()[1] <= 800) and kdpress >= 0.05:
                mpos = (215, 485)
                kdpress = 0
            elif (key[pygame.K_l] or event.type == pygame.MOUSEBUTTONDOWN and 400 < pygame.mouse.get_pos()[
                0] < 800 and 0 < pygame.mouse.get_pos()[1] <= 400) and kdpress >= 0.05:
                mpos = (515, 295)
                kdpress = 0
            elif (key[pygame.K_SEMICOLON] or event.type == pygame.MOUSEBUTTONDOWN and 400 < pygame.mouse.get_pos()[
                0] < 800 and 400 < pygame.mouse.get_pos()[1] <= 800) and kdpress >= 0.05:
                mpos = (525, 490)
                kdpress = 0
        tme += eggtime.tick() / 1000

        if tme >= lim:
            tme = 0
            if lim - 0.001 * multi >= 0.001:
                lim -= 0.001 * multi
            move = r.randint(1, 4)
            eggs.append(eggadd(move, screen))
        eggs, gametype = eggmove(eggs, mpos, multi)

        movem(mpos)

        if stmove >= 1:
            sty -= 20 * stpose
            stpose *= -1
            stmove = 0
        stmove += stickmove.tick() / 1000

        back = pygame.transform.scale(load_image('stickman.png'), (stx, sty))
        screen.blit(back, (310, 340 - 10 * stpose))

        if gametype == 1:
            score += 1
            gametype = 0
        elif gametype == 2:
            if gameover() == 1:
                pygame.quit()
                sys.exit()

        text = font.render(str(score), True, pygame.color.Color(light))
        text_x = width // 2 - text.get_width() // 2
        screen.blit(text, (text_x, 50))

        kdpress += kdtime.tick() / 1000
        # Это нужно оставить, чтоб мышка была выше яиц
        if pygame.mouse.get_focused():
            arrow(pygame.mouse.get_pos(), screen)
            pygame.mouse.set_visible(False)
        pygame.display.flip()


def gameover():
    font = pygame.font.Font(None, 250)
    pygame.mixer.music.set_volume(0.25)
    mus = True
    while mus:
        fon = pygame.transform.scale(load_image(fontype), (width, height))
        screen.blit(fon, (0, 0))

        if oblr != 0:
            oblt = pygame.transform.scale(load_image(f'obl{oblr}.png'), (width, height))
            screen.blit(oblt, (obl[0] - 0.005 * obl[1], 0))

        back = pygame.transform.scale(load_image(backtype), (width, height))
        screen.blit(back, (0, 0))

        back = pygame.transform.scale(load_image('stickman.png'), (stx, sty))
        screen.blit(back, (310, 340 - 10 * stpose))

        over = pygame.transform.scale(load_image('Game Over Screen.png'), (width, height))
        screen.blit(over, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1


            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                game()

        text = font.render(str(score), True, (255, 255, 255))
        text_x = width // 2 - text.get_width() // 2
        screen.blit(text, (text_x, 550))

        if pygame.mouse.get_focused():
            arrow(pygame.mouse.get_pos(), screen)
            pygame.mouse.set_visible(False)
        pygame.display.flip()


pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ну, поймай!')
start_screen(width, height)
pygame.mixer.music.load('data/Gameplay OST.wav')
pygame.mixer.music.play(-1)
game()
pygame.quit()
