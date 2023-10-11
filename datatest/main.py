import fitz
import re
doc = fitz.open("file_for_test.pdf")
page = doc[0]
extracted_text = page.get_text('blocks')
print(extracted_text)
for line in extracted_text:
    print(line[4])
    x = re.findall("Мочевина1",line[4])
    

    x_n = re.split('\n', line[4])
    for i in range(len(x_n)):
        print(x_n[i])
    print(x_n)
    print(str(len(x_n)) * 10)
    print(x_n[0])

    print("**********************************************")