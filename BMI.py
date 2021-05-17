# import tkinter
import tkinter
from tkinter import *
from tkinter import messagebox

# Creating The Application
root = Tk()
root.geometry("360x400")
root.configure(background='skyblue')
root.title('BMI Calculator')
root.resizable(width=True, height=True)
# Defining My Buttons and Calculations
def get_height():
    height_cm = float(height.get())
    return height

def get_weight():
    weight_kg = float(weight.get())
    return weight
def BMI(a=''):
    print(a)
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")

def clear():
    weight.delete(0, END)
    height.delete(0, END)
    age.delete(0, END)


def close():
    return root.destroy()

# A frame that has all the input values
frame1 = Frame(root, highlightbackground="black", highlightcolor="green", highlightthickness=1, width=350, height=150)
frame1.place(x=3, y=1,)


# Your weight Entry
label1 = Label(root, text='Enter Your Weight: ', bd=4, bg='#cef0f1', highlightthickness=2)
label1.place(x=5, y=10)
weight = Entry(root)
weight.place(x=150, y=10)

# Your Height Entry
label2 = Label(root, text='Enter Your Height: ', bd=4, bg='#cef0f1')
label2.place(x=5, y=50)
height = Entry(root)
height.place(x=150, y=50)

# The Gender Selection
label3 = Label(root, text='Gender', bd=4, bg='#cef0f1')

male = Radiobutton(root, text='Male', value='male')
male.place(x=5, y=90)

female = Radiobutton(root, text='Female', value='female')
female.place(x=100, y=90)

# Age Entry
label4 = Label(root, text='Enter Your Age:', bd=4, bg='#cef0f1')
label4.place(x=5, y=120)
age = Entry(root)
age.place(x=150, y=120)

# Body Mas Index output
label5 = Label(root, text='Body Mass Index: ', bd=4, bg='#cef0f1')
label5.place(x=5, y=200)
BMI = Entry(root)
BMI.place(x=150, y=200)

# Ideal Body Mass Index
label6 = Label(root, text='Ideal B Mass Index: ', bd=4, bg='#cef0f1')
label6.place(x=5, y=240)
IBMI = Entry(root)
IBMI.place(x=150, y=240)

# Buttons
b1 = tkinter.Button(root, text='Calculate Your Body Mass Index', width=40, bd=3, command='BMI')
b1.place(x=3, y=160)

b2 = tkinter.Button(root, text='Clear', width=10, bd=3, command=clear)
b2.place(x=3, y=280)
b3 = tkinter.Button(root, text='Exit', width=10, bd=3, command=close)
b3.place(x=245, y=280)


root.mainloop()
