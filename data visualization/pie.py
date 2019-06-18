import matplotlib.pyplot as plt


labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl'
sizes = [33, 52, 12, 17, 62, 48]
separated = (0.3, 0.1, 0.1, 0.1, 0.1, 0.1)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=separated)
plt.axis('equal')
plt.show()
