
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
from replit import clear
import random
wdl = ["awkward", "balloon", "camel","egypt","oxford","physics","french","delhi","fantasy","idol","mysterious","mayonnaise","dinosaur","indian","penguin","buffalo","jogging","handkerchief","congratulations","confess","sanitizer","turkey","starving","magical","avenue","resort","yesterday","weird","kerchief","embarrass","cuttingplier","diamond"]
cw = random.choice(wdl)
#print(f'solution is {cw}.')
from hangman_art import logo
print(logo,"\n")
print("\nYou Have Only 6 Lives!! GOOD LUCK\n")
dis=["__"]*len(cw)
z=' '.join(dis)
print(z,"\n")

life=6

while "__" in dis:
  while life!=0:
    g = input("Guess a letter: ").lower()
    print("    ")
    
    clear()

    if g in dis:
      print(f"You have already guessed '{g}' ")

    for d in range(len(dis)):
      if g not in cw:
        life-=1
        print(stages[life])
        print(f"'{g}' is Wrong letter      lifes:",life)
        break
      elif cw[d]==g:
        dis[d]=g
    
    d=" ".join(dis)
    print(d,"\n",stages[life])
    if life==0:
        print("You lose!!   The Word is :",cw)
        print(" ")
    elif '__' not in dis:
      print("\nCongratulations Smarty!  👏")
      break
    

#logo = ''' 
#  _                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/    '''