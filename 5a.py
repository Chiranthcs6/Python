import matplotlib.pyplot as plt

exam_scores=[65,78,69,86,75,45,31,25,49,50,11,25,34,39,97,100,82,45,67,86,36,72,88,33,36,71,84,56,71,17,80]

bins=[60,65,70,75,80,85,90,95,100]

plt.hist(exam_scores,bins=bins,color='purple',edgecolor='black')
plt.xlabel('Exam scores out of (100)')
plt.ylabel('Frequencey')
plt.title('Distribution of exam scores')
plt.grid(True)
plt.show()