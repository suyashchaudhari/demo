#prime
def prime(n):

    for i in range(2,n):
        if n %i==0:
            print("its not prime")
            break
    else:
        print("its prime")

x=prime(9)
print(x)
