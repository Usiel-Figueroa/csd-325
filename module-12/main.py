#Usiel Figueroa 
#October 21, 2024 
#Module 1.3 Assignment: On the Wall + Flowchart 
#CSD325 Advanced Python 
# Source:(n.d.). 99 bottles of beer. Rosetta Code. Retrieved October 21, 2024, from https://rosettacode.org/wiki/99_bottles_of_beer
#Source: Replit. (n.d.). Replit. Retrieved October 21, 2024, from https://replit

""""The program first asks the user to input the number of bottles.
The input is validated to ensure it's a positive integer.
Once the number is valid, the beer_song() function is called to start the countdown.
The program prints the lyrics of the song as it counts down from the input number to 1.
When it reaches 1, the output changes to "1 bottle of beer" as required.
Finally, it prints "Go buy more beer!" once the countdown is complete."""

def get_valid_input():
    """
    Prompt the user for a valid positive integer input.

    Returns:
        int: A positive integer representing the number of bottles to start with.
    """
    while True:
        try:
            bottles = int(input("Enter the number of bottles to start with: "))
            if bottles <= 0:
                print("Please enter a positive integer.")
            else:
                return bottles
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def generate_lyrics(bottles):
    """
    Generate the lyrics for the '99 Bottles of Beer' song.

    Args:
        bottles (int): The number of bottles to start with.
    """
    for i in range(bottles, 0, -1):
        if i > 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.\n")
        elif i == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.")
            print("Take one down and pass it around, 1 bottle of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down and pass it around, no more bottles of beer on the wall.\n")
    """
    Prompt the user for input and validate it.
    Returns a positive integer.
    """
    while True:
        try:
            num_bottles = int(input("Enter the number of bottles to start with: "))
            if num_bottles <= 0:
                print("Please enter a positive integer.")
            else:
                return num_bottles
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def generate_lyrics(num_bottles):
    """
    Generate and print the '99 Bottles of Beer' song lyrics.
    """
    for i in range(num_bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i-1} {'bottle' if i-1 == 1 else 'bottles'} of beer on the wall.\n")
        elif i == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down and pass it around, no more bottles of beer on the wall.\n")

    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go buy more beer!")
    """
    Prompts the user for a positive integer input and validates it.
    Returns the valid input as an integer.
    """
    while True:
        try:
            bottles = int(input("Enter the number of bottles to start with: "))
            if bottles <= 0:
                print("Please enter a positive integer.")
            else:
                return bottles
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def generate_lyrics(bottles):
    """
    Generates and prints the '99 Bottles of Beer' song lyrics.

    Args:
    bottles (int): The number of bottles to start with.
    """
    while bottles > 0:
        # Print the current verse
        print(f"\n{bottles} bottle{'s' if bottles > 1 else ''} of beer on the wall,")
        print(f"{bottles} bottle{'s' if bottles > 1 else ''} of beer.")
        print("Take one down, pass it around,")

        # Decrease the number of bottles
        bottles -= 1

        # Print the next line, which depends on the number of remaining bottles
        if bottles > 0:
            print(f"{bottles} bottle{'s' if bottles > 1 else ''} of beer on the wall.")
        else:
            print("No more bottles of beer on the wall.")

    # Print the final message
    print("\nGo buy more beer!")

def main():
    """
    Main function to run the '99 Bottles of Beer' song generator.
    """
    print("Welcome to the '99 Bottles of Beer' Song Generator!")
    bottles = get_valid_input()
    generate_lyrics(bottles)

if __name__ == "__main__":
    main()

