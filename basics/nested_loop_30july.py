# for i in range(3):
#     for j in range(2):
#         print(i,j)



#         #while loop 

# start=100
# while start>0:
#     print('start:',start)
#     start-=8

from turtle import *

value=300

while value>0:
    pencolor('red')
    pensize('2')
    fd(value)
    lt(90)
    value-=10
    write(value)
mainloop()    

