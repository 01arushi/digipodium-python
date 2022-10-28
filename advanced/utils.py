def char_counter(sentences):
    data={} # blank dict 
    for char in set(sentences):
        # print(char, sentences.count(char))
        data[char]= sentences.count(char)
    return data 

def word_counter(sentence):
    data={}
    words=sentence.split()
    for word in set(words):
        data[word]=words.count(word)
    return data

def remove_punc(sentences):
    '''removes punctuatio ( TBC)'''
    pass        