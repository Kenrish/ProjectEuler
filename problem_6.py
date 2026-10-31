#a = 1^2 + ... + 10^2
#b = (1 + ... + 10)^2
#soln = diff(a,b)
#first hundred terms?

a = 0
for i in range(1,101):
    a += pow(i, 2)

b = 0
for i in range(1,101):
    b += i
c = pow(b,2)

Diff = abs(a-c)
print(f"Difference between sum of square and square of sum of first 100 terms is: {Diff}")
print(a,c)
