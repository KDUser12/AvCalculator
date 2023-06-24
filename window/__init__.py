import customtkinter
from PIL import Image
from tkinter import END

import statistics

class App(customtkinter.CTk):

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')


    def __init__(self):
        super().__init__()
        self.title('CalculApp')
        self.iconbitmap('assets/icons/CalculApp_icon_Windows.ico')

        self.geometry('350x500')
        self.resizable(False, False)
        
        title_image = customtkinter.CTkImage(Image.open('assets/icons/CalculApp_icon_Windows.ico'), size=(30, 30))
        title_font = customtkinter.CTkFont(family='Roboto', size=30, weight='bold')
        title_label = customtkinter.CTkLabel(master=self, width=350, height=75, text=' CalculApp', font=title_font, image=title_image, compound='left')
        title_label.grid()

        textbox = customtkinter.CTkTextbox(master=self, width=250, height=300, activate_scrollbars=False)
        textbox.grid()

        button_font = customtkinter.CTkFont(family='Roboto', size=15)
        button = customtkinter.CTkButton(master=self, height=25, width=150, text="Entrer", font=button_font, command=lambda: action_button(textbox, text_label))
        button.grid(pady=25)

        text_label = customtkinter.CTkLabel(master=self, height=20, width= 350, text='Résultat', fg_color='#585858')
        text_label.grid(pady=30)
        

def action_button(textbox, text_label):
    arg1 = textbox.get("1.0", END)
    words = arg1.split()
    numbers = []

    for word in words:
        try:
            number = float(word)
            numbers.append(number)
        except ValueError:
            pass

    if numbers:
        result = statistics.mean(numbers)
        text_label.configure(text=result)
    else:
        text_label.configure(text="Aucune donnée disponible")

    return 0

window = App()
window.mainloop()