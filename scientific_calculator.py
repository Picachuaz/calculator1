import tkinter as tk
from math import sin, cos, tan, log, log10, sqrt, pi, e, radians

memory = 0  # Memory storage

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = evaluate(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def memory_click(action):
    global memory
    try:
        current = float(entry.get())
        if action == "M+":
            memory += current
        elif action == "M-":
            memory -= current
        elif action == "MR":
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(memory))
        elif action == "MC":
            memory = 0
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def evaluate(expression):
    expression = expression.replace("π", str(pi)).replace("e", str(e))
    expression = expression.replace("√", "sqrt").replace("^", "**")
    expression = expression.replace("ln", "log").replace("log", "log10")
    expression = expression.replace("sin", "sin(radians(")
    expression = expression.replace("cos", "cos(radians(")
    expression = expression.replace("tan", "tan(radians(")
    expression = expression.replace(")", "))")
    return str(eval(expression))

def key_input(event):
    key = event.char
    if key in "0123456789.+-*/()^":
        entry.insert(tk.END, key)
    elif key == "\r":  # Enter key
        try:
            result = evaluate(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "\x08":  # Backspace
        entry.delete(len(entry.get())-1, tk.END)

# 🎨 Theme
bg_color = "#1e1e2f"
entry_bg = "#2e2e3e"
btn_bg = "#3e3e5e"
btn_fg = "#ffffff"
accent_color = "#00c2cb"

root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.configure(bg=bg_color)
root.bind("<Key>", key_input)

entry = tk.Entry(root, font="Arial 20", bg=entry_bg, fg=accent_color, insertbackground=accent_color, bd=0)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ["M+", "M-", "MR", "MC"],
    ["sin", "cos", "tan", "√"],
    ["log", "ln", "π", "e"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "^", "+"],
    ["C", "(", ")", "="]
]

for row in buttons:
    frame = tk.Frame(root, bg=bg_color)
    frame.pack(pady=2)
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 16 bold", width=5, height=2,
                      bg=btn_bg, fg=btn_fg, activebackground=accent_color, activeforeground=bg_color, bd=0)
        b.pack(side=tk.LEFT, padx=4, pady=4)
        if btn in ["M+", "M-", "MR", "MC"]:
            b.bind("<Button-1>", lambda e, a=btn: memory_click(a))
        else:
            b.bind("<Button-1>", click)

root.mainloop()