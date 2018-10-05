import random

num= random.randint(1,9)
guess=0
count=0
while guess != num and guess != 'exit':
    guess =int(input ("guess "))
    g=int(guess)
    if g> num:
        count +=1
        print(" Too high ")
    elif g< num:
        count += 1
        print (" Too low ")
if int(guess) == num :
    print ("you guessed number "+str(num) +" correct in "+str(count))
elif guess :
    print(" you failed to guess")