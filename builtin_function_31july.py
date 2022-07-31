


# chr()- convert integer to string character
# ord()- convert a char to integer
# len()- returns length of string
# str()- convert items to string

# str=chr(65)
# print(str)
# str=chr(2365)
# print(str)
# str=chr(12365)
# print(str)

for i in range(1000 , 16000):
    print(f'{i} : {chr(i)}', end='\t\t')
    if i %10 ==0:
     print()