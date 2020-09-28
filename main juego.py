import random
import pygame
import time
import sys
import pygame_menu
from pygame.locals import *

pygame.init()

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

# creamos el sprite boton
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal

        pantalla.blit(self.imagen_actual, self.rect)
#----------------------------------------------------------------
play = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\Practica\\sprites\\boton-de-play.png")
play_2 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\Practica\\sprites\\boton-de-play.png")
opcion_1 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\Practica\\sprites\\opciones.png")
opcion_2 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\Practica\\sprites\\opciones.png")
boton1 = Boton(play, play_2, 100, 50)
boton2 = Boton(opcion_1, opcion_2, 100, 350)
cursor1 = Cursor()
#----------------------------------------------------------------
#op_Img = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\op_re.png")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
click = False
pause=False
screen = pygame.display.set_mode((800, 600))

class Dino():
    def __init__(self):
        self.Img = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\dino_.png")
        self.Img.set_colorkey([255, 255, 255])
        self.WIDTH, self.HEIGHT = 70, 90
        self.Img = pygame.transform.scale(self.Img, (self.WIDTH, self.HEIGHT))
        self.image = self.Img
        self.x = 20
        self.y = 450
        self.g = -0.25  # Gravity
        self.up = 13  # Initial upward velocity
        self.t = 0  # time
        self.hitbox = pygame.Rect(self.x + 5, self.y, self.WIDTH - 15, self.HEIGHT - 5)

        self.runImg1 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\dino_1.png")
        self.runImg1.set_colorkey([255, 255, 255])
        self.runImg2 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\dino_2.png")
        self.runImg2.set_colorkey([255, 255, 255])
        self.runImg1 = pygame.transform.scale(self.runImg1, (self.WIDTH, self.HEIGHT))
        self.runImg2 = pygame.transform.scale(self.runImg2, (self.WIDTH, self.HEIGHT))

        self.duck1 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\dino_ducking1.png")
        self.duck2 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\dino_ducking2.png")
        self.duck1 = pygame.transform.scale(self.duck1, (self.WIDTH + 15, self.HEIGHT))
        self.duck2 = pygame.transform.scale(self.duck2, (self.WIDTH + 15, self.HEIGHT))
        self.ducking = False

        self.duckImgs = [self.duck1, self.duck2]

        self.runImgs = [self.runImg1, self.runImg2]

        self.jump_sound = pygame.mixer.Sound("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\jump.wav")
        self.count = 0
        self.jumping = False

    def jump(self):
        self.y -= self.up  # Start jumping
        self.jumping = True
        self.jump_sound.play()

    def update(self):
        if self.y < 450:  # check if jumping
            self.up = self.up + self.g * self.t  # v = u + at
            self.y -= self.up
            self.t += 0.15  # incrementing time

        if self.y > 450:  # check if the jump is complete and resetting all variables
            self.y = 450
            self.t = 0
            self.up = 13
            self.jumping = False

        if self.ducking:
            self.hitbox = pygame.Rect(self.x + 5, self.y + 20, self.WIDTH + 12, self.HEIGHT - 20)
            self.image = self.duckImgs[int(self.count) % 2]
            self.count += 0.2
        elif self.jumping:
            self.hitbox = pygame.Rect(self.x + 5, self.y, self.WIDTH - 15, self.HEIGHT - 5)
            self.image = self.Img
        else:
            self.hitbox = pygame.Rect(self.x + 5, self.y, self.WIDTH - 15, self.HEIGHT - 5)
            self.image = self.runImgs[int(self.count) % 2]
            self.count += 0.2

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2) In case you want to see the hitbox

