import matplotlib.pyplot as plt 
print("Matplotlib imported succesfully")
months=['Jan','Feb','March','Apr','May']
books_read=[10,12,15,18,20]

plt.bar(months,books_read,color='skyblue')
plt.xlabel('Months')
plt.ylabel('Books read')
plt.title('Monthly Books reader')
plt.show()