import matplotlib.pyplot as plt
import numpy as np

'''#line plot
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
'''





'''#bar chart
x = [1,3,5,7,9]
y = [21,33,11,44,75]
plt.bar(x,y)
plt.show()


#showing more than one bar
plt.bar(np.arange(1,10,2),[1,33,4,75,15],color = "g")
plt.bar(np.arange(0,10,2),[54,13,43,42,2],color = "b")

plt.show()


#showing categorical value for x
plt.bar(["John","Mark"],[99,65])
plt.show()



#histograms
ages = np.random.randint(1,80,50)
bins = np.arange(0,81,10)

plt.figure(facecolor="r")
plt.hist(ages,bins,rwidth=0.8) #relative width
plt.show()


#scatter graph
x = np.arange(1,10)
y = np.random.randint(1,70,9)

plt.scatter(x,y,color="g",marker="x",s=100)
plt.show()


#pie chart
slices = [12,33,34,22,100]
labels = ["Maths","Chemistry","English","Physics","Sports"]

plt.pie(slices,labels=labels,autopct='%1.1f%%',colors=["r","r","r","r","r"],wedgeprops={'edgecolor':"g"},shadow=True,startangle=90)
plt.show()


#stack plot
x = ["Mon","Tue","Wed","Thu","Fri"]
languages = [1,0,7,2,1]
sciences = [3,0,5,3,1]
sports = [1,0,2,0,0]
maths = [3,3,1,4,1]
other = [1,0,0,2,1]

plt.stackplot(x,languages,sciences,sports,maths,other,labels=["Language","Science","Sport","Math","Other"])
plt.legend()
plt.show()
'''


#subplots
plt.subplot(2,3,3)
plt.plot([5,4,3,6,3],[33,4,66,33,55])
plt.subplot(2,3,2)
plt.plot([5,4,3,6,3],[33,4,66,33,55])
plt.subplot(2,3,5)
plt.plot([5,4,3,6,3],[33,4,66,33,55])
plt.show()
