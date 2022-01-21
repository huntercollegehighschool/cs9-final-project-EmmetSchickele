"""
Name(s): Emmet Schickele
Name of Project: Hangman (Python 1)
"""
d = 0

from page1 import chooseword

word = chooseword(d)

guessesleft = int(input("How many mistakes would you like? (Note: words are 5-10 letters long)"))

while guessesleft < 1:
  guessesleft = int(input("That is not a valid input. \nHow many mistakes would you like?"))



#word = "habitat"
letters = list(word)
currentword = []
for x in letters:
  currentword.append('_')
incorrect = []

while '_' in currentword and guessesleft > 0:
  currentword = ' '.join(currentword)
  incorrect = ','.join(incorrect)
  print(currentword, "\nGuessed letters not in the word: ", incorrect, "\n Mistakes left:", guessesleft)
  guess = input("Guess a letter: ")
  incorrect = incorrect.replace(',','')
  incorrect = list(incorrect)
  
  if guess in letters:
    currentword = currentword.replace(' ', '')
    currentword = list(currentword)
    for i in letters:
      if guess == i:
        getreplaced = -1
        for y in letters:
          getreplaced = getreplaced + 1
          if y == guess:
            currentword[getreplaced] = y
  elif guess not in letters:
    incorrect.append(guess)
    guessesleft = guessesleft - 1
    currentword = currentword.replace(' ', '')

if guessesleft == 0:
  print("You ran out of guesses. Better luck next time!")

else:
  print(word, "\nYou found the word! Congratulations!")





#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
