#A palindrome reads same both ways. The largest palindrome made by product of two 2 digit number is 9009=90X91.
#Find the largest palindrome made by product of two 3-digit number.

def palin(num):
    n_num = 0
    _num_ = num
    while _num_ > 0:
        n_num = n_num*10 + _num_%10
        _num_ //= 10
    return n_num

largest = 0

for x in range(999, 99, -1):
    for y in range(x, 99, -1):
        num = x * y
        if num <= largest:
            break
        if palin(num) == num:
            largest = num


print(f"The largest palindromic number is: {largest}")
