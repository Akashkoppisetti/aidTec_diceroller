import random

def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def display_results(results):
    print("Dice roll result:", ', '.join(str(result) for result in results))
    print("Total:", sum(results))

def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll (0 to quit): "))
            if num_dice < 0:
                print("Please enter a non-negative number.")
                continue

            if num_dice == 0:
                print("Thank you for using the Dice Rolling Simulator. Goodbye!")
                break

            dice_results = roll_dice(num_dice)
            display_results(dice_results)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()