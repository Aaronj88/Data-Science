import numpy as np
import matplotlib.pyplot as plt


def l_equation(x):
    print("ax + b")
    print(' ')
    
    global a,b
    a = int(input('Enter your value for a: '))
    b = int(input('Enter your value for b: '))

    ans_l = a*x + b
    print(str(a)+'x'+' + '+str(b)+' for x = 0 to 10 is:')
    return ans_l

def q_equation(x):
    print("ax^2 + bx + c")
    print(' ')

    global a,b,c
    a = int(input('Enter your value for a: '))
    b = int(input('Enter your value for b: '))
    c = int(input('Enter your value for c: '))
    print(' ')

    ans_q = a*x**2+b*x+c
    print(str(a)+'x^2 + '+str(b)+'x + '+str(c)+' for x = 0 to 10 is:')
    return ans_q


y = np.arange(1,10)
z = np.arange(1,50)

print('1. Linear Equation')
print('2. Quadratic Equation')

a = int(input('Which kind of expression would you like to evaluate?'))

if a == 1:
    print(l_equation(y))
    ans_l = a*z + b
    plt.plot(z,ans_l)
    plt.xlabel("1-50")
    plt.ylabel("Equation answer for x = 1-50")
    plt.show()
elif a == 2:
    print(q_equation(y))
    ans_q = a*z**2 + b*z+c
    plt.plot(z,ans_q)
    plt.xlabel("1-50")
    plt.ylabel("Equation answer for x = 1-50")
    plt.show()
else:
    print('Please enter either 1 or 2')




