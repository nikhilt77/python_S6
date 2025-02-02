def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
def nCr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))
n=input("Enter the value of n:")
r=input("Enter the value of r:")
print("nCr is:", nCr(int(n),int(r)))
