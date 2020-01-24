from tkinter import *
import Cube

# window properties
WIDTH       = 800      # window width in pixels
HEIGHT      = 500      # window height in pixels

# font settings
H1_FONT     = ("arial", 16, "bold")
BUTTON_FONT = ("arial", 14)
MAIN_FONT   = ("arial", 12)
CUBE_FONT   = ("david", 12)
TXT_BOX_FONT= ("david", 13)

# images
LOGO        = "Resources\\logo.png"


# styles
BTN_WIDTH   = 30
BTN_HEIGHT  = 1

class Graphics:
    """GUI of game buggle"""
    def __init__(self, letters):
        self.__letters = letters
        self.__root = self.init_main_window()
        self.frames = {}

        self.create_main_frame()
        self.create_game_frame()

        self.__root.mainloop()

    def init_main_window(self):
        """ Creates and returns instance of Tk"""
        gui_main = Tk()
        gui_main.geometry(f"{WIDTH}x{HEIGHT}")
        gui_main.resizable(width=False, height=False)
        gui_main.title("HUJI Boggle")
        return gui_main

    def create_main_frame(self):
        main_frame = Frame(self.__root)
        self.frames["main"] = main_frame

        # logo
        logo_img = PhotoImage(file=LOGO)
        logo = Label(main_frame, image=logo_img)
        logo.image = logo_img

        # labels
        main_menu_instruction = Label(main_frame,
                                  text="Welcome! press on start to get youre daily dose of boggle",
                                  font=H1_FONT)
        # buttons
        start_button = Button(main_frame, text="Start!",
                          height=BTN_HEIGHT, width=BTN_WIDTH,
                          bg="green", fg="white", relief="solid",
                          font=BUTTON_FONT,
                          command=self.on_start_click_event)

        quit_button = Button(main_frame, text="Quit!",
                         height=BTN_HEIGHT, width=BTN_WIDTH,
                         bg="dark red", fg="white", relief="solid",
                         font=BUTTON_FONT,
                         command=self.on_quit_click_event)

        # pack all objects
        main_frame.grid(row=0, column=0, rowspan=3 ,sticky='news', ipadx=100)
        logo.pack()
        main_menu_instruction.pack()
        start_button.pack()
        quit_button.pack()

    def create_game_frame(self):
        """Creates the frame of the game"""
        #TODO: delete debug frame
        debug_style = {"highlightbackground":"green",
                    "highlightcolor":"green",
                    "highlightthickness":1,
                    "width":100,
                    "height":100,
                    "bd": 0}

        game_frame = Frame(self.__root, **debug_style)
        self.frames["game"] = game_frame
        left_frame = Frame(game_frame, **debug_style)
        right_frame = Frame(game_frame, **debug_style)

        # board
        self.__create_game_board(left_frame)

        # time
        time_frame = Frame(right_frame, **debug_style)
        # TODO: add time support
        time_label = Label(time_frame, text="time here")

        # score
        score_frame = Frame(right_frame, **debug_style)
        score_label = Label(score_frame, text="Score:")

        # textbox
        words_frame = Frame(right_frame, **debug_style)
        words_box   = Text(words_frame, state="disabled",
                           cursor="pirate", relief="groove", bg='light grey',
                           width=20, font=TXT_BOX_FONT)

        # packing objects
        game_frame.grid(row=0, column=0, rowspan=3, sticky='news')
        left_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nse')
        right_frame.grid(row=0, column=2, padx=10, pady=10, sticky='nsw')
        score_frame.pack()
        score_label.pack()
        time_frame.pack()
        time_label.pack()
        words_frame.pack(fill=Y)
        words_box.pack()

    def __create_game_board(self, frame):

        # create image objects for canvas
        bg_img = self.__letters[0][0].get_background()
        img = PhotoImage(file=bg_img)

        # create a canvas
        canvas = Canvas(frame,height=450, width=500, bg="white")

        # TODO: find out why cant see background image
        for row in range(len(self.__letters)):
            curr_letters = self.__letters[row]
            for col in range(len(curr_letters)):
                pos_x = row*110+60
                pos_y = col*110+60
                image = canvas.create_image(pos_x, pos_y, image=img)
                canvas.background = img
                canvas.create_text(pos_x, pos_y, fill="darkblue", font="Times 20 italic bold",
                                        text=curr_letters[col].get_letter())
        canvas.pack()



    # region EVENTS
    def on_start_click_event(self):
        """Event handler for start button click"""
        self.frames["game"].tkraise()

    def on_quit_click_event(self):
        """Event handler for quit button click"""
        pass
    # endregion EVENTS


if __name__ == "__main__":
    lst = [[],[],[],[]]
    for let in ['a','b','c','k']:
        cubbe = Cube.Cube(let)
        lst[0].append(cubbe)

    for let in ['e','f','g','k']:
        cubbe = Cube.Cube(let)
        lst[1].append(cubbe)

    for let in ['e','f','g','k']:
        cubbe = Cube.Cube(let)
        lst[2].append(cubbe)

    for let in ['e','f','g','k']:
        cubbe = Cube.Cube(let)
        lst[3].append(cubbe)

    gui = Graphics(lst)