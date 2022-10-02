a = []
b = int(input("Enter a number to find the factor of : "))
i = 1
while i <= b:
    if b % i == 0:
        a.append(i)
    i += 1
print(a)
