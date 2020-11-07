import pygame
import sys
import math

# STUFF FOR EXECUTABLE
import os


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# GAME CONTENT
pygame.init()
fps = 50
clock = pygame.time.Clock()
sur_obj = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Keyboard_Input")
White = (255, 255, 255)
GREY = (128, 128, 128)
p1 = 10
p2 = 10
step = 6
SPRITE_SIZE = (32, 32)

f1 = pygame.image.load('walkc/f1.png').convert_alpha()
f2 = pygame.image.load('walkc/f2.png').convert_alpha()
f3 = pygame.image.load('walkc/f3.png').convert_alpha()
f4 = pygame.image.load('walkc/f4.png').convert_alpha()
f5 = pygame.image.load('walkc/f5.png').convert_alpha()

b1 = pygame.image.load('walkc/b1.png').convert_alpha()
b2 = pygame.image.load('walkc/b2.png').convert_alpha()
b3 = pygame.image.load('walkc/b3.png').convert_alpha()
b4 = pygame.image.load('walkc/b4.png').convert_alpha()
b5 = pygame.image.load('walkc/b5.png').convert_alpha()

s1 = pygame.image.load('walkc/s1.png').convert_alpha()
s2 = pygame.image.load('walkc/s2.png').convert_alpha()
s3 = pygame.image.load('walkc/s3.png').convert_alpha()
s4 = pygame.image.load('walkc/s4.png').convert_alpha()
s5 = pygame.image.load('walkc/s5.png').convert_alpha()

front = [f1, f2, f3, f4, f5]
back = [b1, b2, b3, b4, b5]
side = [s1, s2, s3, s4, s5]
char_state = {'front': front, 'back': back, 'left': side, 'right': side}

anim = 0
cur_pos = 'front'


def redrawGameWindow():
    global anim, p1, p2, char_state, step
    # sur_obj.blit(GREY, (0, 0))

    if anim + 1 >= len(front):
        anim = 0

    key_input = pygame.key.get_pressed()

    if key_input[pygame.K_LEFT]:
        sur_obj.blit(side[anim % 5], (p1, p2))
        anim += 1
        p1 -= step
    elif key_input[pygame.K_RIGHT]:
        sur_obj.blit(pygame.transform.flip(
            side[anim % 5], True, False), (p1, p2))
        # sur_obj.blit(char_state[cur_pos][anim//5 + 1], (p1, p2))
        anim += 1
        p1 += step
    else:
        if cur_pos == 'right':
            sur_obj.blit(pygame.transform.flip(
                side[0], True, False), (p1, p2))
        else:
            sur_obj.blit(char_state[cur_pos][0], (p1, p2))

    pygame.display.update()


while True:
    clock.tick(fps)
    # t = pygame.time.get_ticks()
    # # deltaTime in seconds.
    # getTicksLastFrame = t
    # dt = int(math.ceil((t - getTicksLastFrame) / 1000.0))
    # clock = pygame.time.Clock()
    # dt = clock.tick(fps)

    cur_rect = (p1, p2)
    sur_obj.fill(GREY)

    # if cur_pos != 'right':
    #     sur_obj.blit(char_state[cur_pos][anim], (p1, p2))
    # else:
    #     sur_obj.blit(pygame.transform.flip(
    #         char_state[cur_pos][anim], True, False), (p1, p2))

    # sur_obj.blit(front[anim], cur_rect)
    # pygame.draw.rect(sur_obj, (255, 0, 0), (p1, p2, 70, 65))
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key_input = pygame.key.get_pressed()

    if key_input[pygame.K_LEFT]:
        cur_pos = 'left'
        # sur_obj.blit(side[anim], (p1, p2))
    elif key_input[pygame.K_RIGHT]:
        cur_pos = 'right'

        # sur_obj.blit(pygame.transform.flip(side[anim], True, False), (p1, p2))
    # if key_input[pygame.K_UP]:
    #     p2 -= step
    #     anim += 1
    #     if anim >= len(front):
    #         anim = 0
    #     cur_pos = 'back'
    #     # sur_obj.blit(back[anim], (p1, p2))
    # elif key_input[pygame.K_DOWN]:
    #     p2 += step
    #     anim += 1
    #     if anim >= len(front):
    #         anim = 0
    #     cur_pos = 'front'
    #     # sur_obj.blit(front[anim], (p1, p2))

        # pygame.display.update()
    pygame.display.update()
    redrawGameWindow()

pygame.quit()
