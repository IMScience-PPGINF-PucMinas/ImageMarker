import customtkinter as ctk
from tkinter import messagebox  
from enum import Enum

class UserLevel(Enum):
    LEVEL1 = 'Level 1'
    LEVEL2 = 'Level 2'
    LEVEL3 = 'Level 3'

class UserLevelSelectionFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.parent = parent
        self.__user_level = "" 
        self._user_level_label = ctk.CTkLabel(master = self, text='Choose the user level.')
        self._option_menu = ctk.CTkOptionMenu(
            master=self,
            values=[UserLevel.LEVEL1.value, UserLevel.LEVEL2.value, UserLevel.LEVEL3.value],
        )

        self._select_image_btn = ctk.CTkButton(
            master = self, 
            text = "Submit",
            command=self._call_next_frame
        )

        self._user_level_label.pack(anchor = "center", pady = (100, 10))
        self._option_menu.pack(anchor = "center", pady=10)
        self._select_image_btn.pack(anchor = "center")

    @property
    def user_level(self):
        return self.__user_level      
    
    @user_level.setter
    def set_user_level(self, new_user_level):
        self.__user_level = new_user_level
    
    def _call_next_frame(self):
        """ Validates the user_level and calls the next frame."""
        self.__user_level = self._option_menu.get()
        if self.__user_level:
            answer = messagebox.askquestion('User level confirmation', f'You choose {self.__user_level}. Do you confirm that?')
            if answer == 'yes':
                self.parent._load_next_frame()
        else:
            messagebox.showerror(
                'User type error.', "Please select a valid user type!")