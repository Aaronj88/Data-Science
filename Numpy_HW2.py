import numpy as np


def l_equation(x):
    print("ax + b")
    print(' ')
    a = int(input('Enter your value for a: '))
    b = int(input('Enter your value for b: '))

    ans = a*x + b
    print(str(a)+'x'+' + '+str(b)+' for x = 0 to 10 is:')
    return (ans)

def q_equation(x):
    print("ax^2 + bx + c")
    print(' ')
    a = int(input('Enter your value for a: '))
    b = int(input('Enter your value for b: '))
    c = int(input('Enter your value for c: '))
    print(' ')

    ans = a*x^2+b*x+c
    print(str(a)+'x^2 + '+str(b)+'x + '+str(c)+' for x = 0 to 10 is:')
    return ans


y = np.arange(1,10)

print('1. Linear Equation')
print('2. Quadratic Equation')

a = int(input('Which kind of expression would you like to evaluate?'))

if a == 1:
    print(l_equation(y))
elif a == 2:
    print(q_equation(y))

else:
    print('Please enter either 1 or 2')




