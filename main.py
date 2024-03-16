from pygame import * 

window = display.set_mode((700, 600))
display.set_caption('Джангл')
#backround = transform.scale(image.load('background.jpg'), (700, 900))
mixer.init()
mixer.music.load('3d-z_uki-na-_oyne.mp3')
mixer.music.play()
#damage = mixer.Sound('dead.mp3')
#ssssssswon = mixer.Sound('win.mp3')

#шрифт

font.init()
font = font.Font(None, 70)
win = font.render('Москва твоя', True, (0, 255, 0))
lose = font.render('Москва не твоя', True, (255, 0 ,0))

clock = time.Clock()
FPS = 60
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, pl_x, pl_y, pl_speed, p_s_x, p_s_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (p_s_x, p_s_y))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 535:
            self.rect.y += self.speed
        if key_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 635:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direct = 'left'
    def update(self):
        if self.rect.x <= 450:
            self.direct = 'right'
        if self.rect.x >= 650:
            self.direct = 'left'
        
        if self.direct == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_hight):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.hight = wall_hight
        self.image = Surface((self.width, self.hight))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 100, 480, 10, 600)
w5 = Wall(154, 205, 50, 450, 200, 10, 600)


backround = GameSprite('background.jpg', 0, 0, 0, 700, 600)
hero = Player('gitler.png', 20, 500, 5, 65, 65)
enemy1 = Enemy('klipartz.com (1).png', 600, 350, 5, 50, 100)
past = GameSprite('kreml.png', 600, 500, 0, 100, 100)
# nein = mixer.Sound('hitler-nein23443.mp3')
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    backround.reset()
    hero.reset()
    enemy1.reset()
    past.reset()
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()



    hero.update()
    enemy1.update()
    w1.update()
    w2.update()
    w3.update()
    w4.update()
    w5.update()
    # key_pressed = key.get_pressed()
    # if key_pressed[K_r]: 
    #     nein.play()

    #проверка победы

    if sprite.collide_rect(hero, past):
        window.blit(win, (200,200))
        
        
    
    # проверка поражения

    if sprite.collide_rect(hero, enemy1) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5):
        window.blit(lose, (200,200))
        hero.rect.x = 0
        hero.rect.y = 450
        
    display.update()
    clock.tick(FPS)