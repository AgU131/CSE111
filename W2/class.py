"""
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

# Example 1
import math
# Define a function named print_cylinder_volume.
def print_cylinder_volume():
  """Compute and print the volume of a cylinder.
  Parameters: none
  Return: nothing
  """
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
  """Compute and print the volume of a cylinder.
  Parameters
  radius: the radius of the cylinder
  height: the height of the cylinder
  Return: nothing
  """
  # Compute the volume of the cylinder.
  volume = math.pi * radius**2 * height
  # Print the volume of the cylinder.
  print(volume)

print_cylinder_volume2(2.5, 4.1)

# Example 3
import math
# Define a function named computer_cylinder_volume.
def compute_cylinder_volume(radius, height):
  """Compute and return the volume of a cylinder.
  Parameters
  radius: the radius of the cylinder
  height: the height of the cylinder
  Return: the volume of the cylinder
  """
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