class Ptera():
    def __init__(self):
        self.WIDTH, self.HEIGHT = 50, 40
        self.im1 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\ptera1.png")
        self.im2 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\ptera2.png")

        self.im1 = pygame.transform.scale(self.im1, (self.WIDTH, self.HEIGHT))
        self.im2 = pygame.transform.scale(self.im2, (self.WIDTH, self.HEIGHT))

        self.flaps = [self.im1, self.im2]

        self.image = None
        self.allowed = False

        self.x = 20000
        self.y = 175
        self.altitudes = [175, 150, 110]
        self.speed = 5
        self.count = 0

        self.hitbox = (self.x, self.y + 10, self.WIDTH, self.HEIGHT - 12)

    def create(self):
        self.x = random.randint(100, 200) * 10  # generate a random position for ptera
        self.y = random.choice(self.altitudes)

    def update(self):
        if self.allowed:
            self.create()
            self.allowed = False

        self.image = self.flaps[int(self.count) % 2]  # Flapping mechanism
        self.count += 0.1

        self.x -= self.speed

        if self.x < 50:
            self.allowed = True

        self.hitbox = pygame.Rect(self.x, self.y + 10, self.WIDTH, self.HEIGHT - 12)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2) In case you want to see the hitbox

class Cactus():
    def __init__(self):
        self.image0 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\cacti-small.png")
        self.image0.set_colorkey([255, 255, 255])
        self.image1 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\cacti-big.png")
        self.image1.set_colorkey([255, 255, 255])
        self.width0 = 60
        self.height = 80
        self.width1 = 80
        self.image0 = pygame.transform.scale(self.image0, (self.width0, self.height))
        self.image1 = pygame.transform.scale(self.image1, (self.width1, self.height))
        self.cacti_dist = 450
        self.x0 = 1350
        self.y = 450
        self.x1 = self.x0 + self.cacti_dist
        self.x2 = self.x1 + self.cacti_dist - 100
        self.speed = 4

        self.hitbox0 = pygame.Rect(self.x0, self.y, self.width0, self.height)
        self.hitbox1 = pygame.Rect(self.x1, self.y, self.width1, self.height)
        self.hitbox2 = pygame.Rect(self.x2, self.y, self.width0, self.height)
        self.hitboxes = [self.hitbox0, self.hitbox1, self.hitbox2]

    def update(self):
        self.x0 -= self.speed
        self.x1 -= self.speed
        self.x2 -= self.speed

        self.hitbox0 = pygame.Rect(self.x0, self.y, self.width0, self.height)
        self.hitbox1 = pygame.Rect(self.x1, self.y, self.width1, self.height)
        self.hitbox2 = pygame.Rect(self.x2, self.y, self.width0, self.height)
        self.hitboxes = [self.hitbox0, self.hitbox1, self.hitbox2]

        if self.x0 < -30:
            # self.x0 = 1500
            self.x0 = 1400
        elif self.x1 < -30:
            # self.x1 = 1500
            self.x1 = self.x0 + random.randint(300, 700)
        elif self.x2 < -30:
            # self.x2 = 1500
            self.x2 = self.x1 + random.randint(300, 700)

    def draw(self, screen):
        screen.blit(self.image0, (self.x0, self.y))
        screen.blit(self.image1, (self.x1, self.y))
        screen.blit(self.image0, (self.x2, self.y))


class Ground():
    def __init__(self):
        self.ground_length = 1202
        self.image1 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\ground.png")
        self.image1.set_colorkey([255, 255, 255])
        self.image1_x = 0
        self.image1_y = 500
        self.image2 = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\ground.png")
        self.image2_x = self.image1_x + self.ground_length
        self.image2_y = self.image1_y
        self.speed = 4

    def draw(self, screen):
        screen.blit(self.image1, (self.image1_x, self.image1_y))
        screen.blit(self.image2, (self.image2_x, self.image2_y))

    def update(self):
        self.image1_x -= self.speed
        self.image2_x -= self.speed

        if self.image1_x + self.ground_length < 0:
            self.image1_x = self.image2_x + self.ground_length
        elif self.image2_x + self.ground_length < 0:
            self.image2_x = self.image1_x + self.ground_length


