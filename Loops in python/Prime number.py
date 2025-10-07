n = int(input("Enter the maximum number to stop: "))
for i in range(2, n):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, "is a prime number")
    