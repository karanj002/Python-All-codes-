#bar chart

import matplotlib.pyplot as plt

lang=('DIGENE','ENO','GAS-O-FAST')
y_pos=[1,2,3]
performance=[15.4,13.3,15.7]
plt.bar(y_pos,performance,align='center',alpha=1,width=0.4,color='r')
plt.xticks(y_pos,lang)
plt.ylabel("Concordant value")
plt.show()
