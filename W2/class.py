"""
Part 1: Writing functions

To write a user-defined function in Python, simply type code that matches this template:

def function_name(param1, param2, …
  paramN):
#   """"""documentation string""""""
  statement1
  statement2
  ⋮
  statementN
  return value
"""

"""
# Example 1
import math
# Define a function named print_cylinder_volume.
def print_cylinder_volume():
  # Compute and print the volume of a cylinder.
  # Parameters: none
  # Return: nothing
  
  # Get the radius and height from the user.
  radius = float(input("Enter the radius of a cylinder: "))
  height = float(input("Enter the height of a cylinder: "))
  # Compute the volume of the cylinder.
  volume = math.pi * radius**2 * height
  # Print the volume of the cylinder.
  print(f"Volume: {volume:.2f}")

print_cylinder_volume()

# Example 2
import math
# Define a function named print_cylinder_volume.
def print_cylinder_volume2(radius, height):
  # Compute and print the volume of a cylinder.
  # Parameters
  # radius: the radius of the cylinder
  # height: the height of the cylinder
  # Return: nothing
  
  # Compute the volume of the cylinder.
  volume = math.pi * radius**2 * height
  # Print the volume of the cylinder.
  print(volume)

print_cylinder_volume2(2.5, 4.1)

# Example 3
import math
# Define a function named computer_cylinder_volume.
def compute_cylinder_volume(radius, height):
  # Compute and return the volume of a cylinder.
  # Parameters
  # radius: the radius of the cylinder
  # height: the height of the cylinder
  # Return: the volume of the cylinder
  # Compute the volume of the cylinder.

  volume = math.pi * radius**2 * height
  # Return the volume of the cylinder so that the
  # volume can be used somewhere else in the program.
  return volume

volume = compute_cylinder_volume(2.5, 4.1)
print(f"your volume is {volume}")

# Example 4
import math
# Get the radius and height from the user.
radius = float(input("Enter the radius of a cylinder: "))
height = float(input("Enter the height of a cylinder: "))
# Compute the volume of the cylinder.
volume = math.pi * radius**2 * height
# Print the volume of the cylinder.
print(f"Volume: {volume:.2f}")

# Example 5
import math
# Define a function named main.
def main():
  # Get the radius and height from the user.
  radius = float(input("Enter the radius of a cylinder: "))
  height = float(input("Enter the height of a cylinder: "))
  # Compute the volume of the cylinder.
  volume = math.pi * radius**2 * height
  # Print the volume of the cylinder.
  print(f"Volume: {volume:.2f}")
# Start this program by
# calling the main function.
main()


# Example 6
import math
# Define the main function.
def main():
  # Get a radius and a height from the user.
  radius = float(input("Enter the radius of a cylinder: "))
  height = float(input("Enter the height of a cylinder: "))
  # Call the compute_cylinder_volume function and store
  # its return value in a variable to use later.
  volume = compute_cylinder_volume(radius, height)
  # Print the volume of the cylinder.
  print(f"Volume: {volume:.2f}")
# Define a function that accepts two parameters.
def compute_cylinder_volume(radius, height):
  # Compute and print the volume of a cylinder.
  # Parameters
  # radius: the radius of the cylinder
  # height: the height of the cylinder
  # Return: the volume of the cylinder
  
  # Compute the volume of the cylinder.
  volume = math.pi * radius**2 * height
  # Return the volume of the cylinder so that the
  # volume can be used somewhere else in the program.
  # The returned result will be available wherever
  # this function was called.
  return volume
# Start this program by
# calling the main function.
main()

"""

"""
Part 2: Functions details


# g is a global variable because it
# is defined outside of all functions.
g = 25
def main():
  # x is a local variable because
  # it is defined inside a function.
  x = 1


  

in order for a function to modify the value of a global variable, the global variable must be declared as global inside the function


# Example 3
import math
def main():
  radius = float(input("Enter the radius of a circle: "))
  area = circle_area()
  print(f"area: {area:.1f}")
def circle_area():
  # Mistake! There is no variable named radius
  # defined inside this function, so the variable
  # radius cannot be used in this function.
  area = math.pi * radius * radius
  return area
main()

# Example 4
import math
def main():
  radius = float(input("Enter the radius of a circle: "))
  area = circle_area(radius)
  print(f"area: {area:.1f}")
def circle_area(radius):
  area = math.pi * radius * radius
  return area
main()



# Example 5
import math
def main():
  # Call the arc_length function with only one argument
  # even though the arc_length function has two parameters.
  len1 = arc_length(4.7)
  print(f"len1: {len1:.1f}")
  # Call the arc_length function again but
  # this time with two arguments.
  len2 = arc_length(4.7, 270)
  print(f"len2: {len2:.1f}")
# Define a function with two parameters. The
# second parameter has a default value of 360.
def arc_length(radius, degrees=360):
  # Compute and return the length of an arc of a circle
  circumference = 2 * math.pi * radius
  length = circumference * degrees / 360
  return length
main()







"""



