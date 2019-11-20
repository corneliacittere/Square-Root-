from tkinter import *
import tkinter.messagebox


def mySqrt(event):
    x = entry.get()

    try:
        label2 = Label(window, text=round((float(x) ** 0.5), 2), font=('verdana', 9, 'bold'))
        canvas.create_window(200, 230, window=label2)
        label1 = Label(window, text='The Square Root of ' + x + ' is:',font=('verdana', 9))
        canvas.create_window(200, 210, window=label1)
    except ValueError:
        tkinter.messagebox.showinfo('Error', 'Please enter a number!')


"""Creating a window"""
window = Tk()

"""Adding a window title"""
window.title('Square Root')

"""Setting window icon"""
window.iconbitmap('i.ico')

"""Creating a canvas"""
canvas = Canvas(window, width=400, height=300)
canvas.pack()

"""Adding a label"""
label = Label(window, text='Calculate the Square Root')
label.config(font=('verdana', 14))
canvas.create_window(200, 25, window=label)

"""Adding invitation to enter the number"""
inviteLabel = Label(window, text="Enter your number")
inviteLabel.config(font=('verdana', 10))
canvas.create_window(200, 100, window=inviteLabel)

"""Adding an entry box"""
entry = Entry(window)
entry.bind('<Return>', mySqrt)
canvas.create_window(200, 130, window=entry)

"""Adding a button"""
goButton = Button(window, text="Go!", command=mySqrt, bg='brown', fg='white', font=('verdana', 9, 'bold'))
canvas.create_window(200, 170, window=goButton)

window.mainloop()
