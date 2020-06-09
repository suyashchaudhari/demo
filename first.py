print("hello")
from numpy import *


#to print top ten numbers
class topten:
    def __int__(self):
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=9:
          val = self.num
          self.num += 1
          return val
        else:
            raise StopIteration
values=topten()
values.__int__()
values.__next__()
for i in values:
    print(i)

#square function using yield 
def ten():
    n = 1
    while n<=10:
        sq=n*n
        yield sq
        n += 1
values=ten()


#execution using try 
for i in values:
    print(i)
a=int(input("enter a 1st number"))
b=int(input("enter a 2nd number"))
try:
    c = a/b
    print(c)
except Exception:
    print("something went wrong")
finally:
    print("bye")


#sorting program
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp


nums = [5, 3, 6, 8, 2, 9]
x= sort(nums)
print(x)


#linear sorting
def sort1(num):
    for i in range(num):
        minpos = 1
        for j in range(1,num+1):
            if num[j]<num[minpos]:
                minpos=j
        temp = num[i]
        num[i]=num[minpos]
        num[minpos]=temp
num=[5,2,4,23,7,2]
sort(num)
print(num)

#numpy 
x = array([
            [5,25,8],
            [14,45,85]
          ])
print(x)
z=x.T
print(z)
y = arange(1,20,2)
print(y)
