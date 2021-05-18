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

bmi = 0

# Defining My Buttons and Calculations
def activate(value):
    variable.set(value)
    if value != "Select...":
        age.config(state='normal')
    else:
        age.config(state='readonly')


gender_menu = OptionMenu(root, variable, *options, command=activate)
gender_menu.place(relx=0.3, rely=0.4)

category = Entry(root)

def bmi_calculator():
    try:
        float(weight.get())
        float(height.get())
        float(age.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * float(weight.get())) / ((float(height.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            IBMI.config(state='normal')
            IBMI.insert(0, result)
            IBMI.config(state='readonly')
            result_bmi = float(weight.get()) / ((float(height.get()) / 100) ** 2)
            IBMI.config(state='normal')
            BMI.insert(0, round(result_bmi, 1))
            BMI.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * float(weight.get())) / ((float(height.get()) / 100) ** 2)) + (
                        0.03 * float(age.get())) + 11
            result = round(result, 1)
            IBMI.config(state='normal')
            IBMI.insert(0, result)
            IBMI.config(state='readonly')
            result_bmi = float(weight.get()) / ((float(height.get()) / 100) ** 2)
            BMI.config(state='normal')
            BMI.insert(0, round(result_bmi, 1))
            BMI.config(state='readonly')

        if result_bmi <= 18.5:
            status.insert(0, 'Underweight')
        elif 18.5 <= result_bmi <= 24.9:
            status.insert(0, 'Normal Weight')
        elif 25 <= result_bmi <= 29.9:
            status.insert(0, 'Overweight')
        elif result_bmi >= 30:
            status.insert(0, 'Obese')

    except ValueError:
        messagebox.showerror(title=None, message='Gender was not specified or invalid entry was given')
        clear()

def clear():
    weight.delete(0, END)
    height.delete(0, END)
    age.config(state='normal')
    BMI.config(state='normal')
    IBMI.config(state='normal')
    age.delete(0, END)
    BMI.delete(0, END)
    IBMI.delete(0, END)
    age.config(state='readonly')
    BMI.config(state='readonly')
    IBMI.config(state='readonly')
    weight.focus()
    variable.set(options[0])


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
options = ['Select...', 'Male', "Female"]
variable = StringVar(root)
variable.set(options[0])
gender = Label(root, text="Gender:", bd=4, bg='#cef0f1')
gender.place(x=5, y=85)
# Age Entry
label4 = Label(root, text='Enter Your Age:', bd=4, bg='#cef0f1')
label4.place(x=5, y=120)
age = Entry(root, )
age.place(x=150, y=120)

# Body Mas Index output
label5 = Label(root, text='Body Mass Index: ', bd=4, bg='#cef0f1')
label5.place(x=5, y=200)
BMI = Entry(root)
BMI.place(x=150, y=200)

# Status Entry
label6 = Label(root, text='BMI Status: ', bd=4, bg='#cef0f1')
label6.place(x=5, y=280)
status = Entry(root)
status.place(x=150, y=280)


# Ideal Body Mass Index
label6 = Label(root, text='Ideal B Mass Index: ', bd=4, bg='#cef0f1')
label6.place(x=5, y=240)
IBMI = Entry(root)
IBMI.place(x=150, y=240)

# Buttons
b1 = tkinter.Button(root, text='Calculate Your Body Mass Index', width=40, bd=3, command=bmi_calculator)
b1.place(x=3, y=160)

b2 = tkinter.Button(root, text='Clear', width=10, bd=3, command=clear)
b2.place(x=3, y=350)
b3 = tkinter.Button(root, text='Exit', width=10, bd=3, command=close)
b3.place(x=245, y=350)


root.mainloop()
