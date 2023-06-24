import customtkinter

from PIL import Image
from tkinter import END

from cache.app import calculate

app = customtkinter.CTk()

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
        
app.title('CalculApp')

app.geometry('350x500')
app.resizable(False, False)

title_image = customtkinter.CTkImage(Image.open("assets/icons/CustomTkinter_icon_Windows.ico"),size=(30, 30))
title_font = customtkinter.CTkFont(family='Roboto', size= 30, weight='bold')
title = customtkinter.CTkLabel(master=app, width=350, height=75, text=' CalculApp', font=title_font,
                                        image=title_image, compound='left')
title.grid()
        
textbox = customtkinter.CTkTextbox(master=app, width=250, height=250, activate_scrollbars=False)
textbox.grid()

def action_button():
        arg1 = textbox.get("1.0", END)
        calculate(arg1)

button_font = customtkinter.CTkFont(family='Roboto', size=15)
button = customtkinter.CTkButton(master=app, height=25, width=150, text="Entrer", font=button_font, command=action_button)
button.grid(pady=35)

text = customtkinter.CTkLabel(master=app, height=20, width= 350, text='Résultat', fg_color='#585858')
text.grid(pady=60)

app.mainloop()