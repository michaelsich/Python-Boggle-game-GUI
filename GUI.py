from tkinter import *
from PIL import Image

# window properties
WIDTH       = 800      # window width in pixels
HEIGHT      = 500      # window height in pixels

# font settings
H1_FONT     = ("arial", 16, "bold")
BUTTON_FONT = ("arial", 14)
MAIN_FONT   = ("arial", 12)

# images
LOGO = "Resources\\logo.jpg"

# styles
BTN_WIDTH   = 30
BTN_HEIGHT  = 1




class Graphics:
    """GUI of game buggle"""
    def __init__(self):
        self.__root = self.init_main_window()
        # self.create_main_frame()
        self.create_game_frame()
        self.__root.mainloop()

    def init_main_window(self):
        """ Creates and returns instance of Tk"""
        gui_main = Tk()
        gui_main.geometry(f"{WIDTH}x{HEIGHT}")
        gui_main.title("HUJI Boggle")
        return gui_main

    def create_main_frame(self):
        self.__main_frame = Frame(self.__root).pack()
        # logo
        # TODO: check how others imported images
        # logo_img = ImageTk.PhotoImage(Image.open(LOGO))
        # logo = Label(gui_main, image=logo_img).pack()

        # labels
        main_menu_instruction = Label(self.__main_frame,
                                  text="Welcome! press on start to get youre daily dose of boggle",
                                  font=H1_FONT).pack()
        # buttons
        start_button = Button(self.__main_frame, text="Start!",
                          height=BTN_HEIGHT, width=BTN_WIDTH,
                          bg="green", fg="white", relief="solid",
                          font=BUTTON_FONT,
                          command=self.on_start_click_event).pack()
        # start_button.place(x=150, y=200)

        quit_button = Button(self.__main_frame, text="Quit!",
                         height=BTN_HEIGHT, width=BTN_WIDTH,
                         bg="dark red", fg="white", relief="solid",
                         font=BUTTON_FONT,
                         command=self.on_start_click_event).pack()

    def create_game_frame(self):
        """Creates the frame of the game"""
        
        debug_style = {"highlightbackground":"green",
                    "highlightcolor":"green",
                    "highlightthickness":1,
                    "width":100,
                    "height":100,
                    "bd": 0}
        
        
        
        self.__game_frame = Frame(debug_style).pack()
        score_frame = Frame(self.__game_frame).pack()
        score_label = Label(score_frame, text="Score:").pack()
        
        
    # region EVENTS
    def on_start_click_event():
        """Event handler for start button click"""
        pass

    def on_quit_click_event():
        """Event handler for quit button click"""
        pass
    # endregion EVENTS


if __name__ == "__main__":
    gui = Graphics()