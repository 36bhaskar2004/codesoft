import random



def choice(option):

    class WrongInputeError(Exception):
        def __init__(self,msg):
            super().__init__(msg)
    print(option)
    try:
        x=input("\nType your option=")
        if x not in option:
            raise WrongInputeError("\n\nPlease enter right speling!!")
        else:
            return x
    except WrongInputeError as w:
        print(w)
def score(your_score,computer_score):
    print("Your_score:",your_score)
    print("Computer_score:", computer_score)

def game():
   your_score=0
   computer_score=0
   print("\n**Game is Start**")
   while True:
       
       score(your_score,computer_score)

       option=["Rock","Paper","Scissors"]
       print("Select or type your one option from following List:")
       player=choice(option)

       computer=random.choice(option)
       print("\nYour choice:",player)
       print("Computer choice:",computer)

       if player==computer:
          print("\nGame is TIE!!")
       elif (player == "Rock" and computer == "Scissors" or   
             player == "Scissors" and computer == "Paper" or
             player == "Paper" and computer == "Rock"):
                print("\n**Your Win**")
                your_score += 1
       else:
            print("\n**Computer are Win**")    
            computer_score +=1

       print("\nSelect only one option from following:")
       print("Enter 1 for stay in Game")
       print("Enter 2 for Restart the Game")
       print("Enter 3 for Exist")
       a=int(input("Enter your choise:"))

       if a==1: 
           continue
       if a==2:
           score(your_score,computer_score)
           your_score=0
           computer_score=0
           print("\n**New Game Start**")
           continue
       if a==3:
           score(your_score,computer_score)
           print("**End**")
           break
       if a>3:
           print("Please enter correct number!!")

game()