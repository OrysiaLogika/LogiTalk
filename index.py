from customtkinter import  *

class Messi(CTk):
    def __init__ (self):
        super().__init__()
        self.geometry('400x300')

        self.frame = CTkFrame(self, width=200, height=self.winfo_height())
        self.frame.pack_propagate(False)
        self.frame.configure(width=0)
        self.frame.place(x=0, y=0)
        self.is_show_menu = False
        self.frame_width = 0
        
        self.label = CTklabel(self, frame, text='ВАше імя')
        self.label.pack(pady=30)
        self.entry = CTkEntry(self.frame)
        self.entry.pack()                           
        self.label.theme  = CTkOptionMenu(self.frame, values=['dark','bright'],comand=self.change_theme)
        self.label_theme.pack(side='bottom',pady=20)
        self.them = None
        self.btn = CTkButton(self, text='>'.toggle_show_menu, width=30)
        self.btn.place(x=0,y=0)
        self.menu_show_speed = 20
        
        self.chat_text =CTkTextbox(self,state='disable')
        self.chat_text.place(x=0,y=30)
