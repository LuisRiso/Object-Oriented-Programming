#15.8.5. Color Chooser
#Tkinter includes a nice dialog box for choosing colors. 
#You provide it with a parent window and an initial color, and it returns a color in two different specifications: ,
# 1) a RGB value as a tuple, such as (255, 0, 0) which represents red
# 2) a hexadecimal string used in web pages, such as "#FF0000" which also represents red. 
#If the user cancels the operation, the return values are None and None.

#O Tkinter inclui uma caixa de diálogo bacana para escolher cores. 
#Você fornece a ele uma janela pai e uma cor inicial, e ele retorna uma cor em duas especificações diferentes: 
# 1) um valor RGB como uma tupla, como que representa vermelho, 
# 2) uma string hexadecimal usada em páginas da web, como que também representa vermelho. 
#Se o usuário cancelar a operação, os valores de retorno são e .(255, 0, 0)"#FF0000"NoneNone

from tkinter import colorchooser

rgb_color, web_color = colorchooser.askcolor(parent=application_window, initialcolor=(255, 0, 0))
