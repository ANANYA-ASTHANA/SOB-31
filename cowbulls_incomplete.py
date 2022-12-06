import random
        
def compare_numbers(number, user_guess):
            print(number)
            cowbull=[0,0]
            for i in range(4):
                if number[i]==user_guess[i]:
                    cowbull[1]+=1
                elif user_guess[i] not in number:
                    continue
                elif user_guess[i] in number:
                    cowbull[0]+=1

            return cowbull

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number
guesses=0
print(number)
print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
      user_guess = input("Give me your best guess!") 
      if user_guess == "exit":
            break
      cowbullcount = compare_numbers(number, user_guess)
      guesses+=1

      print("You have "+ str(cowbullcount[0])+ " cows, and "+ str(cowbullcount[1]), " bulls.")
      

      if cowbullcount[1]==4:
            playing = False
            print("You win the game after ", guesses, " guess(es)! The number was ", number)
            break
      else:
            print("Your guess isn't quite right, try again.")
    
