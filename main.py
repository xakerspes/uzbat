import pandas as pd
import datetime
import numpy as np
###################################################################################################################
from  tkinter import *
import os
root = Tk()
root.title("Программа для получения отчётов от расходомеров")
root.geometry("500x200")
value_1 = StringVar()
value_2 = StringVar()

def show():
    
    text_1 = value_1.get()
    text_2 = value_2.get()
    print(r2.getboolean())
    
    
def soatlik():
    
    try:
        
        data = pd.read_excel('d:\\uzbat\\ExChange.xls')
        
        df = pd.DataFrame(data)
        df['Дата_и_Время'] = pd.to_datetime(df['Дата_и_Время'])
        df[df.columns[1:]] = df[df.columns[1:]].apply(np.diff, axis = 0)
        df_copy = np.array(df[df.columns[1:]][:-1])
        df.drop(index=0, inplace=True)
        df[df.columns[1:]] = df_copy

        for i in df.columns[1:]:
            df[i] = np.where((df[i] < 0),  0, df[i])

        df.to_excel('output.xlsx')
        
        print(df.head())
        l_2["text"] = "Часовой отчет сохранен.   Путь к файлу:   " + os.path.abspath('') + '\\'  + 'output.xlsx'
    
    except Exception as e:
        print(
            type(e).__name__,  # TypeError
            __file__,  # /tmp/example.py
            e.__traceback__.tb_lineno )    
    
    
def kunlik():
    
    try:
        freq='24H'
        col_names = []
        df = pd.DataFrame(pd.read_excel('d:\\uzbat\\ExChange.xls'))
        df['Дата_и_Время'] = pd.to_datetime(df['Дата_и_Время'])
        df = df.groupby(pd.Grouper(key="Дата_и_Время", freq=freq)).agg(['min', 'max'])
        for i in range(0,len(df.columns)-1,2):
            df[df.columns[i][0]+"_result"] =  df[df.columns[i+1]] - df[df.columns[i]]
            col_names.append(df.columns[i][0])
        df = df.dropna()
        for i in df.columns:
            if i[-1] != '':
                df.drop([i], axis=1, inplace=True)
        df.columns = col_names
        df.to_excel('output.xlsx')     
    
        l_2["text"] = "Дневной отчет сохранен.   Путь к файлу:   " + os.path.abspath('') + '\\'  + 'output.xlsx'
    except Exception as e:
        print(
            type(e).__name__,  # TypeError
            __file__,  # /tmp/example.py
            e.__traceback__.tb_lineno )    
        
def oylik():
    
    try:
        freq='1M'
        col_names = []
        df = pd.DataFrame(pd.read_excel('d:\\uzbat\\ExChange.xls'))
        df['Дата_и_Время'] = pd.to_datetime(df['Дата_и_Время'])
        df = df.groupby(pd.Grouper(key="Дата_и_Время", freq=freq)).agg(['min', 'max'])
        for i in range(0,len(df.columns)-1,2):
            df[df.columns[i][0]+"_result"] =  df[df.columns[i+1]] - df[df.columns[i]]
            col_names.append(df.columns[i][0])
        df = df.dropna()
        for i in df.columns:
            if i[-1] != '':
                df.drop([i], axis=1, inplace=True)
        df.columns = col_names
        df.to_excel('output.xlsx')
        
        l_2["text"] = "Месячный отчет сохранен.   Путь к файлу:   " + os.path.abspath('') + '\\' + 'output.xlsx'
    except Exception as e:
        print(
            type(e).__name__,  # TypeError
            __file__,  # /tmp/example.py
            e.__traceback__.tb_lineno )    
    
l=Label(text="Получить отчёт:")
e1=Entry(textvariable=value_1)
e2=Entry(textvariable=value_2)
b_0=Button(command=soatlik, text="Часовой")
b_1=Button(command=kunlik, text="Дневной")
b_2=Button(command=oylik, text="Месячный")
l_2=Label()
l.pack()
b_0.pack()
b_1.pack()
b_2.pack()
l_2.pack()
root.mainloop()

