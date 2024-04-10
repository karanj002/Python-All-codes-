#graph
import matplotlib.pyplot as plt

xaxis=[1,2,3,4]
yaxis=[]
for ele in xaxis:
    yaxis.append(ele*ele)

plt.plot(xaxis,yaxis)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph")
plt.show()
