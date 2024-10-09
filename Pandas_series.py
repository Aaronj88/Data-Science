import pandas as pd


a = [1,6,2,85,85,5,6,9,10,11,9,85,6]
b = pd.Series(a)
print(b)
print(type(b))


#statistical operations

#minimum
print(b.min())

#maximum
print(b.max())

#average
print(b.mean())

#middle number
print(b.median())

#most frequent value
print(b.mode())

#sort the values
print(b.sort_values())

print(b.sort_values(ascending=False))

#how many times each value occurs
c = b.value_counts()

print(c[6])


