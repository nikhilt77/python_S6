def sumOfDigitsOfNumber(n):
    if n<10:
        return n
    else:
        return n%10+sumOfDigitsOfNumber(n//10)
n=int(input("Enter the number:"))
print("Sum of digits of the number is:",sumOfDigitsOfNumber(n))
