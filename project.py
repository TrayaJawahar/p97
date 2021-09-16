import random
rnum = random.randint(1,9)
print ("GUESS A NUMBER BETWEEN 1 TO 9 ")
chance=0
while chance<5 :
    guess = int(input("ENTER UR GUESS : "))
    if guess==rnum :
        print ("CONGRATS U HAVE WON THE GAME")
        break
    elif guess > rnum :
        print("GUESS A LOWER NUMBER")
    else:
        print("GUESS A HIGHER NUMBER")
    chance=chance+1

if not chance<5:
    print ("U LOSE ... TRY AGAIN .. THE NUMBER IS :", rnum)

