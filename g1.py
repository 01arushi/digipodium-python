import pgzrun

HEIGHT =500
WIDTH = 600

p=Actor('ironman',pos=(100,100))

def draw():
    screen.clear()
    screen.draw.text("welcome to pgzero",(10,10),color='red',fontsize=20)
    screen.draw.text('created by Arushi Saxena', (10,40),color='white')
    p.draw

    # outside function
pgzrun.go()    