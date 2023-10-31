import tkinter as tk
from tkinter import filedialog
import pandas as pd
def abri_arquivo():
    file_path=filedialog.askopenfilename(filetypes=[("Arquivo(s) Excel","*.xlsx")])
    if file_path:
        df=pd.read_excel(file-path)
        exibir_dados(df)
def exibir_dados(dataframe):
    result_text.config(state="normal")
    result_text.delete("1.0","end")
