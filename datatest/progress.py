import fitz
import re
import sqlite3
doc = fitz.open('file_for_test.pdf')
page = doc[0]
extracted_blocks = page.get_text('blocks')

symbols_of_text = [] 

test_results = []

for block in extracted_blocks:
    x_n = re.split('\n', block[4])
    symbols_of_text.append(x_n)
    if 'Общий белок1' in x_n:
        test_results += [[x_n[1], x_n[2]]]
    elif 'Креатинин1' in x_n:
        test_results += [[x_n[1], x_n[2]]]
    elif 'Мочевина1' in x_n:
        test_results += [[x_n[1], x_n[2]]]

for item in test_results:
    print(item)