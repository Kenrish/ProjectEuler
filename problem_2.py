#Each new term in the Fibbonacci sequence is geerate by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1,2,3,5,8,13, ...
#By considering the two terms in the fibbonacci whoose values do not exceed four milllion, find the sum of te even-valued terms.


def main():
    def fibo(n):
        t1 = 0
        t2 = 1
        for i in range(n):
            t1, t2 =t2, t1 + t2
            fib.append(t2)
        return fib
    fib = []
    print('Enter 23 for your desired output.')
    fibo_print = fibo(int(input('Enter a number: ')))
    Sum = sum(fib)
    print(Sum)
    #print(*fib)

if __name__ == '__main__':
    main()
