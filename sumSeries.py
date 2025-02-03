import math
x = float(input("Enter the value of x in radians: "))
n = int(input("Enter the number of terms: "))
sum_sin = 0
print("Sin series equation: ", end="")

for i in range(n):
    exponent = 2 * i + 1
    term = ((-1) ** i) * (x ** exponent) /  math.factorial(exponent)
    sum_sin += term
    if i == 0:
        print(f"{x}^{exponent}/{exponent}!", end=" ")
    else:
        sign = "-" if i % 2 == 1 else "+"
        print(f"{sign} {x}^{exponent}/{exponent}!", end="")

print(f"\nSum of the sine series up to {n} terms: {sum_sin}")
