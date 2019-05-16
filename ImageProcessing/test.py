import tkinter as tk
root = tk.Tk()
def enter(event):
    root_1 = tk.Tk()
    c = b.get()
    c = c.lower()
    d = c.split(" ")
    f = 0
    print(d)
    for x in d:
        for y in d:
            if y == x:
                f += 1
        tk.Label(root_1, text = "{} is there {} no. of times in the sentence.".format(x, f)).grid()
        f = 0
a = tk.Label(text = "Type a sentence here - ", bg = "black", fg = "white")
a.grid(row = 0, column = 0)
b = tk.Entry(root)
b.grid(row = 0, column = 1)
c = tk.Label(root,text = "clik enter/return",bg = "black", fg = "white")
c.grid(row = 1,column = 0)
root.bind('<Return>', enter)
root.mainloop()
