def calculate_difference(n):
    sum_of_squares = sum([i**2 for i in range(1, n+1)])
    square_of_sum = sum(range(1, n+1))**2
    difference = square_of_sum - sum_of_squares
    return difference
print(calculate_difference(10))
