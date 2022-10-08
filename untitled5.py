import requests
import json
import pandas as pd
import xlwings as xw
from time import sleep
from datetime import datetime
import requests
import json
import math
import os
import glob
import requests
import time
import os
import shutil
import pandas as pd
from datetime import datetime
import shutil
import mysql.connector
import csv
import sqlalchemy
import openpyxl
from sqlalchemy import create_engine
import xlwings as xw
from sqlalchemy import create_engine

engine = sqlalchemy.create_engine('mysql+pymysql://admin:@localhost:3306/test')
TOTAL_TARDING_MINUTES=375
INTERVAL=1                #<<<<====================CHANE ACCORDINGLY[1/3/5/10/15...............]
REPEAT_CODE=TOTAL_TARDING_MINUTES/INTERVAL




def DATA_EXTRACT():                                  
    url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
    url1 = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'

    headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
      'accept-language':'en-US,en;q=0.9,bn;q=0.8','accept-encoding':'gzip, deflate, br'}
    session = requests.Session()
    data= session.get(url,headers= headers, timeout=5).json()["records"]["data"]
    ocdata =[]
    for i in data:
        for j,k in i.items():
            if j=="CE" or j=="PE":
                info = k
                info["InstrumentTye"]=j
                ocdata.append(info)
    df =pd.DataFrame(ocdata)
    wb = xw.Book("oi.xlsx")
    st = wb.sheets("oi")
    st.range("A1").value =df
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    df.to_csv("nifty_DATA.csv",index=False)
    df.columns = df.columns.str.replace(' ', '')
    os.rename('nifty_DATA.csv', time.strftime('NFTY-''%d%m%y-%H%M%S.csv'))
    df.to_csv("live_data.csv",index=False)
    
    df.to_sql(
        name='live_data',
            con=engine,
            index=False,
            if_exists='append'
            )

    ocdata2 =[]
    data2= session.get(url1,headers= headers).json()["records"]["data"] 
    ocdata2 =[]
    for a in data2:
        for g,h in a.items():
            if g=="CE" or g==("PE"):
                info = h
                info["InstrumentTye"]=g    
                ocdata2.append(info)
    df =pd.DataFrame(ocdata2)
    wb = xw.Book("bc.xlsx")
    st = wb.sheets("oi")
    st.range("A1").value =df
    current_time = now.strftime("%H:%M:%S")
    df.to_csv("bank.csv",index=False)
    df.to_csv("data.csv",index=False)
    
    
    df.to_sql(
        name= 'data',
        con=engine,
        index=False,
        if_exists='append'
        )
    df.columns = df.columns.str.replace(' ', '')
    os.rename('bank.csv', time.strftime('bank-''%d%m%Y-%H%M%S.csv'))
    print(current_time+' '+'DATA RECORDED SUCCESSFULLY')  
   
    df = pd.read_csv('LIVE_DATA.csv',skipinitialspace = True,skiprows=0)
   

    column_name = 'InstrumentTye'

    replace_symbols = ['>', '<', ':', '"', '/', '\\\\', '\|', '\?', '\*']
    df[column_name] = (
       df[column_name].replace(replace_symbols, '', regex=True).str.strip().str.title()
    )
    unique_values = df[column_name].unique()

    for unique_value in unique_values:
        df_output = df[df[column_name].str.contains(unique_value)]
        output_path = os.path.join('output', time.strftime('CEPE''%d%m%Y%H%M%S') +'.xlsx')
        df_output.to_excel(output_path, sheet_name=unique_value[:31], index=False)

        
    
   # shutil.move("C:/Users/patia/Downloads/DATA.csv", "E:/Download/data_live/bank/DATA.csv")
    
    #os.rename('LIVE_DATA.csv', time.strftime('NFTY-''%d%m%y-%H%M%S.csv'))
    time.sleep(INTERVAL*115)
     
for j in range(0,int(REPEAT_CODE)):
     while True:
         try:
             DATA_EXTRACT()
             break
         except:
             print("Trying to collect data")
             time.sleep(2)
             



     

