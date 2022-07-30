from turtle import *

# pencolor('blue')
# pensize(3)
# fillcolor('red')
# speed('fastest')
# for i in range(10,0,-1):
#     begin_fill()
#     circle(i*10)
#     lt(25)
#     end_fill()
# #goto(20,250)
# mainloop()  
  
#penup()  
# goto(-200,200)
# goto(200,200)
# pendown()
# goto(200,-200)
# write(' i am here ')
# goto(-200,-200)
# write('i am here')
# font=('arial',40,'normal')
# align=('center')
# mainloop()

# speed('slowest')
# penup()
#align=('upward')

# for i in range(3):
# fd(100)
# dot(50)
# goto(-250,250)
# rt(90)
# fd(100)
# rt(90)

# fd(50)
# dot(50)
# fd(100)
# dot(50)
# fd(50)
# lt(90)
# fd(100)
# lt(90)
# fd(100)
# dot(50)

# speed('slowest')
c=[(-200,200),
   (0,200),
   (200,200),
   (-100,100),
   (100,100),
   (0,0)
   ]
penup()
for i in range(6):
    goto(c[i])
    pendown()
    dot(50)
    penup()
mainloop()    















