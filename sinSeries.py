n = int(input("Enter the number of terms: "))
print("Series:", end=" ")
print(f"x^1/1!", end=" ")
i = 1
while i < n:
    exp = 2 * i + 1
    if i % 2 == 1:
        print(f"- x^{exp}/{exp}!", end=" ")
    else:
        print(f"+ x^{exp}/{exp}!", end=" ")
    i += 1
