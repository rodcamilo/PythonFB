import tkinter as tk
from tkinter import messagebox
def adicao(a, b):
  return a + b
def subtracao(a, b):
  return a - b
def multiplicacao(a, b):
  return a * b
def divisao(a, b):
  if b != 0:
    return a / b
  else:
    return "NÃO EXISTE DIVISÃO POR ZERO!"
def calcular():
  try:
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operacao = str(entry_operacao.get())
    if operacao == "+":
      resultado = adicao(num1, num2)
    elif operacao == "-":
      resultado = subtracao(num1, num2)
    elif operacao == "*":
      resultado = multiplicacao(num1, num2)
    else:
      resultado = divisao(num1, num2)
    resultado_label.config(text="RESULTADO: " + str(resultado))
  except ValueError:
    messagebox.showerror("ERRO", "DIGITE APENAS NÚMEROS!")
def criar_interface():
  root = tk.Tk()
  root.title("CALCULADORA PYTHON")
  tk.Label(root, text="PRIMEIRO NÚMERO:").grid(row=0, column=0)
  tk.Label(root, text="SEGUNDO NÚMERO:").grid(row=1, column=0)
  tk.Label(root, text="OPERAÇÃO:").grid(row=2, column=0)
  global entry_num1, entry_num2, entry_operacao
  entry_num1 = tk.Entry(root)
  entry_num2 = tk.Entry(root)
  entry_operacao = tk.Entry(root)
  entry_num1.grid(row=0, column=1)
  entry_num2.grid(row=1, column=1)
  entry_operacao.grid(row=2, column=1)
  calcular_button = tk.Button(root, text="CALCULAR", command=calcular)
  calcular_button.grid(row=3, column=0, columnspan=2)
  global resultado_label
  resultado_label = tk.Label(root, text="RESULTADO:")
  resultado_label.grid(row=4, column=0, columnspan=2)
  root.mainloop()
criar_interface()
