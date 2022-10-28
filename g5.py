 from ctypes.wintypes import HACCEL
import pgzrun

HEIGHT = 500
WIDTH = 500

class Player(Actor):
    speed =3

    def move(self):
        if keyword.LEFT and self.left>0:
            self.x += -self.speed
        if keyboard.RIGHT and self.right< WIDTH:
            self.x += self.speed

p = Player('ironmn1', pos=(100,100))

def draw():
    screen.clear()
    p.draw()

def update():
    p.move()

pgzrun.go        
