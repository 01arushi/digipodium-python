import pgzrun

HEIGHT=500
WIDTH=600

P=Actor('ironmn1',(100,100))
speed=3

def draw():
    screen.clear()
    p.draw()

def update():
    player_control()
    def player_control():
        print('updating')
        if keyboard.RIGHT:
            p.x+=speed
        if keyboard.LEFT:
            p.x-=speed  
        if keyboard.UP:
            p.y+=speed 
        if keyboard.DOWN:
            p.y+=speed         

pgzrun.go()
