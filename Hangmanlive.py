from words  import words_list
import random

def get_random():
    word=random.choice(words_list)
    return word.upper()

def main():
    print("Let's play hangman!!")

    word=get_random()
    #print(word)
    play(word)


def play(word):
    word_comp="_"*len(word)
    print("length of your word is",len(word))
    guessed=False       # by deafult we will keep it false
    guessed_letter=[]   # sometimes user may guess a letter correct
    guessed_word=[]     # sometimes user may guess word correct
    tries=6            # a finite amount of tries we will give to try
    print(word_comp)
    print(display_hangman(tries))


    while not guessed and tries > 0 :
        guess = input("Enter your guess").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print("You have already guessed this letter",guess)
            elif guess not in word:
                print(guess,"You have guessed the wrong leter")
                tries -= 1
                guessed_letter.append(guess)
                print(display_hangman(tries))
            else :
                print("God job!",guess,"is a right guess")
                guessed_letter.append(guess)
                word_as_list = list(word_comp)
                indices = [i for i,letter in enumerate(word) if letter==guess]
                for i in indices:
                    word_as_list[i]=guess
                word_comp="".join(word_as_list)
                if "_" not in word_comp:
                    guessed=True
                print(word_comp)


        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word :
                print("You have already guessed this word",guess)

            elif guess != word :
                print("sorry you have guessed the wrong word")
                tries-=1
                guessed_word.append(guess)

            elif guess == word:
                print("GOOD JOB!!",guess,"is the correct word")
                word_comp =guess
                guessed = True

        else:
            print("NOt a valid guess")


    if guessed == True :
        print(display_hangman(tries))
        print("congrats ! You win ",word,"is the right guess")
    else :
        print("Sorry !good luck for next time ,correct word is",word)




def display_hangman(tries):
    stages=[
            #6
            """
            
   
     ____________
    |          |
    |          o
    |         \\|/
    |          |
    |         /|\\
    |             
            """
            ,
            #5
            """ 
     ____________
    |          |
    |          o
    |         \\|/
    |          |
    |         /|
    |            
            """,
            #4
            """
      ____________
    |          |
    |          o
    |         \\|/
    |          |
    |         
    |            
             """,
            #3
            """ 
      ____________
    |          |
    |          o
    |         \\|/
    |          
    |         
    |              
            """,
            #2
            """ 
      ____________
    |          |
    |          o
    |         \\|
    |          
    |         
    |             
            """,
            #1
            """ 
      ____________
    |          |
    |          o
    |         
    |          
    |         
    |               
            """,
            #0
            """ 
      ____________
    |          |
    |          
    |         
    |          
    |         
    |            
            """

        ]
    return stages[tries]
main()
print()