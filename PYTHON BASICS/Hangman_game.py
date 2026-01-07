import random 
#import  hangman_stages
word_list = ["apple","beautiful","potato"]
lives=6
choosen_word=random.choice(word_list)
print(choosen_word)
display = []
for letter in choosen_word:
    display +=  '_'
print(display)
game_over = False
while not game_over:
    guess_letter=input("Guess a letter:").lower()
    for position in range(len(choosen_word)):
                           letter = choosen_word[position]
                           if letter ==guess_letter:
                                  display[position]=guess_letter
    print(display)
    if guess_letter not in choosen_word:
            lives = lives -1
            if lives == 0:
                    game_over =True
                    print("you lose!!")
    if '_'  not in display:
            game_over= True
            print("you win!!")
   # print(hangman_stages.stages[lives])
