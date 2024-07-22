import random
n=5
to_be_gassed = int(n*random.random())+1

guess=0
while guess != to_be_gassed:
    guess = int(input("New Numbers:-"))
    if guess>0:
        if guess > to_be_gassed:
            print("Number is too large")
        elif guess< to_be_gassed:
            print("Number is too Small")
    else:
        print("sorry! that you are giving up!")
else:
    print("Congratulation . You are made it!")