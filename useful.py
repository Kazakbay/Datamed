mylist = [('Общий белок', '73.5', '2023.09.03'),
('Общий белок', '73.4', '2023.09.19'),
('Общий белок', '69.0', '2023.06.27'),
('Общий белок', '70.0', '2023.01.25'),
('Общий белок', '70.0', '2023.01.25')]

for i in mylist:
    print(i)
print(len(mylist))

mylist = list(dict.fromkeys(mylist))

print('\n\n')

print(len(mylist))
for i in mylist:
    print(i)

import sqlite3 


conn = sqlite3.connect('laboratory_data.db')
c = conn.cursor()

c.execute("""SELECT * FROM storage_of_results WHERE test_name = 'Креатинин' """)
data = c.fetchall()
for i in data:
    print(i)

# importing datetime
from datetime import datetime

# input list of date strings
inputDateList = ['06.2014', '08.2020', '4.2003', '04.2005', '10.2002', '7.2020']

# sorting the input list by formatting each date using the strptime() function
inputDateList.sort(key=lambda date: datetime.strptime(date, "%m.%Y"))

# Printing the input list after sorting
print("The input list of date strings after sorting:\n", inputDateList)

example = [('Общий белок', '73.5', '2023.09.03'),
('Общий белок', '73.4', '2023.09.19'),
('Общий белок', '69.0', '2023.06.27'),
('Общий белок', '70.0', '2023.01.25'),
('Общий белок', '70.0', '2023.01.25')]

data.sort(key = lambda x: datetime.strptime(x[2], "%Y.%m.%d")) 

for item in data:
    print(item)
