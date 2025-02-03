def sqrtNewton(N, tolerance=1e-7, max_iterations=1000):
    x = N
    iteration = 0
    while iteration < max_iterations:
        x_new = 0.5 * (x + N / x)
        if abs(x_new - x) < tolerance:
            break
        x = x_new
        iteration += 1
    return x

N = int(input("Enter a value: "))
result = sqrtNewton(N)
print(f"The square root of {N} is approximately {result}")
