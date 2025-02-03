words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
num = input("Enter a number: ")
output = " ".join(words[int(digit)] for digit in num)
print(output)
