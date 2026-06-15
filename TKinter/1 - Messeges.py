#15.8.1. Messages
#A messagebox can display information to a user. There are three variations on these dialog boxes based on the type of message you want to display. 
#The functions’ first parameter gives a name for the dialog box which is displayed in the window’s header. 
#The second parameter is the text of the message. The functions return a #string which is typically ignored.

#A messageboxpode exibir informações para um usuário. Há três variações nessas caixas de diálogo com base no tipo de mensagem que você deseja exibir. 
#O primeiro parâmetro das funções fornece um nome para a caixa de diálogo que é exibida no cabeçalho da janela. 
#O segundo parâmetro é o texto da mensagem. 
#As funções retornam uma string que normalmente é ignorada.

from tkinter import messagebox

messagebox.showinfo("Information","Informative message")
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")