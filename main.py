import random
num = random.randint(1,101)
a=-1
guesses = 1
while(a != num):
    a = int(input("enter your guess."))
    if (a > num):
        print('lower number please!!')
        guesses +=1
    elif(a<num):
        print('higher number please!!')
        guesses +=1 

print(f"you Guessed number {num} in {guesses} attempts.")