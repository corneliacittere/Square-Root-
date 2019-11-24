from tkinter import *
import tkinter.messagebox


class SquareRoot:
    def __init__(self, root):
        root.title('Square Root Calculator')
        root.iconbitmap('i.ico')

        self.canvas = Canvas(root, width=400, height=300)
        self.canvas.pack()

        self.label = Label(root, text='Calculate the Square Root')
        self.label.config(font=('verdana', 14))
        self.canvas.create_window(200, 25, window=self.label)

        self.invite_label = Label(root, text="Enter your number")
        self.invite_label.config(font=('verdana', 10))
        self.canvas.create_window(200, 100, window=self.invite_label)

        self.entry = Entry(root)
        self.entry.bind('<Return>', self.my_sqrt)
        self.canvas.create_window(200, 130, window=self.entry)

        self.go_button = Button(root, text="Go!", command=self.my_sqrt, bg='brown', fg='white', font=('verdana', 9, 'bold'))
        self.canvas.create_window(200, 170, window=self.go_button)

    def my_sqrt(self, event):
        x = self.entry.get()

        try:
            self.label2 = Label(root, text=round((float(x) ** 0.5), 2), font=('verdana', 9, 'bold'))
            self.canvas.create_window(200, 230, window=self.label2)

            self.label1 = Label(root, text='The Square Root of ' + x + ' is:', font=('verdana', 9))
            self.canvas.create_window(200, 210, window=self.label1)
        except ValueError:
            tkinter.messagebox.showinfo('Error', 'Please enter a number!')


root = Tk()
obj = SquareRoot(root)
root.mainloop()




