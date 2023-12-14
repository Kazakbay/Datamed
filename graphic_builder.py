import sqlite3
from matplotlib import pyplot as plt
from datetime import datetime
import os


class Graphic_builder:
    def __init__(self, test_name, username, lan):
        self.lan = lan
        self.test_name = test_name
        self.username = username
        self.x_y_data = [[], []]
        print(os.path.isfile('laboratory_data.db'))
        if os.path.isfile('laboratory_data.db') == True:
            self.conn = sqlite3.connect('laboratory_data.db')
            self.c = self.conn.cursor()
        else:
            print('No database!')
        self.image = None
        self.name = None
        self.db_exist = None
        self.last_result = None
    
    def extract_data(self):
        try:
            self.c.execute(f"""SELECT * FROM {self.username} WHERE test_name = '{self.test_name}'""")
            self.test_results = self.c.fetchall()
            self.db_exist = True
        except:
            print('No db!')
            self.db_exist = False
    



    def remove_duplicates_n_sort_by_date(self):
        #removes duplicated values from list
        self.test_results = list(dict.fromkeys(self.test_results))

        #sorts list items by date
        self.test_results.sort(key = lambda x: datetime.strptime(x[2], "%Y.%m.%d")) 
        
    
    def build_gpaph(self):
        data_x = []
        data_y = []

        fig = plt.figure(figsize=(10, 5))

        ax = plt.gca()


        for i in self.test_results:
            date = datetime.strptime(i[2], "%Y.%m.%d")
            x = date.strftime('%Y-%b-%d')
            data_x.append(x)
            data_y.append(float(i[1]))


        plt.title(self.test_name)

        if self.test_name == 'Креатинин':
            ylabel = 'µmol/L'
        elif self.test_name == 'Общий белок':
            ylabel = 'g/L'
        elif self.test_name == 'Мочевина':
            ylabel = 'mmol/L'
        elif self.test_name == 'Гемоглобин':
            ylabel = 'g/L'
        elif self.test_name == 'эритроциты':
            ylabel = 'cells/mcL'
        elif self.test_name == 'Тромбоциты':
            ylabel = 'mcL'
        elif self.test_name == 'Холестерин':
            ylabel = 'mg/dL'
        elif self.test_name == 'Глюкоза':
            ylabel = 'mmol/L'


        plt.ylabel(ylabel)
        plt.plot(data_x, data_y, 'H:g', linewidth = 2, )
        for tick in ax.get_xticklabels():
            tick.set_rotation(30)
        # save plot like a photo
        self.name = f"{self.test_name}_{self.username}.png"
        plt.savefig(self.name, dpi = 400, bbox_inches='tight')
        #plt.show()

        
    def ai_response(self):
        from openai import OpenAI
        client = OpenAI(api_key='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')
        if self.lan == 'eng':
            completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "You give a list of possible diagnoses according to the results of biological tests to answer on the exam. In short by 3 sentences."},
            {"role": "user", "content": f'What is the patient’s diagnosis if the test results are as follows? {self.test_results}'}
            ]
            )
        elif self.lan == 'kz':
            completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "You give a list of possible diagnoses according to the results of biological tests to answer on the exam. In short by 3 sentences."},
            {"role": "user", "content": f'What is the patient’s diagnosis if the test results are as follows? {self.test_results}, give answer in grammatically correct Kazakh'}
            ]
            )

        self.chat_gpt_opinion = f"ChatGPT: \n {completion.choices[0].message.content}"
        


    def run(self):
        self.extract_data()
        if self.db_exist == True:
            self.remove_duplicates_n_sort_by_date()
            self.build_gpaph()
            self.ai_response()
        
        else:
            print('Nothing to do!')

        if self.chat_gpt_opinion != None:
            return self.chat_gpt_opinion
        else:
            return 'No data'