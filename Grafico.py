#pip install matplotlib

import tkinter as tk
import random
from matlibplot.backend.backend_tkagg import FigureCanvasTkAgg

def update_graph():
    data=[random.randint(1,10)for _ in range(5)]
    ax.clear()
    canvas.draw()

root=tk.Tk()
root.title("Gráfico")

update_button=tk.Button(root,text="Atualizar Gráfico",command=update_graph)

fig=Figure(figsize=(5,4),dpi=100)
ax=fig.add_subplot(111)

canvas.get_tk_widget().pak()

update_graph()
root.mainloop()
