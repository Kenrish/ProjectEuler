#a+b+c = 1000, a^2+b^2=c^2
#find a*b*c


def pytho(num):
    for i in range(1,num):
        for j in range(1, num-i):
            k = num - i - j
            if i**2+j**2 == k**2:
                return i,j,k


def prod(a,b,c):
    return a*b*c

def main():
    num = int(input("Enter the required number: "))
    a,b,c = pytho(num)
    P = prod(a,b,c)
    print(a)
    print(b)
    print(c)
    print(f"The required answer is: {P}")


if __name__ == "__main__":
    main()
