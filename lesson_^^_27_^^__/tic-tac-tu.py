import random
import time

number=random.randint(1, 100)

def intro():
    print("may i ask you for your name")
    global name
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")
    if(number%2==0):
            x='even'
    else:
            x='odd'
    print("\nThis is an {} NUMBER".format(x))
    time.sleep(0.5)
    print("go ahead. Guess!")
def pick():
    gueesesTaken = 0
    
    while guessesTaken < 6:
        time.sleep(.25)
        enter=input("Guess: ")
        
        try:
            
            guess = int(enter)
            
            if guess<=100 and guess>=1:
                guessesTaken=guessesTaken+1
                
                if guessesTaken<6:
                    if guess<number:
                        print("the guess of the number is smALLER")
                        
                if guess>number:
                    print("the number is higher")
                    
                if guess !=number:
                    time.sleep(.5)
                    print("TRY AGAIN!!!")
                        
                if guess==number:
                    break
        
            if guess>100 or guess<1:
                print("yall is stupid as allways")
        
                time.sleep(.25)
                print("more than 1 or 100 yaaalll")
        except:
            print("i dont think enter is an number bro")
            
    if guess == number:
                guessesTaken = str(guessesTaken)
                print("you are finally correct".format(name, guessesTaken))
            
    if guess != number:
                print("nuuuuuuuuhuhuhuhuhuhuhuhuhuh")
    playagain="yessss"   
while playagain=="yessss" or playagain=="yeah"
intro()
pick()
    print("wonna die")
playagain=input()
        
    