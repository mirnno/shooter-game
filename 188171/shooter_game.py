#Create your own shooter
from pygame import *
from random import randint
bullets = sprite.Group()


class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (105,105))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class america(Gamesprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT] and self.rect.x < 799:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 00:
            self.rect.x -= self.speed
    def fire(self):
        rocket = bullet("bullet.png",self.rect.x,self.rect.y,5)
        bullets.add(rocket)
class alien(Gamesprite):
    
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 550:
            self.rect.y = 0
            self.rect.x = randint(50,900)
class bullet(Gamesprite):
    def update(self):
        self.rect.y -= self.speed


window = display.set_mode ((900,700))
display.set_caption("shooter")
backround = transform.scale (image.load("galaxy.jpg"), (900,700))
game = True
clock = time.Clock()
FPS = 60
freedom_maker = america("rocket.png",70,550,18)

monsters = sprite.Group()


for i in range(30):
    ufo1 = alien("ufo.png",randint(50,900),0,randint(1,2))
    monsters.add(ufo1)

font.init()
font1 = font.Font(None,70)
score1 = 0
score = font1.render("score:"+str(score1),True,(255,255,255))
missed = font1.render("missed:"+str(missed1),True,(255,255,255))

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    keys_pressed = key.get_pressed()
    if keys_pressed[K_SPACE]:
        freedom_maker.fire()
    collides = sprite.groupcollide(monsters,bullets,True,True)
    for i in collides:
        score1 += 1
        ufo = alien("ufo.png",randint(0,650),10,7)
        monsters.add(ufo)
    window.blit(backround,(0,0))
    #window.blit(score,(30,30))
    window.blit(missed,(30,70))
    score = font1.render("score:"+str(score1),True,(255,255,255))
    window.blit(score,(20,20))
    freedom_maker.draw()
    freedom_maker.update()
    monsters.draw(window)
    monsters.update()
    bullets.draw(window)
    bullets.update()
    clock.tick(FPS)    
    display.update()

