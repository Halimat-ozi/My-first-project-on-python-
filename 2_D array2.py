import array

# Declaring and initializing a 2D array using the array module
two_dimensional_array = [
    array.array('i', [1, 2, 3]),
    array.array('i', [4, 5, 6]),
    array.array('i', [7, 8, 9])
]
# Printing the 2D array
for row in two_dimensional_array:

  print(row.tolist())