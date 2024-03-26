import customtkinter as ctk
from ..utils.file_manager import read_file_path
from ..utils.file_manager import open_image

class FileSelectionFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.parent = parent
        self._select_image_btn = ctk.CTkButton(
            master = self, 
            text = "Load Image",
            command=self._call_image_frame
        )

        self._select_image_btn.place(relx=0.5, rely=0.5, anchor="center")
        
    def _call_image_frame(self):
        """ Calls the parent frame loader if the image is valid. """
        filepath = read_file_path()
        image = open_image(filepath)
        if image is not None:
            self.parent._image = image
            self.parent._load_next_frame()
