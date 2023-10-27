import fitz
import re
import sqlite3
import os

class Data_manager:
    def __init__(self, filename):
        self.filename = filename
        self.text_lines = []
        self.test_results = []
        self.test_types = ['Общий белок','Мочевина','Креатинин']
        self.doc = fitz.open(self.filename) #opens PDF file
        self.page = self.doc[0]
        self.data = ''

    def extract_text(self):
        text_blocks = self.page.get_text('blocks') # extracts sentences with coordinates

        # this loop extracts only sentences
        for line in text_blocks:
            self.text_lines.append(re.split('\n',line[4]))


    # extracts tests results
    def get_test_result(self):
        for type in self.test_types:
            for sentence in self.text_lines:
                for i, word in enumerate(sentence):
                    if type.lower() in word.lower():
                        if re.findall(r'\d+', sentence[i + 1]) != []:
                            lst = re.findall(r'\d+', sentence[i + 1])
                            num = ''
                            if len(lst) > 1:
                                num = lst[0] + '.' + lst[1]
                            else:
                                num = lst[0]
         
                            self.test_results.append((type, float(num)))                
                  

    #gets creation date of the file
    def get_date(self):
        data_strange = self.doc.metadata['creationDate'][2:10]
        data = ''
        data += data_strange[0:4] + '.'
        data += data_strange[4:6] + '.'
        data += data_strange[6:8] 
        self.data = data
        

    #connects database
    def db_connecter(self):
        self.conn = sqlite3.connect('laboratory_data.db')
        self.c = self.conn.cursor()


    #if database named laboratory_data.db does not exists, its creates it
    
    def insert_data(self):
        if os.path.isfile('laboratory_data.db') == False:
            self.db_connecter()
            self.c.execute("""CREATE TABLE storage_of_results (
                      test_name text,
                      result real,
                      data text
            )""")
            self.conn.commit()
            self.conn.close()
            print('i created db')

        #inserts values to db table named "storage_of_results"
        self.db_connecter()
        for item in self.test_results:
            self.c.execute(f"INSERT INTO storage_of_results VALUES {(item[0], item[1], self.data)}")
        self.conn.commit()
        self.conn.close()


    #RUNS the process of data extraction with inserting into db
    def run(self):
        self.extract_text()
        self.get_test_result()
        self.get_date()
        self.insert_data()
        print('Done')
        


