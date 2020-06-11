#input array and to print no. of even and odd

from array import *
def count(lst):
    arr = array('i',[])
    for i in range (6):
        x = int(input("enter the values"))
        arr.append(x)
    print(arr)
    even=0
    odd=0
    for j in arr:
      if j%2 == 0:
        even+=1
      else:
        odd+=1
    return even,odd
lst = array('i',[])
even,odd = count(lst)
print("total no.of even numbers are-",even)
print("total no.of odd numbers are-",odd)
