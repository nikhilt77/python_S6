odds = [x for x in range(1,50,2)]
print("List of odd numbers:", odds)

cubes = list(map(lambda x:x**3, odds))
print("Cubes of numbers:", cubes)

divBy = list(filter(lambda x:x%3==0, odds))
print("Numbers divisible by 3:", divBy)
