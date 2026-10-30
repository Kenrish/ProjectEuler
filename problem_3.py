#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

def main():
    def prime(num):
        Div = list()
        Prime = list()
        for i in range(2,num//2+1):
            if num%i==0:
                Div.append(i)
        for i in Div:
            is_prime = True
            for j in Prime:
                if i%j==0:
                    is_prime=False 
                    break
            if is_prime:
                Prime.append(i)
        return Prime
    num = int(input('Give a number: '))
    _prime_ = prime(num)
    print(_prime_)
if __name__ == "__main__":
    main()
