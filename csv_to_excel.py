import pandas as pd


def convert_to_excel():
    try:
        df = pd.read_csv("output.csv")
        excel_writer = pd.ExcelWriter("output.xlsx")
        df.to_excel(excel_writer, index = False) 
        excel_writer.save() 
    except:
        print("Couldn't generate excel file. Make sure you have Pandas installed and main.py has run successfully")
