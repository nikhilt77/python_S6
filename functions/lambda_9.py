def binary(n):
    if n == 0:
        return "0000"
    bin = ""
    while n > 0:
        bin = str(n % 2) + bin
        n = n // 2
    while len(bin) < 4:
        bin = "0" + bin
    return bin

def bcd(num):
    digits = str(num)
    result = ""
    for digit in digits:
        result += binary(int(digit)) + " "
    return result
number = int(input("Enter a number: "))
print(f"BCD of {number} is: {bcd(number)}")
