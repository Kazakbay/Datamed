import fitz
import re

# extracts text from PDF into the list named "extracted_text"
def get_text_blocks(filename) -> str:
    doc = fitz.open(filename)
    page = doc[0]
    extracted_blocks = page.get_text('blocks') # gets text blocks from PDF

    extracted_text = []
    # This loop seperates text from its coordinates
    for i, line in enumerate(extracted_blocks):
        extracted_text += re.split('\n', line[4])

    # this is clear list with text only
    return extracted_text

def get_test_results(test_name, extracted_text):
    result = ()
    for i, word in enumerate(extracted_text):
        if f"{test_name}".lower() in word.lower():
            if re.findall(r'\d+', extracted_text[i + 1]) != []:
                result = [test_name, extracted_text[i + 1]]
                print(result)

def main():
    extracted_text = get_text_blocks('file_for_test4.pdf')
    for line in extracted_text:
        print(line)
    get_test_results('Общий белок', extracted_text)
    get_test_results('Мочевина', extracted_text)
    get_test_results('Креатинин', extracted_text)

main()