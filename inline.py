a=[print(k) for k in range(int(input("Enter the number"))) if k%2!=0] #For odds
a=[print(k*k) for k in range(int(input("Enter the number"))+1) if k!=0] #For Squares
b=[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16]
print(b[::-1])
c=[print((x,y,z)) for x in range (1,30) for y in range (x,30) for z in range (y,30) if x**2 + y**2 =10= z**2 ]