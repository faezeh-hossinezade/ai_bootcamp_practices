import numpy as np

def shoelace(x_y: np.array):
    """
    Calculates the area of a polygon using the shoelace formula.

    Args:
        x_y: A NumPy array of shape (n, 2) containing the x and y coordinates of the polygon's vertices.

    Returns:
        The area of the polygon.
    """

    # Reshape the input array to a 2D array with two columns
    x_y = x_y.reshape(-1, 2)

    # Extract x and y coordinates from the array
    x = x_y[:, 0]
    y = x_y[:, 1]

    # Calculate the sum of x_i * y_(i+1)
    S1 = np.sum(x * np.roll(y, -1))

    # Calculate the sum of y_i * x_(i+1)
    S2 = np.sum(y * np.roll(x, -1))

    # Calculate the area using the shoelace formula
    area = 0.5 * np.absolute(S1 - S2)

    return area

# Get the number of vertices from the user
n = int(input())

# Create an empty list to store the coordinates
list_ar = []

# Read the coordinates from the user
for j in range(n):
    list_ar.append([int(i) for i in input().split()])

# Convert the list of coordinates to a NumPy array
numpyArr = np.array(list_ar)

# Calculate and print the area of the polygon
print(shoelace(numpyArr))