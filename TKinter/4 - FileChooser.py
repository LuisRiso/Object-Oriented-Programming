#15.8.4. File Chooser 
#A common task is to select the names of folders and files on a storage device. This can be accomplished using a filedialog object. 
#Note that these commands do not save or load a file. They simply allow a user to select a file. 
#Once you have the file name, you can open, process, and close the file using appropriate Python code. 
#These dialog boxes always return you a “fully qualified file name” that includes a full path to the file. 
#Also note that if a user is allowed to select multiple files, the return value is a tuple that contains all of the selected files. 
#If a user cancels the dialog box, the returned value is an empty string.

#Uma tarefa comum é selecionar os nomes de pastas e arquivos em um dispositivo de armazenamento. 
# Isso pode ser feito usando um filedialogobjeto. Observe que esses comandos não salvam ou carregam um arquivo. 
# Eles simplesmente permitem que um usuário selecione um arquivo. 
# Depois de ter o nome do arquivo, você pode abrir, processar e fechar o arquivo usando o código Python apropriado. 
# Essas caixas de diálogo sempre retornam um "nome de arquivo totalmente qualificado" que inclui um caminho completo para o arquivo. 
# Observe também que se um usuário tiver permissão para selecionar vários arquivos, 
#o valor de retorno será uma tupla que contém todos os arquivos selecionados. 
#Se um usuário cancelar a caixa de diálogo, o valor retornado será uma string vazia.

import tkinter as tk
from tkinter import filedialog
import os

application_window = tk.Tk()

# Build a list of tuples for each file type the file dialog should display
my_filetypes = [('all files', '.*'), ('text files', '.txt')]

# Ask the user to select a folder.
answer = filedialog.askdirectory(parent=application_window,
                                 initialdir=os.getcwd(),
                                 title="Please select a folder:")

# Ask the user to select a single file name.
answer = filedialog.askopenfilename(parent=application_window,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:",
                                    filetypes=my_filetypes)

# Ask the user to select a one or more file names.
answer = filedialog.askopenfilenames(parent=application_window,
                                     initialdir=os.getcwd(),
                                     title="Please select one or more files:",
                                     filetypes=my_filetypes)

# Ask the user to select a single file name for saving.
answer = filedialog.asksaveasfilename(parent=application_window,
                                      initialdir=os.getcwd(),
                                      title="Please select a file name for saving:",
                                      filetypes=my_filetypes)