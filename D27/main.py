import tkinter

window = tkinter.Tk()

window.title("Hello I'm Tsibo")

window.minsize(width=500, height=300)

#label 
my_label = tkinter.Label(text="Hey, I am a label.", font=("Arial", 24, "bold"))
my_label.pack()


window.mainloop()