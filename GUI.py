from tkinter import *
import Cube

# window properties
WIDTH       = 700      # window width in pixels
HEIGHT      = 500      # window height in pixels

# font settings
H1_FONT     = ("arial", 16, "bold")
BUTTON_FONT = ("arial", 14)
MAIN_FONT   = ("arial", 12, "bold")
CUBE_FONT   = ("david", 36, "bold")
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

        # game elements
        self.__game_cubes = []
        self.__elements = {
            "canvas"    : "",
            "textbox"   : "",
            "time"      : "",
            "score"     : ""
        }

        # create frames
        self.create_main_frame()
        self.create_game_frame()

        self.__root.mainloop()

    def init_main_window(self):
        """ Creates and returns instance of Tk"""
        gui_main = Tk()
        gui_main.geometry(f"{WIDTH}x{HEIGHT}")
        gui_main.resizable(width=False, height=False)
        gui_main.title("HUJI Boggle!")
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
        time_label = Label(time_frame, text="time here", font=MAIN_FONT)
        self.__elements["time"] = time_label

        # score
        score_frame = Frame(right_frame, **debug_style)
        score_label = Label(score_frame, text="Score:", font=MAIN_FONT)
        self.__elements["score"] = score_label

        # textbox
        words_frame = Frame(right_frame, **debug_style)
        words_box   = Text(words_frame, state="disabled", cursor="pirate",
                           relief="groove", bg='light grey', spacing1=10,
                           width=20, height=14, padx=10, font=TXT_BOX_FONT)
        self.__elements["textbox"] = words_box

        # quit button
        quit_button = Button(right_frame, text="Quit",
                             bg="dark red", fg="white", relief="solid",
                             font=BUTTON_FONT,
                             command=self.on_quit_click_event)

        # packing objects
        game_frame.grid(row=0, column=0, rowspan=3, sticky='news')
        left_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nse')
        right_frame.grid(row=0, column=2, padx=10, pady=10, sticky='nsw')
        time_frame.pack(fill=X)
        time_label.pack()
        score_frame.pack(fill=X)
        score_label.pack(side=LEFT)
        words_frame.pack(fill=Y)
        words_box.pack()
        quit_button.pack(fill=X)

    def __create_game_board(self, frame):
        """ Creates a canvas with cubes in the given frame """
        # create image objects for canvas
        bg_img = self.__letters[0][0].get_background()
        img = PhotoImage(file=bg_img)

        # create a canvas
        canvas = Canvas(frame, height=450, width=450, bg="dark blue")
        canvas.config(scrollregion=canvas.bbox(ALL))

        # fill cubes ( pic + letter )
        for row in range(len(self.__letters)):
            curr_letters = self.__letters[row]
            for col in range(len(curr_letters)):
                pos_x = row*110+60
                pos_y = col*110+60

                # create cube
                image = canvas.create_image(pos_y, pos_x, image=img, command=self.on_start_click_event())
                canvas.background = img
                canvas.create_text(pos_y, pos_x, fill="darkblue", font=CUBE_FONT,
                                   text=curr_letters[col].get_letter())
                self.__game_cubes.append(image)

                # create event handling
                # TODO: configure how to change background
                canvas.tag_bind(image, '<ButtonPress-1>',
                                lambda event, arg=image: self.on_cube_click_event(event, arg))

        self.__elements["canvas"] = canvas
        canvas.pack()

    # region EVENTS
    def on_start_click_event(self):
        """Event handler for start button click"""
        self.frames["game"].tkraise()

    def on_quit_click_event(self):
        """Event handler for quit button click"""
        # TODO: add message box first
        self.__root.destroy()

    def on_cube_click_event(self, event, index):
        self.add_word_to_box("abc\n")
        print(index)

    # endregion EVENTS

    # region SETTERS
    def add_word_to_box(self, word):
        """ Gets a word and adds it to the text box """
        self.__elements["textbox"].config(state=NORMAL)
        self.__elements["textbox"].insert(0.0, word)
        self.__elements["textbox"].config(state=DISABLED)

    def set_time(self, new_time):
        """ updates the game time """
        self.__elements["time"].config(text=new_time)

    def set_score(self, new_score):
        """ updates the game time """
        self.__elements["score"].config(text=new_score)

    # endregion SETTERS



if __name__ == "__main__":
    lst = [[],[],[],[]]
    for let in ['a','b','c','k']:
        cubbe = Cube.Cube(let)
        lst[0].append(cubbe)

    for let in ['e','f','Qe','k']:
        cubbe = Cube.Cube(let)
        lst[1].append(cubbe)

    for let in ['e','f','g','k']:
        cubbe = Cube.Cube(let)
        lst[2].append(cubbe)

    for let in ['e','f','g','k']:
        cubbe = Cube.Cube(let)
        lst[3].append(cubbe)

    gui = Graphics(lst)
