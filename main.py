import random

print ("Welcome to the multiplication game Amelia.")
print ("How well do you know your 2-11 multiplication tables Amelia?")

for num in range(0,30):
    #pick the numbers to multiply
    number1 = random.randint(2,11)
    number2 = random.randint(2,11)
    answer = number1 * number2

    guess = 0
    print ("What is", number1, "x", number2, "?")

    while guess != answer:
        guess = input("Answer: ")
        guess = int(guess)
      
        if guess != answer:
            print ("No, try again")

    print ("You got it!")

print ("That's it, good work!")