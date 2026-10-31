#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

def prime(num):
    Prime = list()
    f = 2
    while f*f < num+1:
        if num%f==0:
            if f not in Prime:
                Prime.append(f)
            num //= f
        else:
            f += 1
    if num>1 and num not in Prime:
        Prime.append(num)
    return Prime
 
def main():
    num = int(input('Give a number: '))
    _prime_ = prime(num)
    print(max(_prime_))

if __name__ == "__main__":
    main()


