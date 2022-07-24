# filng color 
#begin fill
# end fill 

from turtle import*

# speed('slowest')
speed('fastest')
pencolor('red')
bgcolor('black')
pensize(5)


side = 3
size = 50
fillcolor('green')
begin_fill()
for i in range(side):
    fd(size)
    lt(90)
    fd(size)
    rt(90)
    
    rt(90)
end_fill()    
mainloop()   