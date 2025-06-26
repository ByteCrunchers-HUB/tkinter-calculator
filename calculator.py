from tkinter import *

def press(key):
    entry.insert(END, key)
def clear():
    entry.delete(0, END)
def equal():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")
mw = Tk()
mw.title("Calculator")
mw.geometry("350x500")

entry = Entry(mw, font=("Corbel", 24), bd=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
buttons = [('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]
for (text, row, col) in buttons:
    if text == '=':
        b1=Button(mw, text=text, width=5, height=2, font=("Corbel", 18),command=equal)
        b1.grid(row=row, column=col, padx=5, pady=5)
    elif text == 'C':
        b2=Button(mw, text=text, width=23, height=2, font=("Corbel", 18),command=clear)
        b2.grid(row=row, column=col, columnspan=4, padx=5, pady=5)
    else:
        b3=Button(mw, text=text, width=5, height=2, font=("Corbel", 18),command=lambda t=text: press(t))
        b3.grid(row=row, column=col, padx=5, pady=5)

mw.mainloop()
