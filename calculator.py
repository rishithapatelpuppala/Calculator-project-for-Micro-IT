import tkinter as tk
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")
root.minsize(300, 400)
root.resizable(True, True)
root.configure(bg="#f0f0f0")
input_field = tk.Entry(root, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify="right")
input_field.pack(fill="x", padx=10, pady=10, ipady=10)
def add_to_input(char):
    input_field.insert(tk.END, str(char))
def evaluate():
    try:
        result = eval(input_field.get())
        input_field.delete(0, tk.END)
        input_field.insert(0, str(result))
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")
def clear():
    input_field.delete(0, tk.END)
def handle_key(event):
    if event.keysym == "Return":
        evaluate()
    elif event.keysym == "Escape":
        clear()
root.bind("<Key>", handle_key)
button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both")
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]
for r in range(4):
    for c in range(4):
        text = buttons[r][c]
        if text == 'C':
            cmd = clear
        elif text == '=':
            cmd = evaluate
        else:
            cmd = lambda ch=text: add_to_input(ch)

        btn = tk.Button(button_frame, text=text, font=("Arial", 20), command=cmd)
        btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)
    button_frame.rowconfigure(i, weight=1)
root.mainloop()