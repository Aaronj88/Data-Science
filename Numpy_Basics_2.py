import numpy as np

a = np.arange(0,11) #slicing on 1 dimensional array
print(a)

print(a[4:9])
print(a[:9])
print(a[5:])
print(a[3:9:2])
print(a[9:3:-2])


b = np.random.randint(0,100,(3,5)) #slicing a 2 dimensional array
print(b)

print(b[1:,1:3])


#conditional slicing
print(a[a%2==0])
print(b[b>50])


#selcted index
print(a[[1,3,4]])


#evaluating expressions
def calculate(x):
    y = 2*x + 5
    return y

z = np.arange(1,21)

print(calculate(z))



