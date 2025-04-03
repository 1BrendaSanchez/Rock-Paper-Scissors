import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors Game")

frame1 = tk.Frame(window)
frame1.grid(column=0, row=0)

frame2 = tk.Frame(window)
frame2.grid(column=1, row=0)

window.mainloop()