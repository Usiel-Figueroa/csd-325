
# Usiel Figueroa
# November 6, 2024 
# Module 4.2 Assignment: High/Low Temperatures
# SD325 Advanced Python


# Purpose: Make the following changes to the sitka_highs.py program.
# Open the program with instructions on how to use the menu; Highs, Lows, or Exit.


# Sources
# (n.d.). Python If. Else. W3schools. Retrieved October 15, 2024, from https://www.w3schools.com/python/python_conditions.asp
# Replit
# ChatGPT




import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# Load data from CSV file
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, highs, and lows from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        lows.append(int(row[6]))  # Assuming row[6] contains low temperatures
        highs.append(high)

def plot_temperatures(dates, temperatures, title, color):
    """Plots temperatures with specified title and color."""
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)

    # Format plot
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def main():
    """Menu-driven program for displaying high and low temperatures."""
    while True:
        print("\nSelect an option:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            plot_temperatures(dates, highs, "Daily High Temperatures - 2018", 'red')
        elif choice == '2':
            plot_temperatures(dates, lows, "Daily Low Temperatures - 2018", 'blue')
        elif choice == '3':
            print("Thank you for using the weather program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


