import numpy as np


nums = [1,2,3,4,5,88]
print(type(nums))

np_nums = np.array(nums)
print(type(np_nums))

for i in range(len(nums)):
    nums[i] = nums[i]*2

print(nums)

print(np_nums * 2)

#array of 0's
zero_list = np.zeros(5,int) #by default float
print(zero_list)

x = np.zeros((3,5)) #2 dimensional, 3 row 5 columns
print(x)

#array of 1's
y = np.ones(5)
print(y)


#find dimension of array
print(x.ndim)
print(y.ndim)

#find shape (how maany values) of an array
print(x.shape)
print(y.shape)

#find size (how many values)
print(x.size)
print(y.size)


#array with numbers in a range
z = np.arange(1,12,3)
print(z)

#change arrangment of values in array
print(np.random.permutation(z))
print(np.random.permutation(z))
print(np.random.permutation(z))

#array of random numbers
print(np.random.randint(1,100,10))
c = np.random.randint(1,100,(5,3))
print(c) #more dimensions, still random


#reshaping array
j = z.reshape((2,2))
print(j)


#sorting an array
a = np.random.randint(1,100,10)
b = np.sort(a)
print(b)


#array splicing (extracting a part, a slice of an array) 
print(a)
print(a[3:6])
print(a[3:])
print(a[:7])

print(c[1:4,1:]) #splicing a multi dimensional array



e = np.random.randint(100,500,5)
f = np.arange(1,6)

print(e)
print(f)
print(e+f)
