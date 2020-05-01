from tkinter import *


# Creating an instance of Tk initializes this interpreter and creates the root window.
# I don`t have to call tkinter it later
root = Tk()
# This allows to make the input box
e = Entry(root)
# All the images that are used
photo = PhotoImage(file="machine-learning.png", )


# The main framework (all the windows)
# Stats = Label(root, width=15, height=50, bg="blue") to tutaj to przykładowe okienko
# Stats.pack(side=LEFT)

label = Label(root, image=photo, width=800, height=450, bg="black")
label.pack()


topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, expand="yes")
root.configure(width=1000, height=400,)
root.configure(bg="black")


# the main text box that is changing
introduction = Label(root, font=("Courier", 15), width=80, height=10, bg="black", fg="white",
                     text=" Wpisz szukane hasło: ________  ")
e.pack()
introduction.pack()


# exit and the buttons
button2 = Button(bottomFrame, width=35, height=1, text="Zamknij", fg="red", command=root.destroy)
button2.pack(side=BOTTOM)


button1 = Button(bottomFrame, width=35, height=1,
                 text="pobieraj", fg="blue",
                 command="pass")
button1.pack(side=BOTTOM, )


root.mainloop()


