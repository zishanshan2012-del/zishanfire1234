import matplotlib.pyplot as plt
day = ['Mon','Tue','Wed','Thurs','Fri']
scores = [70,85,60,90,75]
plt.plot(day,scores)
plt.show()
plt.plot(day,scores)
plt.title('My Quiz score tracker')
plt.xlabel('Day of week')
plt.ylabel('Scores')
plt.grid(True)
plt.ylim(0,100)
plt.show()
plt.bar(day,scores,color = 'orange')
plt.title('My Quiz score bar chart')
plt.xlabel('Days of week')
plt.ylabel('Score')
plt.ylim(0,100)
plt.show()