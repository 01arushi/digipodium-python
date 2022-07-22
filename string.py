a=34
b="harry"
print(a,b)
print(type(b))

b="harry's" #--> use this if you have single quotes in your code

print(b)
 
name = "arushi"
greeting="good morning ,"
#print(type(name))
# print(greeting+name) 
c=greeting+name
print(c)

# now if we want two character from the string 
name = 'arushi'
print(name[0])
# name[3]='f' -----> does not work


# SLICING
name='Arushi'
print(name[0:3])
print(name[1:3])
print(name[0:5])
print(name[0:])
print(name[:3])
print(name[1:]) # string ki length aa jaayegi

# NEGATIVE INDESIS 
c=name[-4:-1]
print(c)

# skip values 
d=name[0::2]
d=name[1:4:2]
print(d)