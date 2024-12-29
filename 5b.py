import matplotlib.pyplot as plt
expense_cat=['Housing expense','Transport','Food','Entertainment','Utilities']
expense_amount=[1200,640,800,190,500]

colors=['gold','orange','yellow','red','purple']

explode=(0.1,0,0,0,0)

plt.figure(figsize=(8,8))
plt.pie(expense_amount,labels=expense_cat,colors=colors,autopct='%1.1f%%',explode=explode,startangle=140)

plt.title('Expense Distribution')
plt.axis('equal')
plt.tight_layout()
plt.show()