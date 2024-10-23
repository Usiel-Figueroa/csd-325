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

def beer_song(count):
  while count > 0:
      if count > 1:
          print(f"{count} bottles of beer on the wall, {count} bottles of beer.")
          print(f"Take one down, pass it around, {count-1} bottles of beer on the wall.\n")
      else:
          print(f"{count} bottle of beer on the wall, {count} bottle of beer.")
          print(f"Take it down, pass it around, no more bottles of beer on the wall.\n")
      count -= 1

# Main program
def main():
  # Ask the user how many bottles of beer are on the wall
  while True:
      try:
          num_bottles = int(input("How many bottles of beer on the wall? "))
          if num_bottles > 0:
              break
          else:
              print("Please enter a number greater than 0.")
      except ValueError:
          print("Please enter a valid number.")

  # Call the beer song function
  beer_song(num_bottles)

  # Remind the user to buy more beer
  print("Go buy more beer!")

# Execute the main program
if __name__ == "__main__":
  main()
