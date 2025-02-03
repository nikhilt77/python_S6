def isArmstrong(num):
    digits = str(num)
    n = len(digits)
    sum = 0
    for digit in digits:
        sum += int(digit) ** n
    return sum == num

num=int(input("Enter a number : "))
if isArmstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