class Cloud():

    def __init__(self):
        self.image = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\cloud.png")
        self.WIDTH, self.HEIGHT = 200, 100
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.image.set_colorkey([255, 255, 255])
        self.speed = 1
        self.x = 600
        self.y = 50

    def update(self):
        self.x -= self.speed
        self.image.set_colorkey([255, 255, 255])

        if self.x < -self.WIDTH:
            self.x = 600
            self.y = random.randint(10, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.image.set_colorkey([255, 255, 255])


def Pause(score_value):
    pause = True
    screen = pygame.display.set_mode((800, 300))
    clock = pygame.time.Clock()
    font = pygame.font.Font("freesansbold.ttf", 20)
    check_point = pygame.mixer.Sound("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\checkpoint.wav")
    death_sound = pygame.mixer.Sound("die.wav")
    pygame.display.set_caption("Dino Run")
    dino_icon = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\dino_.png")

    pygame.display.set_icon(dino_icon)

    game_over = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\spritesgame_over.png")
    replay_button = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\spritesdeplay.png")
    logo = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\spriteslogo.png")
    GREY = (240, 240, 240)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    ground = Ground()
    dino = Dino()
    cactus = Cactus()
    cloud = Cloud()
    ptera = Ptera()

    running = False
    play_game = True
    dead = False
    high_score_value = 0
    FPS = 60
    while pause:

        clock.tick(FPS)  # Controlling Frames Per Second

        score = font.render("Score: " + str(int(score_value)), True, (200, 200, 200))
        score_value += 0.25
        high_score_value = max(high_score_value, score_value)
        high_score = font.render("High Score: " + str(int(high_score_value)), True, (200, 200, 200))
        screen.fill(GREY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_e:
                    pause = False
                elif event.key == pygame.K_r:
                    pygame.quit()
                    quit()
        ground.update()
        ground.draw(screen)

        cloud.update()
        cloud.image.set_colorkey([255, 255, 255])
        cloud.draw(screen)

        dino.update()
        dino.draw(screen)

        cactus.update()
        cactus.draw(screen)

        ptera.update()
        ptera.draw(screen)

        screen.blit(score, (650, 30))
        screen.blit(high_score, (450, 30))

        if int(score_value) % 100 == 0 and int(
                score_value) % 3 == 0:  # Increase game speed after score crosses a multiple of 300
            cactus.speed += 0.25
            ground.speed += 0.25

            if score_value == 500.0:  # ptera is allowed to spawn after score crosses 500
                ptera.allowed = True

            if score_value > 1 and score_value % 100 == 0:  # Checkpoint sound after score crosses a multiple of 100
                check_point.play()

            closest_hitbox = min(cactus.hitbox0, cactus.hitbox1, cactus.hitbox2)  # Hitbox of closest cactus

            if dino.hitbox.colliderect(closest_hitbox):  # Collision detection with closest cactus
                death_sound.play()
                dead = True
                screen.blit(game_over, (200, 70))
                screen.blit(replay_button, (360, 100))

            if dino.hitbox.colliderect(ptera.hitbox):  # Collision detection with ptera
                death_sound.play()
                dead = True
                screen.blit(game_over, (200, 70))
                screen.blit(replay_button, (360, 100))

            pygame.display.update()

            if dead:
                del dino
                del ground
                del cactus
                del ptera
                running = False


def options(): 
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        clock.tick(60)

#----------------------------------------------------------------
#----------------------------------------------------------------

def main_menu():
    while True:
        screen.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()
       # button_1 = pygame.Rect(50, 100, 200, 50)   //rectangulos con orientacion a otros menus
       # button_2 = pygame.Rect(50, 200, 200, 50)
        
        #------Area de dibujo
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
       # pygame.draw.rect(screen, (255, 0, 0), button_1)    //estos son mis rectangulos rojos
       # pygame.draw.rect(screen, (255, 0, 0), button_2)    //estos son mis rectangulos rojos
              #estos son los botones nuevos
        #------Area de dibujo-
        #------Seccion de seleccion de Menu
        #if button_1.collidepoint((mx, my)):
        #    if click:
        #        Game()
        #if button_2.collidepoint((mx, my)):
         #   if click:
         #       options()
        #------Fin Seccion de seleccion de Menu
        cursor1.update()    #si no llamo este metodo no funcionara al ahcer click
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #if event.type == KEYDOWN:
                #if event.key == K_ESCAPE:
                    #pygame.quit()
                    #sys.exit()
            #if event.type == MOUSEBUTTONDOWN:
                #if event.button == 1:
                    #click = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    Game()
                if cursor1.colliderect(boton2.rect):
                    options()
        boton1.update(screen,cursor1)       #estos son los botones nuevos
        boton2.update(screen,cursor1) 
                
 
        pygame.display.update()
        clock.tick(60)



def Game():
    fondo = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\fondo.png")
    fondo_juego = pygame.transform.scale(fondo, (800, 600))
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font("freesansbold.ttf", 20)
    check_point = pygame.mixer.Sound("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\checkpoint.wav")
    death_sound = pygame.mixer.Sound("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\die.wav")
    pygame.display.set_caption("Dino Run")
    dino_icon = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\dino_.png")

    pygame.display.set_icon(dino_icon)

    game_over = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\game_over.png")
    replay_button = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\deplay.png")
    logo = pygame.image.load("D:\\Documentos owo\\Documentos\\Universidad\\Seminarios de Lenguajes\\Codigo\\TP Final\\pygame-unla-master\\sprites\\logo.png")
    GREY = (240, 240, 240)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    ground = Ground()
    dino = Dino()
    cactus = Cactus()
    cloud = Cloud()
    ptera = Ptera()
    running = False
    play_game = True            #esta variable activa o no el loop
    dead = False
    high_score_value = 0
    FPS = 36
    
    while play_game:           #mientras seaa True andara este loop que es el que contiene los demas loop (es loop principal)
       

        if not dead:
            ######## screen.fill(GREEN)
            screen.blit(fondo_juego, [0, 0])
            ground.draw(screen)
            screen.blit(dino.image, (dino.x, dino.y))
            screen.blit(logo, (200, 70))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                play_game = False       #si decidimos cerrar la ventana la variable cambia a false y se cierra el loop principal
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #si presiona SPACE arranca el otro loop y todos los procesos que hacen funcionar el resto del juego
                    running = True      #este booleano se pone en True al presionar barra espaciadora y activa el loop de mas abajo
                    ground = Ground()
                    dino = Dino()
                    cactus = Cactus()
                    ptera = Ptera()
                    dead = False
                    running = True
                    score_value = 0

        while running:
            clock.tick(FPS)  # Controlling Frames Per Second

            score = font.render("Score: " + str(int(score_value)), True, (200, 200, 200))
            score_value += 0.25
            high_score_value = max(high_score_value, score_value)
            high_score = font.render("High Score: " + str(int(high_score_value)), True, (200, 200, 200))
            #####screen.fill(GREY)
            screen.blit(fondo_juego, [0, 0])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dino.jump()
                    elif event.key == pygame.K_DOWN:
                        dino.ducking = True
                    elif event.key == pygame.K_e:
                        Pause(score_value)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        dino.ducking = False

            ground.update()
            ground.draw(screen)

            cloud.update()
            cloud.image.set_colorkey([255, 255, 255])
            cloud.draw(screen)

            dino.update()
            dino.draw(screen)

            cactus.update()
            cactus.draw(screen)

            ptera.update()
            ptera.draw(screen)

            screen.blit(score, (650, 30))
            screen.blit(high_score, (450, 30))

            if int(score_value) % 100 == 0 and int(
                    score_value) % 3 == 0:  # Increase game speed after score crosses a multiple of 300
                cactus.speed += 0.25
                ground.speed += 0.25

            if score_value == 500.0:  # ptera is allowed to spawn after score crosses 500
                ptera.allowed = True

            if score_value > 1 and score_value % 100 == 0:  # Checkpoint sound after score crosses a multiple of 100
                check_point.play()

            closest_hitbox = min(cactus.hitbox0, cactus.hitbox1, cactus.hitbox2)  # Hitbox of closest cactus

            if dino.hitbox.colliderect(closest_hitbox):  # Collision detection with closest cactus
                death_sound.play()
                dead = True
                screen.blit(game_over, (200, 70))
                screen.blit(replay_button, (360, 100))

            if dino.hitbox.colliderect(ptera.hitbox):  # Collision detection with ptera
                death_sound.play()
                dead = True
                screen.blit(game_over, (200, 70))
                screen.blit(replay_button, (360, 100))

            pygame.display.update()

            if dead:
                del dino
                del ground
                del cactus
                del ptera
                running = False


# enconding: utf-8

#Game()
main_menu()
