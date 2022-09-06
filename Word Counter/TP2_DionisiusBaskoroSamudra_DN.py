import matplotlib.pyplot as mp
import numpy as np

print ("="*50)
print ("Enter message : (Enter empty message to stop)")
print ('='*50)

#opening file from the same library
def stop_words (filename) :
    stop = open(filename,'r').read().split()
    return stop

end = stop_words ('stopword.txt')

#input message and lower all characters then split the message becomme a list
def word_input () :
    words = []
    while True :
        txt = input("Message : ").lower()
        if txt == "" :
            break
        else :
            split_text = txt.split()
            words += split_text
    return words

raw_words = word_input()

#strip all punctuations
def cleaning_dash (dash_punc) : 
    dash = []
    for item in (dash_punc) :
        x = item.strip('''!()[]{;:'"\,<>./?@#$%^&*_~}-''') 
        dash.append(x)
    return dash

clear_dash = cleaning_dash (raw_words)

#remove stopwords that exist the main list
def word_clearance (lst, message) :
    word_clear = []
    for letter in list(message) :
        if letter in lst or letter == "":
            message.remove(letter)
    word_clear += message

    return word_clear

clear_word = word_clearance (end, clear_dash)

print ("-" * 50)
print (f"{'No' : >2}{'Kata' : >6}{'Frekuensi' : >40}")
print ("-" * 50)

final_word = []
word_frequence = []

#make a list without any same words and the frequence of them
for kata in clear_word :
    if kata not in final_word :
        final_word.append(kata)
        word_frequence.append(1)
    
    else :
        word_frequence[final_word.index(kata)] += 1

for l in range (len(word_frequence)) :
    print (f"{(l+1) : >3} {final_word[l] : <35} {word_frequence[l] : <10}")

print('-' * 50)

#making the graphic using matplotlib
y_pos = np.arange(len(final_word))

mp.figure (figsize=(9,7))
mp.subplot (131)
mp.barh (final_word, word_frequence)
mp.yticks(y_pos, final_word)

mp.show()