import pygame
import random
import math
# inicializace
pygame.init()

# Obrazovka
width = 700
height = 470
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("********** Vítejte  **********")

# Nastavení hry
fps = 60
clock = pygame.time.Clock()


# Classy
class Game:
    # nastavím konstruktor v něm bude skore, kolize, hudbu, obrázky
    def __init__(self, our_player):
        self.score = 0
        self.new_round = 0
        self.round_time = 0
        self.minute_time = 0
        self.slow_down_cycle = 0
        self.scroll = 0  # rolování rychlost
        self.tiles = math.ceil(width / height) + 1  # snímky zokrouhlí nahoru
        self.our_player = our_player

        # Fonty
        self.fire_font_big = pygame.font.Font("font/Xefora.ttf", 50)
        self.fire_font_middle = pygame.font.Font("font/Xefora.ttf", 25)

        # hudba v pozadí

        # obrázek hry, convert - namnoží obrázek, aby se pohyboval musí byt takto
        self.background_image = pygame.image.load("img/sky.png").convert()    # 1 obrazek nahraju
        self.background_width = self.background_image.get_width()       # šířku
        self.background_image_rect = self.background_image.get_rect()     # obrázek

    # kod který je volán dokla, třeba počítání času, hlídání kolize
    def update(self):
        # pohyb pozadí update obrázku pozadí aby se pohyboval
        for i in range(0, self.tiles):
            # provedu zdvojení obrázku, scroll zajistí pohyb
            screen.blit(self.background_image, (i * self.background_width + self.scroll, 0))
            self.background_image_rect.x = i * self.background_width + self.scroll     # zajistí pohyb
        self.scroll -= 2     # rychlost pohybu pozadí
        # reset scroll, abs - absolutní hodnota
        if abs(self.scroll) > self.background_width:
            self.scroll = 0

        # Počítání času
        self.slow_down_cycle += 1
        if self.slow_down_cycle == fps:
            self.round_time += 1
            self.slow_down_cycle = 0
            if self.round_time == 60:
                self.round_time = 0
                self.minute_time += 1

        # hlídání kolize
        self.check_collisions()

    # Vykresluje vše ve hře texty,a co mam udělat( veškeré texty aj jejich bliting
    def draw(self):                    # a třeba vakreslení čáry či ramečku či jineho obrazce
        # barvy
        dark_yellow = pygame.Color("#938f0c")

        # pozor texty bez self
        score_text = self.fire_font_middle.render(f"Score: {self.score}", True, dark_yellow)
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = (10, 5)  # můžu zapsat score_text_rect.topleft = (20, 5)
        # pozor na our_player.
        lives_text = self.fire_font_middle.render(f"Lives: {self.our_player.lives}", True, dark_yellow)
        lives_text_rect = lives_text.get_rect()
        lives_text_rect.topleft = (120, 5)

        round_time_text = self.fire_font_middle.render(f"Time: {self.minute_time} : {self.round_time}",
                                                       True, dark_yellow)
        round_time_text_rect = round_time_text.get_rect()
        round_time_text_rect.center = (width // 2, 20)

        new_round_text = self.fire_font_middle.render(f"Round: {self.new_round}", True, dark_yellow)
        new_round_text_rect = new_round_text.get_rect()
        new_round_text_rect.topright = (width - 10, 5)

        # blitnutí textu
        screen.blit(score_text, score_text_rect)
        screen.blit(lives_text, lives_text_rect)
        screen.blit(round_time_text, round_time_text_rect)
        screen.blit(new_round_text, new_round_text_rect)

    # Kontrola kolize, či sebrání předmětu, předání peněz,
    def check_collisions(self):        # dáme do update nahoře
        pass

    # start nového kola , nový nepřátelé, vyšší skore, víc nepřátel, jiné ukoly, atd
    def start_new_round(self):
        pass

    # výběr nového nepřítele
    def choose_new_target(self):
        pass

    # pausa hry hlevní text a podtext pro pauzu, vyplnění aj blitnuti
    def pause_game(self):
        pass

    # reset hry, když umřu vše vrátí na původní hodnoty, konec hudby
    def reset_game(self):
        pass


# Player (pygame.sprite.Sprite - dědím od někud v pozadí musí být)
class Player(pygame.sprite.Sprite):
    def __init__(self):    # obrázek, umístění, počet životů, rychlost, zvuk chycení, minutí
        super().__init__()        # dědění
        self.image = pygame.image.load("img/airplane.png")
        self.rect = self.image.get_rect()
        self.rect.center = (20, height // 2 + 190)     # výchozí pozice plane

        self.lives = 5
        self.speed = 5

    # update hráče
    def update(self):
        self.move()

    #  pohyb
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 50:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < height - 45:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.left > 20:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < 640:
            self.rect.x += self.speed

    # návrat do bezpečné zony
    def back_to_safe_zone(self):
        pass

    # vrácení pozice hráče když skončím hru
    def reset_game(self):
        pass


# zbraň
# class Gun:
    #def __init__(self):
     #   super().__init__()
      #  # nahrání střely
       # self.ammo_image = pygame.image.load("img/two-line-horizontal.png")
        #self.rect = self.ammo_image.get_rect()
     #   self.rect.center = (20, height // 2 + 190)
      #  self.ammo_number = 100
       # self.gun_speed = 100   # ryychlost střely

    #def update(self):    # střela na kliknutí myši
     #   if event.type == pygame.MOUSEBUTTONDOWN:
      #      screen.blit(self.ammo_image, self.rect)
       #     self.rect.x += self.gun_speed
        #    self.ammo_number -= 1

# Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):      # obrázky, umístění, pohyb, typy
        super().__init__()

    # update nepřátel
    def update(self):    # pohyb nepřátel
        pass


# Skupina nepřátelé

# Skupina hráč
player_group = pygame.sprite.Group()
one_player = Player()
player_group.add(one_player)

# zobrazení střely
# gun_group = pygame.sprite.Group()
# my_gun = Gun()
# gun_group.add(my_gun)

# Objekt Game vytvoření podle klasy Game, volám metodu na game vždy .
my_game = Game(one_player)   # konkretní nazvy, ne ty ve hře
# my_game.pause_game("Bitva s mozkomory", "Stiskni Enter pro pokracovani")   # musím update hoře
# my_game.start_new_round()    # nám začne novou hru, nedávat do cyklu

# Hlavní cyklus hry
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

        # přidáme další event, schování do zony
        # if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_SPACE:
        # one_player.back_to_save_zone()  # zavolám metodu na hráče

    # vyplnění obrazovky po pohybu

    # nahrání obrázku pozadí ve finále

    # update game
    my_game.update()
    my_game.draw()

    # update hráči
    player_group.draw(screen)
    player_group.update()

    # update zbraň
    # my_gun.update()

    # update nepřítel

    # update obrazovky
    pygame.display.update()

    # zpomalení cyklu hry
    clock.tick(fps)

# ukončení hry
pygame.quit()
