import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from bubbleSort import bubble_sort
from quickSort import quick_sort
import random

class Welcome():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Select Theme')
        self.root.maxsize(width=1200, height=600)
        self.root.config(bg='#1e1f26')

        self.UI_frame = tk.Frame(self.root, width=900, height=200, bg='#ffffff')
        self.UI_frame.grid(row=0, column=0, padx=10, pady=5)

        self.canvas = tk.Canvas(self.root, width=1100, height=380, bg='#d0e1f9')
        self.canvas.grid(row=1, column=0, padx=10, pady=5)

        tk.Label(self.UI_frame, text='Welcome to Sorting Visualiser Tool!', fg='#1e1f26', font=["arial", 30, "bold"]).grid(row=0, column=0, padx=5,
                                                                                            pady=5)

        tk.Label(self.canvas, text='Select a theme: ', font=["arial", 20, "bold"]).grid(row=1, column=0, padx=5,
                                                                                            pady=5)
        # Tkinter string variable
        # able to store any string value
        self.theme = tk.StringVar()

        # Dictionary to create multiple buttons
        values = {"Cool and Fresh": "coolFresh",
                  "Lively and Inviting": "lively",
                  "Contemporary and Bold": "contemporary"}

        # Loop is used to create multiple Radio buttons
        # rather than creating each button separately
        temp = 2
        for (text, value) in values.items():
            tk.Radiobutton(self.canvas, text=text, variable=self.theme,
                        value=value, indicator=0,
                        background="light blue").grid(row=temp, column=0, padx=5)#.pack(fill=tk.X, ipady=5)
            temp += 1
        button = ttk.Button(
            self.canvas, text='Submit', command=self.theme_selection).grid(row=temp+1, column=0, padx=10, pady=10)#.pack()

        self.root.mainloop()

    def theme_selection(self):
        theme = self.theme.get()
        self.color_scheme(theme)


    def color_scheme(self, theme):
        if theme == 'coolFresh':
            bg = '#05386B'
            UI_color = '#379683'
            canvas_color = '#5CDB95'
            light_color = '#EDF5E1'
            self.run_algo(bg, UI_color, canvas_color, light_color)

        elif theme == 'lively':
            bg = '#E7717D'
            UI_color = '#7E685A'
            canvas_color = '#C2B9B0'
            light_color = '#C2CAD0'
            self.run_algo(bg, UI_color, canvas_color, light_color)

        elif theme == 'contemporary':
            bg = '#1A1A1D'
            UI_color = '#C3073F'
            canvas_color = '#6F2232'
            light_color = '#4E4E50'
            self.run_algo(bg, UI_color, canvas_color, light_color)

    def run_algo(self, bg, UI_color, canvas_color, light_color):
        sorting = SortingAlgorithm(bg, UI_color, canvas_color, light_color)
        sorting.run()
