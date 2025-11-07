def minimax(low, high):
    return (low + high) // 2

print("=== Number Guessing Game (AI using Minimax) ===")
print("Think of a number between 1 and 100. The AI will try to guess it!")

low, high = 1, 100
steps = 0

while True:
    guess = minimax(low, high)
    steps += 1
    print(f"\nAI guesses: {guess}")

    feedback = input("Is it (H)igh, (L)ow, or (C)orrect? : ").upper()

    if feedback == 'H':
        high = guess - 1
    elif feedback == 'L':
        low = guess + 1
    elif feedback == 'C':
        print(f"\nAI successfully guessed your number in {steps} steps!")
        break
    else:
        print("Invalid input. Please enter H, L, or C.")
