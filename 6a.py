import matplotlib.pyplot as plt
temp=[25,23,22,24,28,21,20]
days=[1,2,3,4,5,6,7]

plt.plot(days,temp,marker='o',linestyle='-',color='b',label='Daily high temperture')

plt.xlabel('Day of the week')
plt.ylabel('Daily High temperature(C)')
plt.title('Daily High temperature changes over a week')
plt.grid(True)
plt.legend()
plt.show()