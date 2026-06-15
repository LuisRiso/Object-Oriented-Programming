#15.8.2. Yes/No Questions
#The tkinter messagebox object also allows you to ask a user simple yes/no type questions 
#and varies the button names based on the type of question.
#The return value is a Boolean, True or False, answer to the question. 
#If “cancel” is an option and the user selects the “cancel” button, None is returned.

#O objeto tkinter messageboxtambém permite que você faça perguntas simples do tipo sim/não ao usuário 
#e varia os nomes dos botões com base no tipo de pergunta.
#O valor de retorno é uma resposta Booleana, Verdadeiro ou Falso, para a pergunta. 
#Se “cancelar” for uma opção e o usuário selecionar o botão “cancelar”, None é retornado.

from tkinter import messagebox

answer = messagebox.askokcancel("Question","Do you want to open this file?")
answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
answer = messagebox.askyesno("Question","Do you like Python?")
answer = messagebox.askyesnocancel("Question", "Continue playing?")

