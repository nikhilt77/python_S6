def prime(n):
   if n < 2:
       return False
   for i in range(2,n):
    if n%i == 0:
            return False
   return True
primeNumbers=[num for num in range(1,100) if prime(num)]
print(primeNumbers)
