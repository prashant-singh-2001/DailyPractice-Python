import re
from unittest.mock import seal
a=input("Enter number :")
r=re.sub(r'5','five',a)
tr=re.sub(r'5','five',a,count=1)
item=["prashant","khushi","gupchup","karan","dheeraj"]
z=[a for a in item if re.search(r'',a)]
print(r)
print(tr)
print(z)