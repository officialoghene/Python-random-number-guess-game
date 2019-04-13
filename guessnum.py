import random

num = random.randint(1, 20)# Computer number

# looping until user guesses the number
while True:
    guess = input("Enter a number >> ")  # user enters their guess
    if len(guess) == 0 or guess.isalpha():  # checking if user didn't enter a number or entered nothing
        print("Invalid input, Please Enter a Number ")
    elif len(guess) > 0 and guess.isdigit():  # Converting input from string to integer
        value = int(guess)
        if value == num:
            print("Ho Ho Ho! You guessed correct \n{} Is The Number".format(value))
            break
        else:
            print("Aaaaah! That's Wrong. Try again")
    else:
        break
