#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
#Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    def is_multiple(num):
        div = list()
        for i in range(2, num):
            if i%3==0 or i%5==0:
                div.append(i)
        return div
    
    num = int(input('Enter the last number to check: '))
    is_multiples = is_multiple(num)
    print(f"The answer is: {sum(is_multiples)}")


if __name__ == "__main__":
    main()