class SortingAlgorithm():
    def __init__(self, bg, UI_color, canvas_color, light_color):
        self.root = tk.Tk()
        self.UI_color = UI_color
        self.canvas_color = canvas_color
        self.light_color = light_color
        self.bg = bg
        self.root.title('Sorting Algorithm Visualisation')
        self.root.maxsize(width=1200, height=600)
        self.root.config(bg=bg)
        self.style = ttk.Style()

        # Button Style
        self.style.configure('W.TButton', font =
                       ('calibri', 10, 'bold',),
                        foreground='#203647',
                        background=bg)

        # Font Style
        self.fontfamilylist = list(tkFont.families())

        self.fontindex = 3 # Terminal

        self.fontStyle = tkFont.Font(family=self.fontfamilylist[self.fontindex], size=15)

        self.fontBarIndex = 22
        self.fontBarStyle = tkFont.Font(family=self.fontfamilylist[self.fontBarIndex], size=10)


        # Variables
        self.selected_alg = tk.StringVar()
        self.data = []

    def run(self):
        # frame / base layout
        self.UI_frame = tk.Frame(self.root, width=900, height=200, bg=self.UI_color)
        self.UI_frame.grid(row=0, column=0, padx=20, pady=5)

        self.canvas = tk.Canvas(self.root, width=1100, height=380, bg=self.canvas_color)
        self.canvas.grid(row=1, column=0, padx=10, pady=5)

        # User Interface Area
        # Row[0]
        tk.Label(self.UI_frame, text='Algorithm: ', bg=self.UI_color, font=self.fontStyle).grid(row=0, column=0, padx=5, pady=5,
                                                                                  sticky=tk.W)
        self.algMenu = ttk.Combobox(self.UI_frame, textvariable=self.selected_alg, values=['Bubble Sort', 'Quick Sort'],
                               font=("arial", 10, "bold"), width=15)
        self.algMenu.grid(row=0, column=1, padx=5, pady=5)
        self.algMenu.current(0)

        self.speedScale = tk.Scale(self.UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=tk.HORIZONTAL,
                              label='Select Speed [s]', font=("arial", 10, "italic bold"), relief=tk.GROOVE, bd=2,
                              width=10, bg=self.light_color)
        self.speedScale.grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(self.UI_frame, text='Start', style='W.TButton', command=self.StartAlgorithm).grid(row=0, column=3, padx=5,
                                                                                           pady=5)
        # Row[1]
        # Label(UI_frame, text='Size:', bg='#007CC7', font=fontStyle).grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.sizeEntry = tk.Scale(self.UI_frame, from_=3, to=30, resolution=1, orient=tk.HORIZONTAL, label='Data Size',
                             font=("arial", 10, "italic bold"), relief=tk.GROOVE, bd=2, width=10, bg=self.light_color)
        self.sizeEntry.grid(row=1, column=0, padx=5, pady=5)

        self.minEntry = tk.Scale(self.UI_frame, from_=0, to=20, resolution=1, orient=tk.HORIZONTAL, label='Min Value',
                            font=("arial", 10, "italic bold"), relief=tk.GROOVE, bd=2, width=10, bg=self.light_color)
        self.minEntry.grid(row=1, column=1, padx=5, pady=5)

        self.maxEntry = tk.Scale(self.UI_frame, from_=20, to=100, resolution=1, orient=tk.HORIZONTAL, label='Max Value',
                            font=("arial", 10, "italic bold"), relief=tk.GROOVE, bd=2, width=10, bg=self.light_color)
        self.maxEntry.grid(row=1, column=2, padx=5, pady=5)

        ttk.Button(self.UI_frame, text='Generate', style='W.TButton', command=self.Generate).grid(row=1, column=3, padx=5, pady=5)

        self.root.mainloop()

    def drawData(self, data, colorArray):
        self.canvas.delete('all')
        c_height = 380
        c_width = 1100
        x_width = c_width / (len(data) + 1)
        offset = 30
        spacing = 10
        normalizedData = [i/max(data) for i in data]
        for i, height in enumerate(normalizedData):
            # top left
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 340
            # bottom right
            x1 = (i + 1) * x_width + offset
            y1 = c_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill= colorArray[i])
            self.canvas.create_text(x0+2, y0, anchor=tk.SW, text=str(data[i]), font=self.fontBarStyle)
        self.root.update()


    def StartAlgorithm(self):
        if not data: return

        if self.algMenu.get() == 'Quick Sort':
            quick_sort(data, 0, len(data) - 1, self.drawData, self.speedScale.get())
            self.drawData(data, ['green' for x in range(len(data))])

        elif self.algMenu.get() == 'Bubble Sort':
            bubble_sort(data, self.drawData, self.speedScale.get())


    def Generate(self):
        global data
        minValue = int(self.minEntry.get())
        maxValue = int(self.maxEntry.get())
        size = int(self.sizeEntry.get())

        data = []
        for _ in range(size):
            data.append(random.randrange(minValue, maxValue+1))
        self.drawData(data, [self.bg for x in range(len(data))])


if '__main__' == __name__:
    sa = Welcome()

