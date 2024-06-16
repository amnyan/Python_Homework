def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()
        
def create_square_matrix(size):
    matrix = []
    print(f"Enter {size}x{size} matrix elements:")

    for i in range(size):
        row = []
        for j in range(size):
            element = int(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    
    return matrix

size = int(input("Enter the size of the square matrix: "))
matrix = create_square_matrix(size)
print("\nMatrix elements:")
print_matrix(matrix)