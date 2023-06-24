import customtkinter
from PIL import Image
from tkinter import END
import statistics

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('CalculApp')
        self.iconbitmap('assets/icons/CalculApp_icon_Windows.ico')
        self.geometry('350x500')
        self.resizable(False, False)

        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')

        title_image = customtkinter.CTkImage(Image.open('assets/icons/CalculApp_icon_Windows.ico'), size=(30, 30))
        title_font = customtkinter.CTkFont(family='Roboto', size=30, weight='bold')
        title_label = customtkinter.CTkLabel(master=self, width=350, height=75, text=' CalculApp', font=title_font, image=title_image, compound='left')
        title_label.grid()

        textbox = customtkinter.CTkTextbox(master=self, width=250, height=300, activate_scrollbars=False)
        textbox.grid()

        with open('window/cache/data.dat', 'r') as file:
            content = file.read()
        textbox.insert(END, content)

        check_var = customtkinter.StringVar(value="on")
        checkbox_font = customtkinter.CTkFont(family='Roboto', size=12)
        checkbox = customtkinter.CTkCheckBox(master=self, height=40, width=150, text='Sauvegarder les informations', font=checkbox_font, variable=check_var, onvalue="on", offvalue="off", checkbox_width=20, checkbox_height=20, corner_radius=5, border_width=1)
        checkbox.grid()

        button_font = customtkinter.CTkFont(family='Roboto', size=15)
        button = customtkinter.CTkButton(master=self, height=25, width=150, text="Entrer", font=button_font, command=lambda: action_button(self))
        button.grid(pady=20)

        text_label = customtkinter.CTkLabel(master=self, height=20, width=350, text='Résultat', fg_color='transparent')
        text_label.grid()

        self.textbox = textbox
        self.text_label = text_label
        self.check_var = check_var

def action_button(self):
    arg1 = self.textbox.get("1.0", END)
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
        self.text_label.configure(text=result)
    else:
        self.text_label.configure(text="Aucune donnée disponible")

    if self.check_var.get() == "on":
        with open('window/cache/data.dat', 'w') as file:
            file.write(' '.join(map(str, numbers)))

    return numbers

window = App()
window.mainloop()