import random

# List of animals
animals = ['Mouse', 'Cat', 'Dog', 'Wolf', 'Elephant']

# Show animal menu
print("Animal List:")
print("1- Mouse")
print("2- Cat")
print("3- Dog")
print("4- Wolf")
print("5- Elephant")

# Player selection
while True:
    try:
        choice = int(input("Choose your animal (1-5): "))
        if 1 <= choice <= 5:
            player = animals[choice-1]
            break
        else:
            print("Please enter a number between 1-5!")
    except:
        print("Invalid input! Please enter a number.")

# Computer selections
computer1 = random.choice(animals)
computer2 = random.choice(animals)

print("\nChoices:")
print("You:", player)
print("Computer 1:", computer1)
print("Computer 2:", computer2)

# Calculate scores
your_score = 0
computer1_score = 0
computer2_score = 0

# Special rule: Mouse beats Elephant
if player == 'Mouse' and computer1 == 'Elephant':
    your_score += 1
elif player == 'Elephant' and computer1 == 'Mouse':
    computer1_score += 1
elif animals.index(player) > animals.index(computer1):
    your_score += 1
else:
    computer1_score += 1

if player == 'Mouse' and computer2 == 'Elephant':
    your_score += 1
elif player == 'Elephant' and computer2 == 'Mouse':
    computer2_score += 1
elif animals.index(player) > animals.index(computer2):
    your_score += 1
else:
    computer2_score += 1

if computer1 == 'Mouse' and computer2 == 'Elephant':
    computer1_score += 1
elif computer1 == 'Elephant' and computer2 == 'Mouse':
    computer2_score += 1
elif animals.index(computer1) > animals.index(computer2):
    computer1_score += 1
else:
    computer2_score += 1

# Show results
print("\nScores:")
print("You:", your_score)
print("Computer 1:", computer1_score)
print("Computer 2:", computer2_score)

# Determine winner
if your_score > computer1_score and your_score > computer2_score:
    print("\nYou win!")
elif computer1_score > your_score and computer1_score > computer2_score:
    print("\nComputer 1 wins!")
elif computer2_score > your_score and computer2_score > computer1_score:
    print("\nComputer 2 wins!")
else:
    print("\nIt's a tie!")