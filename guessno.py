import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("Choose Difficulty Level:")
    print("1. Easy (1 - 10)")
    print("2. Medium (1 - 50)")
    print("3. Hard (1 - 100)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        max_number = 10
    elif choice == '2':
        max_number = 50
    elif choice == '3':
        max_number = 100
    else:
        print("❌ Invalid choice")
        return

    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"\nI have selected a number between 1 and {max_number}.")
    print("Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("🔻 Too low!")
        elif guess > secret_number:
            print("🔺 Too high!")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break

number_guessing_game()
