import pandas as pd
import datetime
import numpy as np
class A:
    def __init__(self, freq: str):
        self.freq = freq
        a = pd.read_excel('workbook.xlsx')
        self.df = pd.DataFrame(a)
        self.result = None
 
    def raznitsa(self):
        
        self.df['Time'] = pd.to_datetime(self.df['Time'])
        df = self.df.groupby(pd.Grouper(key="Time", freq=self.freq)).agg(['min', 'max'])
        for i in range(0,len(df.columns)-1,2):
            df[df.columns[i][0]+"_result"] =  df[df.columns[i+1]] - df[df.columns[i]]
        df = df.dropna()
        for i in df.columns:
            if i[-1] != '':
                df.drop([i], axis=1, inplace=True)
        self.result = df
    
        return df
    def write_excel(self):
        self.result.to_excel('output.xlsx')
        
###################################################################################################################
from  tkinter import *
import os
root = Tk()
root.title("Программа для получения отчётов от расходомеров")
root.geometry("600x200")
asd = None
value_1 = StringVar()
value_2 = StringVar()

def show():
    text_1 = value_1.get()
    text_2 = value_2.get()
    print(r2.getboolean())
    

    
def kunlik():
    a = A('24H')
    a.raznitsa()
    try:
        a.write_excel()
        l_2["text"] = "Дневной отчет сохранен.   Путь к файлу:   " + os.path.abspath('') + '\\'  + 'output.xlsx'
    except:
        print('Error')
def oylik():
    a = A('1M')
    a.raznitsa()
    try:
        a.write_excel()
        l_2["text"] = "Месячный отчет сохранен.   Путь к файлу:   " + os.path.abspath('') + '\\' + 'output.xlsx'
    except:
        print('Error')
    
l=Label(text="Получить отчёт:")
e1=Entry(textvariable=value_1)
e2=Entry(textvariable=value_2)
b_1=Button(command=kunlik, text="Дневной")
b_2=Button(command=oylik, text="Месячный")
l_2=Label()
l.pack()
b_1.pack()
b_2.pack()
l_2.pack()
root.mainloop()
