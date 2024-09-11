# Initializing a 2D array (list of lists)
traversing= [
    [1, 20, 30],
    [40, 5, 60],
    [65, 80, 99]
]
# Function to traversing and print the elements of a 2D array
def travers_2dim_array(array):
    print("Traversing the 2D array:")
    for q in range(len(array)): 
        for b in range(len(array[q])):  
            print(array[q][b], end=' ')
        print()  # New line after each row
# Call the function to traversing the 2D array

travers_2dim_array(traversing)