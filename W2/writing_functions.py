def main():
    start = float(input("Enter the start point in milles: "))
    end = float(input("Enter the end point in milles: "))
    gallons = float(input("Enter the gallons used on the trip: "))
    # Compute the miles per gallon.
    total_miles = miles_per_gallon(start, end, gallons)
    # Compute the liters per 100 kilometers.
    lp100k = lp100k_from_mpg(total_miles)
    # Print all the obtained info
    print(f"Your miles per gallon is {total_miles:.2f}")
    print(f"Your lp100k is {lp100k:.2f}")


def miles_per_gallon(start, end, gallons):
    # Compute and return the miles per gallon.
    # Parameters
    # start: the starting odometer reading
    # end: the ending odometer reading
    # gallons: the number of gallons used
    # Return: the miles per gallon
    # Compute the miles per gallon.
    miles = end - start
    mpg = miles / gallons
    # Return the miles per gallon so that the
    # miles per gallon can be used somewhere else in the program.
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215/mpg

    return lp100k

main()

