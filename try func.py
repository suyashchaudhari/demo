#use of yield,try,exception,finally


def ten():
    n = 1
    while n<=10:
        sq=n*n
        yield sq
        n += 1
values=ten()
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
