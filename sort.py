L = [(54, 'Nikhil Tomy'), (55, 'Nived RS'), (48, 'Karthik')]

L.sort(key=lambda item: item[0])
print("Sorted by roll number:")
for rno, name in L:
    print(f"Roll No: {rno}, Name: {name}")

print("-" * 20)

L.sort(key=lambda item: item[1])
print("Sorted by name:")
for rno, name in L:
    print(f"Roll No: {rno}, Name: {name}")
