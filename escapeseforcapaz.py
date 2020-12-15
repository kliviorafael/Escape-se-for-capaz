import pygame
from pygame.locals import * 

# Definições de Tela e Velocidade
SCREEN_WIDTH = WIDTH = 1510
SCREEN_HEIGHT = HEIGHT = 800
GAME_SPEED = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Definições do Boneco
class Boneco(pygame.sprite.Sprite): 

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) 
        super(). __init__()

        self.images = [pygame.image.load('Idle (1).png').convert_alpha(),
                       pygame.image.load('Idle (2).png').convert_alpha(),
                       pygame.image.load('Idle (3).png').convert_alpha(),
                       pygame.image.load('Idle (4).png').convert_alpha(),
                       pygame.image.load('Idle (5).png').convert_alpha(),
                       pygame.image.load('Idle (6).png').convert_alpha(),
                       pygame.image.load('Idle (7).png').convert_alpha(),
                       pygame.image.load('Idle (8).png').convert_alpha(),
                       pygame.image.load('Idle (9).png').convert_alpha(),
                       pygame.image.load('Idle (10).png').convert_alpha(),
                       pygame.image.load('Idle (11).png').convert_alpha(),
                       pygame.image.load('Idle (12).png').convert_alpha(),
                       pygame.image.load('Idle (13).png').convert_alpha(),
                       pygame.image.load('Idle (14).png').convert_alpha(),
                       pygame.image.load('Idle (15).png').convert_alpha()]

        self.current_image = 0

        self.image = pygame.image.load('idle (1).png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH / 4
        self.rect.y = SCREEN_HEIGHT / 3

        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y): 
        self.change_x += x
        self.change_y -= y

    def update(self):
        self.current_image = (self.current_image + 1) % 15
        self.image = self.images [ self.current_image ]
        self.rect.x += self.change_x
        self.rect.y += self.change_y

# Definições do Grupo Portas 

class Porta1(pygame.sprite.Sprite): 

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 

        self.images = pygame.image.load('porta.png').convert_alpha()

        self.current_image = 0

        self.image = pygame.image.load('porta.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 1.4
        self.rect[1] = SCREEN_HEIGHT / 1.82

class Porta2(pygame.sprite.Sprite): 

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 

        self.images = pygame.image.load('porta.png').convert_alpha()

        self.current_image = 0

        self.image = pygame.image.load('porta.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2.2
        self.rect[1] = SCREEN_HEIGHT / 1.82

class Porta3(pygame.sprite.Sprite): 

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 

        self.images = pygame.image.load('porta.png').convert_alpha()

        self.current_image = 0

        self.image = pygame.image.load('porta.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 4.2
        self.rect[1] = SCREEN_HEIGHT / 1.82

class Porta4(pygame.sprite.Sprite): 

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 

        self.images = pygame.image.load('porta.png').convert_alpha()

        self.current_image = 0

        self.image = pygame.image.load('porta.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 22
        self.rect[1] = SCREEN_HEIGHT / 1.82

# Carregamentos de imagens e sons

pygame.init()
screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('planomaior.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.mixer.music.load('10convert.com_Dark-Music-The-Master-Of-Death-Immortality_ZL1LBle8rTI.ogg')
pygame.mixer.music.play()

pygame.display.set_caption("comando")
comando = pygame.image.load('comando.png')

pygame.display.set_caption("abertura")
abertura = pygame.image.load('abertura.png')

pygame.display.set_caption("susto screen")
susto = pygame.image.load('susto.png')

pygame.display.set_caption("Game Over")

click_sound = pygame.mixer.Sound ('10convert.com_O-GRITO-DO-TERROR_JVNLsiu9Q0c.ogg')

passou = pygame.image.load('passou.png')


#Grupos 

menino_group = pygame.sprite.Group()
menino = Boneco(432, 361)
menino_group.add(menino)

door_group1 = pygame.sprite.Group()
door1 = Porta1()
door_group1.add(door1)

door_group2 = pygame.sprite.Group()
door2 = Porta2()
door_group2.add(door2)

door_group3 = pygame.sprite.Group()
door3 = Porta3()
door_group3.add(door3)

door_group4 = pygame.sprite.Group()
door4 = Porta4()
door_group4.add(door4)


clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

display_instructions = True
instruction_page = 1

#Inicio do Laço

done = False 

while not done and display_instructions : 

    clock.tick(90)

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True 
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False

    if instruction_page == 1:

        screen.blit(abertura, (90, 60))
        
    if instruction_page == 2:

        text = font.render("Instruções", True, WHITE)
        screen.blit(text, [10, 10])

        screen.blit(comando, (300, 250))
  
    clock.tick(90)


    pygame.display.flip()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Movimento
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                menino.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                menino.changespeed(3, 0)

        # Reseta a velocidade na troca do movimento
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                menino.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                menino.changespeed(-3, 0)


        # Interações com as portas
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if x > 86 and y > 454 and x < 238 and y < 724: 
                screen.fill(BLACK)
                click_sound.play()
                screen.blit(susto, [300, 250])
            elif  x > 360 and y > 441 and x < 527 and y < 724: 
                screen.fill(BLACK)
                click_sound.play()
                screen.blit(susto, [300, 250])
            elif  x > 705 and y > 454 and x < 855 and y < 724:
                screen.fill(BLACK)
                click_sound.play()
                screen.blit(susto, [300, 250]) 
            elif  x > 1096 and y > 456 and x < 1249 and y < 721:
                screen.fill(WHITE)
                screen.blit(passou, [300, 250])
        
    
    clock.tick(90)


    # Updates e Desenhos de Tela
    pygame.display.flip()

    screen.blit(BACKGROUND, (0, 0))
    
    door_group1.update()
    door_group1.draw(screen)

    door_group2.update()
    door_group2.draw(screen)

    door_group3.update()
    door_group3.draw(screen)

    door_group4.update()
    door_group4.draw(screen)

    menino_group.update()
    menino_group.draw(screen)


    clock.tick (90)
    pygame.display.update()


pygame.quit()
