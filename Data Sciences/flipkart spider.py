from dputils import scrape 

# step 1 . get the data as soup obj 
# step 2 . create the setuo dictionaries
# step 3 . pass the dictonaries nto the extract_many() function
# step 4 . repeat step 1 to step 3 until data keep coming 
# step 5 . check and save data into a file 

# understanding the url 

url ='https://www.flipkart.com/search?q=laptop%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

query = 'laptop'
pos = 1 # page number 
url = f'https://www.flipkart.com/search?q={query}&page={pos}'
# print(url)
soup = scrape.get_webpage_data(url)

# step 2 
# target dic , items dict,etc
t = { 'tag':'div','attrs':{'class':'_1YokD2_3Mn1Gg'}}

# data collect process 