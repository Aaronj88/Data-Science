import matplotlib.pyplot as plt
import numpy as np

#line plot
x = np.arange(1,10,2)
y = 2*x+3
plt.figure(figsize=(6,4))
plt.plot(x,y,"m--^",linewidth = 1,label = "y = 2x+3")
#plt.axis([1,20,1,50])
plt.xticks(ticks=x,labels=["hwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwi","hellwwwwwwwwwwwwwwwwwwwwwwwo","hewwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwy","a str","last value"],rotation=32)

plt.title("graph1")
plt.xlabel("random values")
plt.ylabel("more random values")
plt.legend()


#plt.show()


#multiple graphs in plot
x = np.arange(1,10,0.1)


plt.figure(figsize=(6,4))

plt.plot(x,x**2,label = "x^2")

plt.plot(x,x**3,label = "x^3")


plt.legend()
plt.show()




