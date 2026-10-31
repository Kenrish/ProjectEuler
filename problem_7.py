#By listig first 6 prime numbers, we can see that 6th prime number is 13.
#What is 10001th prime number

def prime(num):
    List = list()
    count = num
    i = 2
    while count > 0:
        if isprime(i)==True:
            List.append(i)
            count -= 1
        i += 1
    return List

def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5 + 1)):
        if num %i == 0:
            return False
    return True

def main():
    num = int(input("Enter the desired number: "))
    ans = prime(num)
    print(f"The answer to given question is: {ans[-1]}")

if __name__ == "__main__":
    main()
