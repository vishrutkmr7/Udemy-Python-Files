import matplotlib.pyplot as plt
import pandas as pd


data = [{
    'name': 'Hawkeye',
    'jan_ir': 124,
    'feb_ir': 100,
    'mar_ir': 165
    }, {
    'name': 'Natasha',
    'jan_ir': 112,
    'feb_ir': 143,
    'mar_ir': 3
    }]
# lines reduced
raw_data = {'names': ['Steve', 'Bruce', 'Tony', 'Thor', 'Natasha', 'Clint'],
            'jan_ir': [143, 122, 101, 106, 365, 223],
            'feb_ir': [221, 122, 220, 388, 366, 224],
            'mar_ir': [556, 122, 100, 385, 600, 225],
            }

df = pd.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'mar_ir'])
df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['mar_ir']
print(df)

color = [(1, .4, .4), (1, .6, .1), (.5, .3, 1), (.3, 1, .5), (.7, .7, .2), (1, .6, 1)]

plt.pie(df['total_ir'], labels=df['names'], colors=color, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
