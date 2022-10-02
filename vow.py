import re
from tkinter import Y
print("\n\n")
a=input("Enter the string ")
at=re.findall("[0-4,a-m]",a)
print(at)

print("\n\n")
a="There are 10 boys in MCA"
t=re.findall("\d",a)
print(t)

x="prashant singh"
y=re.findall("p..",x)
print(y)

