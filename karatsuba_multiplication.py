import time 

x = int(input("Enter First Number\n"))
y = int(input("Enter Second Number\n"))

def breakup(num, l):
    num_1 = int(num/10**(l/2))
    num_2 = int(num%10**(l/2))
    return num_1, num_2
    
def karatsuba_mul(x, y):
    n = len(str(x))
    if n==1:
        return x*y
    a, b = breakup(x, n)
    c, d = breakup(y, n)
    
    return (10**n) * karatsuba_mul(a, c) + (10**(n/2))*(karatsuba_mul(a,d) + karatsuba_mul(b,c)) + karatsuba_mul(b,d)
tic  = time.time()
print(f"Karatsuba Multiplication: {karatsuba_mul(x ,y)}")
print(f"The time taken is {time.time()-tic}")
tic = time.time()
print(f"Classical Multiplication: {x*y}")
print(f"The time taken is {time.time()-tic}")