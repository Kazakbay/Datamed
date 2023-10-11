import fitz
import re
import sqlite3
doc = fitz.open('file_for_test2.pdf')
page = doc[0]
extracted_text = page.get_text('blocks')

symbols_of_text = []

test_results = []

for block in extracted_text:
    x_n = re.split('\n', block[4])
    symbols_of_text.append(x_n)
    if 'Общий белок1' in x_n:
        test_results += [x_n[1], x_n[2]]
    elif 'Креатинин1' in x_n:
        test_results += [x_n[1], x_n[2]]
    elif 'Мочевина1' in x_n:
        test_results += [x_n[1], x_n[2]]



for line in symbols_of_text:
    print('\n')
    print(line)

print(test_results)
