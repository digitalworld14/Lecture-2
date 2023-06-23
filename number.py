import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("guess the number (between 1 and 100):"))

        attempts = 1
        if guess < secret_number:
            print("Too Low! Try Again")

        elif guess > secret_number:
            print("To High! Try Again")
        
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_number()
