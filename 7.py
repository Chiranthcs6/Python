import seaborn as sns
import matplotlib.pyplot as plt

ages=[25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]

sns.set(style="whitegrid",palette='pastel')
plt.figure(figsize=(8,5))
sns.histplot(ages,bins=5,kde=True,color='skyblue',alpha=0.7)

plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Distribution of Ages")

plt.show()