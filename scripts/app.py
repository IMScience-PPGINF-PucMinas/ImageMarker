import customtkinter as ctk
from enum import Enum
from .frames.file_selection_frame import FileSelectionFrame
from .frames.user_level_selection_frame import UserLevelSelectionFrame
from .frames.image_frame import ImageFrame

class Frames(Enum):
    USER_LEVEL_SELECTION_FRAME = 'UserSelectionFrame'
    FILE_SELECTION_FRAME = 'FileSelectionFrame'
    IMAGE_FRAME = 'ImageFrame'
    
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Image Marker")
        self._config_window(width = 1200,height = 600)
        self._current_frame = None
        self._image = None
        self._current_frame_name = ""
        self._load_next_frame()
        
        self.__next_frame_dict = {
            Frames.USER_LEVEL_SELECTION_FRAME:Frames.FILE_SELECTION_FRAME,
            Frames.FILE_SELECTION_FRAME:Frames.IMAGE_FRAME
        }

    @property
    def project_name(self):
        return self.__project_name
    
    @project_name.setter
    def set_project_name(self, new_name: str):
        self.__project_name = new_name
        
    def _config_window(self, width: int, height: int):
        """ Sets up the width, the height and the centering of the window app."""
        self.width = width
        self.height = height
        self.geometry(f"{width}x{height}")
        self._center_window()

    def _center_window(self):
        """ Places the window on the center of the screen."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width/2) - (self.width/2)
        y = (screen_height/2) - (self.height/2)
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y-50)) 
   
    def _load_next_frame(self): 
        """ Destroys the current frame and calls the next one."""
        try:
            if self._current_frame_name == "":
                self._clear_frame()
                self._load_user_level_selection_frame()
            elif self._current_frame_name == Frames.FILE_SELECTION_FRAME.value:
                self._clear_frame()
                self._load_image_frame()
            elif self._current_frame_name == Frames.USER_LEVEL_SELECTION_FRAME.value:
                self._user_level = self._current_frame.user_level
                self._clear_frame()
                self._load_file_selection_frame()
            else:
                raise Exception('Invalid frame selection')
        except Exception as e:
            print('An exception has ocurred:', e)
             
    def _clear_frame(self):
        """ Destroys the current frame."""
        if self._current_frame is not None:
            self._current_frame.destroy()
    
    def _load_file_selection_frame(self):
        """ Renders the file selection frame."""
        self._file_selection_frame = FileSelectionFrame(parent = self)
        self._current_frame = self._file_selection_frame
        self._current_frame_name = Frames.FILE_SELECTION_FRAME.value
        self._file_selection_frame.pack(fill=ctk.BOTH, expand=True)
    
    def _load_user_level_selection_frame(self):
        """ Renders the user level selection frame.""" 
        self._user_level_selection_frame = UserLevelSelectionFrame(parent = self)
        self._current_frame = self._user_level_selection_frame
        self._current_frame_name = Frames.USER_LEVEL_SELECTION_FRAME.value
        self._user_level_selection_frame.pack(fill=ctk.BOTH, expand=True)
        
    def _load_image_frame(self):
        self._clear_frame()
        """ Renders the image labelling frame."""
        self._image_frame = ImageFrame(parent = self, image=self._image)
        self._current_frame = self._image_frame
        self._image_frame.pack(fill=ctk.BOTH, expand=True)