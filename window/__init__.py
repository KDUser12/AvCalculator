import customtkinter
from tkinter import *

from PIL import Image

class Window(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')
    
        self.title('CalculApp')

        self.geometry('350x500')
        self.resizable(False, False)

        title_image = customtkinter.CTkImage(Image.open("assets/icons/CustomTkinter_icon_Windows.ico"),size=(30, 30))
        title_font = customtkinter.CTkFont(family='Roboto', size= 30, weight='bold')
        title = customtkinter.CTkLabel(master=self, width=350, height=75, text=' CalculApp', font=title_font,
                                       image=title_image, compound='left')
        title.grid()

        textbox = customtkinter.CTkTextbox(master=self, width=250, height=250, activate_scrollbars=False)
        textbox.grid()

        check_var = customtkinter.StringVar(value="on")
        checkbox_font = customtkinter.CTkFont(family='Roboto', size=12)
        checkbox = customtkinter.CTkCheckBox(master=self, height=40, width=150, text='Sauvegarder les informations', font=checkbox_font,
                                             variable=check_var, onvalue="on", offvalue="off", checkbox_width=20, checkbox_height=20, corner_radius=5, border_width=1)
        checkbox.grid()

        button_font = customtkinter.CTkFont(family='Roboto', size=15)
        button = customtkinter.CTkButton(master=self, height=25, width=150, text="Entrer", font=button_font)
        button.grid(pady=35)

        text = customtkinter.CTkLabel(master=self, height=20, width= 350, text='Résultat', fg_color='#585858')
        text.grid(pady=20)



app = Window()
app.mainloop()