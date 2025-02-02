def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

def pow(x, n):
    if n == 0:
        return 1
    else:
        return x * pow(x, n-1)

def cos_series(x, n):
    sum = 0
    for i in range(n):
        term = pow(-1, i) * pow(x, 2*i) / fact(2*i)
        sum += term
    return sum


x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))
result = cos_series(x, n)
print(f"Sum of cosine series for x={x} with {n} terms is: {result}")
