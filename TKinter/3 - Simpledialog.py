#15.8.3. Single Value Data Entry
#If you want to ask the user for a single data value, either a string, integer, or floating point value, you can use a simpledialog object. 
#A user can enter the requested value and hit “OK”, which will return the entered value. If the user hits “Cancel,” then None is returned.

#Se você quiser pedir ao usuário um único valor de dados, seja uma string, um inteiro ou um valor de ponto flutuante, você pode usar um simpledialogobjeto. 
#Um usuário pode digitar o valor solicitado e clicar em “OK”, que retornará o valor digitado. Se o usuário clicar em “Cancelar”, então Noneé retornado.

import tkinter as tk
from tkinter import simpledialog

application_window = tk.Tk()

answer = simpledialog.askstring("Input", "What is your first name?",
                                parent=application_window)
if answer is not None:
    print("Your first name is ", answer)
else:
    print("You don't have a first name?")

answer = simpledialog.askinteger("Input", "What is your age?",
                                 parent=application_window,
                                 minvalue=0, maxvalue=100)
if answer is not None:
    print("Your age is ", answer)
else:
    print("You don't have an age?")

answer = simpledialog.askfloat("Input", "What is your salary?",
                               parent=application_window,
                               minvalue=0.0, maxvalue=100000.0)
if answer is not None:
    print("Your salary is ", answer)
else:
    print("You don't have a salary?")