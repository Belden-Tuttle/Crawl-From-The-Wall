print("CRAWL FROM THE WALL")
print()
print("Welcome to Crawl from the Wall")
print("In this game you are an illeagle immigrint trying to escape")
print("Trumps boarder patrol. You are 100 miles from canada.")
print("And youre low rider has a gas leak. Good luck essay!")
print()

import random
distance_travled = 0
gas = 0
report = random.randrange(1,3)
distance_patrol = 20
lost = random.randrange(1,9)
racist_attack = random.randrange(1,15)


print("Youre choice")

done = False
while done == False:
    
    print("A: Pedal to the metal")
    
    print("B: Fill up gas")
    
    print("C: Ask for dirention")

    print("D: Check status")
    
    print("Q: Quit")

    lost = random.randrange(1,9)

    if lost == 4:
        print("You have taken a wrong turn and are now lost")       
        choice = input("")

        if choice == ("C"):  
            report = random.randrange(1,3)

            if report == (1):
                distance_travled = ( distance_travled - 5)
                print("A good samaritan pointed you in the right direction.")
                
            else:
                print("You have been put you under citizens arrest.")
                print("Game over")
                done = True
                    
        else:
            print("Should have asked for directions")
            print("Game over")
            done = True

    choice = input("")

    if choice == ("Q"):
        done = True
    
    elif choice == ("A"):
        distance_travled = ( distance_travled + random.randrange( 10, 21))
        distance_patrol = ( distance_patrol - random.randrange(10, 21) + random.randrange(5, 21)) 
        gas = ( gas + 1)
        print("You have travled ", distance_travled)
        
    elif choice == ("B"):
        gas = (0)
        distance_patrol = ( distance_patrol - random.randrange( 1, 6))
        print("Youre tank is full..... for now")
        

    if choice == ("D"):
        print("Miles travled ", distance_travled)
        print("Distance from boarder patrol ", distance_patrol)

    if distance_travled >= (100):
        print("Welcome to Canda a")
        print("Congragulations you reached Canada safely!")
        print("You win")
        done = True

    if gas == (3) and done == False:
        print("Running low on gas! Must refill tank.") 

    elif gas == (4):
        print("Ran out of gas! Boarder patrol has caught up to you.")
        print("Game over")
        done = True

    if distance_patrol <= (0):
        print("Got to be faster than that")
        print("Boarder patrol has caught up to you")
        print("Game over")
        done = True

    elif distance_patrol < (10) and done == False:
        print("Boarder patrol is close")
        
    racist_attack = random.randrange(1,15)
    if racist_attack == (1):
        print("A group of racist recognise youre car from the news")
        print("and have blocked you off")
        print("Game over")
        done = True
    

    print()
    
