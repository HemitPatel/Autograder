def find_sum(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
    return sum

n = 7
print("The sum of the first", n, "even numbers is:", find_sum(n))
