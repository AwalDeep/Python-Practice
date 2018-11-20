#HANGMAN

import random
list_words=['charizard','pikachu','bulbasaur','dragonite','chikorita','magikarp','gyarados','meowth','wobbuffet','totodile','zapdos','articuno','blastoise','vaporean']
o_word=list_words[random.randint(0,len(list_words)-1)]
g_word=''
k_chr=['a','e','i','o','u']
score=5
def gen_puzzle():
    global g_word
    g_word=o_word
    for x in o_word:
        if x not in k_chr:
            g_word=g_word.replace(x,' _ ')
    print(g_word)       


def g_input():
    global score
    global k_chr
    k_in=input("Enter guess alphabet")
    if k_in in o_word and k_in in k_chr :
        print ("Incorrect Guess")
        print (str(score-1)+"chances left" )
        score=score-1
    elif k_in in o_word and k_in not in k_chr :    
        k_chr.append(k_in)
        score=score+1
    elif k_in not in o_word:
        print ("Incorrect Guess")
        print (str(score-1)+"chances left" )
        score=score-1

c=True
while c:
    gen_puzzle()
    if g_word==o_word:
        print ("you won")
        print("score:"+str(score))
        c=False
    elif score==0:
        c=False
        print("you lost")
    else:
        g_input()
		
			