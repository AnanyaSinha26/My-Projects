import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

frame = tk.Frame(root)

button1 = tk.Button(frame, width=10, height=5)
button2 = tk.Button(frame, width=10, height=5)
button3 = tk.Button(frame, width=10, height=5, text="●", fg="red")
button4 = tk.Button(frame, width=10, height=5)
button5 = tk.Button(frame, width=10, height=5)
button6 = tk.Button(frame, width=10, height=5)
button7 = tk.Button(frame, width=10, height=5)
button8 = tk.Button(frame, width=10, height=5)
button9 = tk.Button(frame, width=10, height=5)
button10 = tk.Button(frame, width=10, height=5)
button11 = tk.Button(frame, width=10, height=5)
button12 = tk.Button(frame, width=10, height=5)
button13 = tk.Button(frame, width=10, height=5)
button14 = tk.Button(frame, width=10, height=5)
button15 = tk.Button(frame, width=10, height=5)
button16 = tk.Button(frame, width=10, height=5)

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
button4.grid(row=0,column=3)
button5.grid(row=1,column=0)
button6.grid(row=1,column=1)
button7.grid(row=1,column=2)
button8.grid(row=1,column=3)
button9.grid(row=2,column=0)
button10.grid(row=2,column=1)
button11.grid(row=2,column=2)
button12.grid(row=2,column=3)
button13.grid(row=3,column=0)
button14.grid(row=3,column=1)
button15.grid(row=3,column=2)
button16.grid(row=3,column=3)

buttons_with_red_dots = [2, 4, 11, 13]
for i in buttons_with_red_dots:
    exec(f"button{i+1}.config(text='●', fg='red')")

frame.pack(expand=True)

root.mainloop()
