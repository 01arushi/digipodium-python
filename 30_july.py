from turtle import *

# pencolor('blue')
# pensize(3)
# speed('slowest')

# for i in range(4):
#     forward(100)
#     pencolor('red')
#     for i in range(6):
#         pencolor('crimson')
#         forward(100)
#         pencolor('black')
#         write(i, font=('arial',14,'normal'),align='left')
#         left(360/6)
#     left(360/4)    

# size=100
# side=6
# pencolor('blue')
# pensize(3)
# speed('fastest')

# for i in range(side):
#     pencolor('red')
#     # forward(size)
#     forward(size)
#     # pencolor('red')
#     for i in range(side):
#         pencolor('green')
#         forward(size//2)
#         pencolor('black')
#         # write(i, font=('arial',14,'normal'),align='left')
#         left(360/side)
#     left(360/side)    

size=40
side=8
pencolor('blue')
pensize(4)
speed('fastest')

for i in range(side):
    pencolor('red')
    # forward(size)
    forward(size)
    # pencolor('red')
    for i in range(side):
        fillcolor('black')
        pencolor('green')
        forward(size/3)
        pencolor('black')
        # write(i, font=('arial',14,'normal'),align='left')
        left(360/side)
        for i in range(side):
            # fillcolor('black')
            # begin_fill()
            pencolor('purple')
            forward(size/3)
            end_fill()
    pencolor('green')
    left(360/side)    


mainloop()    

