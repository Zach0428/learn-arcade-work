import random
import arcade

# Printing Section
# for i in range(10):
#     x = random.randrange(120)
#     print(f"My number: {x:3}")

# my_fruit = ("Apples", "Oranges", "Grapes", "Pears")
# my_calories = [4, 300, 70, 30]
#
# for i in range(4):
#     print(my_fruit[i], "are", my_calories[i], "calories")
#     print(f"{my_fruit[i]:>7} are {my_calories[i]:<3} calories.")

# for hours in range(1,13):
#     for minutes in range(0,60):
#         print(f"Time {hours}:{minutes:02}")

# x = 0.1
# y = 123.456789
#
# print(f"{x:.1}  {y:.1}")
# print(f"{x:.2}  {y:.2}")
# print(f"{x:.3}  {y:.3}")
# print(f"{x:.4}  {y:.4}")
# print(f"{x:.5}  {y:.5}")
# print(f"{x:.6}  {y:.6}")
#
# print()
# print(f"{x:.1f}  {y:.1f}")
# print(f"{x:.2f}  {y:.2f}")
# print(f"{x:.3f}  {y:.3f}")
# print(f"{x:.4f}  {y:.4f}")
# print(f"{x:.5f}  {y:.5f}")
# print(f"{x:.6f}  {y:.6f}")

# x = 0.1
# y = 123.456789
#
# print(f"My number: '{x:10.1}' and '{y:10.1}'")
# print(f"My number: '{x:10.2}' and '{y:10.2}'")
# print(f"My number: '{x:10.3}' and '{y:10.3}'")
# print(f"My number: '{x:10.4}' and '{y:10.4}'")
# print(f"My number: '{x:10.5}' and '{y:10.5}'")
# print(f"My number: '{x:10.6}' and '{y:10.6}'")
#
# print()
# print(f"My number: '{x:10.1f}' and '{y:10.1f}'")
# print(f"My number: '{x:10.2f}' and '{y:10.2f}'")
# print(f"My number: '{x:10.3f}' and '{y:10.3f}'")
# print(f"My number: '{x:10.4f}' and '{y:10.4f}'")
# print(f"My number: '{x:10.5f}' and '{y:10.5f}'")
# print(f"My number: '{x:10.6f}' and '{y:10.6f}'")

# cost1 = 3.07
# tax1 = round(cost1 * 0.06, 2)
# total1 = cost1 + tax1
#
# print(f"Cost:  ${cost1:5.2f}")
# print(f"Tax:    {tax1:5.2f}")
# print(f"-------------")
# print(f"Total: ${total1:5.2f}")
#
# cost2 = 5.07
# tax2 = round(cost2 * 0.06, 2)
# total2 = cost2 + tax2
#
# print()
# print(f"Cost:  ${cost2:5.2f}")
# print(f"Tax:    {tax2:5.2f}")
# print(f"-------------")
# print(f"Total: ${total2:5.2f}")
#
# print()
# grand_total = total1 + total2
# print(f"Grand total: ${grand_total:5.2f}")

# def on_draw(self):
#     """ Use this function to draw everything to the screen. """
#
#     # Start the render. This must happen before any drawing
#     # commands. We do NOT need an stop render command.
#     arcade.start_render()
#
#     # Calculate minutes
#     minutes = int(self.total_time) // 60
#
#     # Calculate seconds by using a modulus (remainder)
#     seconds = int(self.total_time) % 60
#
#     # Figure out our output
#     output = f"Time: {minutes:02d}:{seconds:02d}"
#
#     # Output the timer text.
#     arcade.draw_text(output, 300, 300, arcade.color.BLACK, 30)
#
# def update(self, delta_time):
#     """
#     All the logic to move, and the game logic goes here.
#     """
#     self.total_time += delta_time

# Exceptions Section

# Divide by zero
# try:
#     x = 5 / 0
# except:
#     print("Error dividing by zero")

# Invalid number conversion
# try:
#     x = int("fred")
# except:
#     print("Error converting fred to a number")

# number_entered = False
# while not number_entered:
#     number_string = input("Enter an integer: ")
#     try:
#         n = int(number_string)
#         number_entered = True
#     except:
#         print("Error, invalid integer")

# Error opening file
# try:
#     my_file = open("myfile.txt")
# except:
#     print("Error opening file")

# Multiple errors
# try:
#     # Open the file
#     filename = "myfile.txt"
#     my_file = open(filename)
#
#     # Read from the file and strip any trailing line feeds
#     my_line = my_file.readline()
#     my_line = my_line.strip()
#
#     # Convert to a number
#     my_int = int(my_line)
#
#     # Do a calculation
#     my_calculated_value = 101 / my_int
#
# except FileNotFoundError:
#     print(f"Could not find the file '{filename}'.")
# except IOError:
#     print(f"Input/Output error when accessing the file '{filename}'.")
# except ValueError:
#     print("Could not convert data to an integer.")
# except ZeroDivisionError:
#     print("Division by zero error.")
# except:
#     print("Unexpected error.")

"""
Show how to use exceptions to save a high score for a game.

Sample Python/Pygame Programs
Simpson College Computer Science
http://simpson.edu/computer-science/
"""


def get_high_score():
    # Default high score
    high_score = 0

    # Try to read the high score from a file
#     try:
#         high_score_file = open("high_score.txt", "r")
#         high_score = int(high_score_file.read())
#         high_score_file.close()
#         print("The high score is", high_score)
#     except IOError:
#         # Error reading file, no high score
#         print("There is no high score yet.")
#     except ValueError:
#         # There's a file there, but we don't understand the number.
#         print("I'm confused. Starting with no high score.")
#
#     return high_score
#
#
# def save_high_score(new_high_score):
#     try:
#         # Write the file to disk
#         high_score_file = open("high_score.txt", "w")
#         high_score_file.write(str(new_high_score))
#         high_score_file.close()
#     except IOError:
#         # Hm, can't write it.
#         print("Unable to save the high score.")
#
#
# def main():
#     """ Main program is here. """
#     # Get the high score
#     high_score = get_high_score()
#
#     # Get the score from the current game
#     current_score = 0
#     try:
#         # Ask the user for his/her score
#         current_score = int(input("What is your score? "))
#     except ValueError:
#         # Error, can't turn what they typed into a number
#         print("I don't understand what you typed.")
#
#     # See if we have a new high score
#     if current_score > high_score:
#         # We do! Save to disk
#         print("Yea! New high score!")
#         save_high_score(current_score)
#     else:
#         print("Better luck next time.")
#
# # Call the main function, start up the game
# if __name__ == "__main__":
#     main()

