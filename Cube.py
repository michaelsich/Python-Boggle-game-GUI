
DEFAULT_BG = 'Resources\\letter_bg2.png'
SELECTED_BG = 'Resources\\selected_bg2.png'

class Cube:

    def __init__(self, letter):
        self.__letter = letter
        self.__selected = False
        self.__background = DEFAULT_BG

    def get_letter(self):
        return self.__letter

    def is_selected(self):
        return self.__selected

    def get_background(self):
        return self.__background

    def set_background(self, selected = False):
        if selected:
            self.__background = SELECTED_BG
        else:
            self.__background = DEFAULT_BG
        return None
