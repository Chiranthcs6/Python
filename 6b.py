import matplotlib.pyplot as plt

months=['Jan','Feb','Mar','April','May','Jun','July','Aug','Sept','Oct','Nov','Dec']
salary=[5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,10500]
plt.plot(months,salary,linestyle='-',color='b',marker='o',markersize=8)
plt.xlabel('Months')
plt.ylabel('Salary (in dollars)')
plt.title('Salary Hike')
plt.grid(True)
plt.legend()
plt.show()