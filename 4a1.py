import matplotlib.pyplot as plt

months=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']
product_a_saled=[2000,2100,2200,2400,2500,2600,2700,2800,2900,3000,3100,3200]
product_b_saled=[2050,2150,2250,2450,2550,2650,2750,2850,2950,3050,3150,3250]

plt.bar(months,product_a_saled,label='Product A',color='orange')
plt.bar(months,product_b_saled,label='Product B',color='green',alpha=0.7)

plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly saled on both products')

plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()