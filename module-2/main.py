# Usiel Figueroa
# October 22, 2024 
# Module 2.2 Assignment: Documenting Debugging 
#CSD325 Advanced Python 
# Fiber Optic Cable Cost Calculator

# Purpose: Calculated the total cost of fiber cable installation evaluate a bulk discount.
# Documented Debugging


# Sources
#(n.d.). Python If. Else. W3schools. Retrieved August 15, 2024, from https://www.w3schools.com/python/python_conditions.asp
# GADDIS, T. (n.d.). Starting Out With Python. Retrieved from https://platform.virdocs.com/read/2608221/169/#/4/2


def main():
  # Display a welcome message
  print("Welcome to Usiel's Fiber Optic Cable Installation Cost Calculator")

  # Get the number of feet of fiber optic cable to be installed from the user
  try:
      num_feet = float(input("Please enter the number of feet of fiber optic cable to be installed: "))

      # Check for a valid number of feet
      if num_feet < 0:
          print("The number of feet cannot be negative. Please enter a positive number.")
          return

      # Determine the price per foot based on the number of feet requested
      if num_feet > 500:
          cost_per_foot = 0.50
      elif num_feet > 250:
          cost_per_foot = 0.70
      elif num_feet > 100:
          cost_per_foot = 0.80
      else:
          cost_per_foot = 0.87

      # Calculate the total cost
      total_cost = num_feet * cost_per_foot

      # Display the calculated information and company name
      print("\nCompany Name: Usiel's Fiber Optics Co.")
      print(f"Number of Feet to be Installed: {num_feet} feet")
      print(f"Cost per Foot: ${cost_per_foot:.2f}")
      print(f"Total Installation Cost: ${total_cost:.2f}")

  except ValueError:
      print("Invalid input. Please enter a numeric value for the number of feet.")

# Run the main function
if __name__ == "__main__":
  main()