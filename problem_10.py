#Sum of prime till 2M

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5) +1):
        if num%i==0:
            return False

    return True


num = int(input("Enter the number: "))

total = 0

for i in range(2, num):
    if isPrime(i):
        total+=int(i)

print(f"The required answer is: {total}")

