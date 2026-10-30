#A palindrome reads same both ways. The largest palindrome made by product of two 2 digit number is 9009=90X91.
#Find the largest palindrome made by product of two 3-digit number.

x= 999
y = 999
a = True
while a == True:
    if str(x*y) == str(x*y)[::-1]:
        print(f"{x} X {y} = {x*y}")
        break
    y -= 1

