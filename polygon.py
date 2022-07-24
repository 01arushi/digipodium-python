from turtle import*

speed('slowest')
pencolor('red')
bgcolor('black')
pensize(45)

side = 3
size = 100
for i in range(side):
    fd(size)
    lt(360/side)
mainloop()    