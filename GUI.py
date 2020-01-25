from tkinter import *
import Cube

# window properties
WIDTH       = 685      # window width in pixels
HEIGHT      = 490      # window height in pixels

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
BG_COLOR = "#142752"

# GENERAL verifies and TODO s
# TODO: word cant be scored twice (even with diffrent path)
# TODO: try to split board manager
# TODO: default time is set to 3:00 mins
# TODO: score is reseting in each game ( not mendatory )
# TODO: can start another game at the end ( message )


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
            "score"     : "",
            "pics"      : []
        }

        # create frames
        self.create_game_frame()
        self.create_main_frame()

        self.__root.mainloop()

    def init_main_window(self):
        """ Creates and returns instance of Tk"""
        gui_main = Tk()
        gui_main.geometry(f"{WIDTH}x{HEIGHT}")
        gui_main.resizable(width=False, height=False)
        gui_main.title("HUJI Boggle!")
        gui_main.configure(background=BG_COLOR)
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
                                  text="Welcome!\nPress 'start!' to get your daily dose of boggle",
                                  font=H1_FONT)
        # buttons
        start_button = Button(main_frame, text="Start!",
                              height=BTN_HEIGHT, width=BTN_WIDTH,
                              bg="green", fg="white", relief="solid",
                              font=BUTTON_FONT,
                              command=self.__on_start_click_event)

        quit_button = Button(main_frame, text="Quit!",
                             height=BTN_HEIGHT, width=BTN_WIDTH,
                             bg="dark red", fg="white", relief="solid",
                             font=BUTTON_FONT,
                             command=self.__on_quit_click_event)

        # pack all objects
        main_frame.grid(row=0, column=0, rowspan=50 ,sticky='news', ipadx=100)
        logo.pack()
        main_menu_instruction.pack()
        start_button.pack()
        quit_button.pack()

    def create_game_frame(self):
        """Creates the frame of the game"""
        #TODO: delete debug frame
        debug_style = {"highlightbackground":"red",
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
        time_frame = Frame(right_frame, **debug_style,)
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
                             command=self.__on_quit_click_event)

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
        canvas = Canvas(frame, height=460, width=450, bg="dark blue")
        canvas.config(scrollregion=canvas.bbox(ALL))

        # fill cubes ( pic + letter )
        for row in range(len(self.__letters)):
            curr_letters = self.__letters[row]
            for col in range(len(curr_letters)):
                pos_x = row*110+65
                pos_y = col*110+62

                # create cube
                image = canvas.create_image(pos_y, pos_x, image=img)
                canvas.image = img  # reference to img(tk garbage collector)
                cube_letter = canvas.create_text(pos_y, pos_x,
                                                 font=CUBE_FONT,
                                                 text=curr_letters[col].get_letter())
                self.__game_cubes.append(image)

                # bind to event handler
                canvas.tag_bind(image, '<ButtonPress-1>',
                                lambda event, arg=image:
                                self.__on_cube_click_event(event, arg))
                canvas.tag_bind(cube_letter, '<ButtonPress-1>',
                                lambda event,
                                arg=image: self.__on_cube_click_event(event, arg))

        self.__elements["canvas"] = canvas
        canvas.pack()

    # region EVENTS
    def __on_start_click_event(self):
        """Event handler for start button click - raises game frame"""
        self.frames["game"].tkraise()

    def __on_quit_click_event(self):
        """Event handler for quit button click - closes window"""
        # TODO: add message box first
        self.__root.destroy()

    def __on_cube_click_event(self, event, index):
        """Changes status and bg pic of clicked item"""
        index_row = index // 8
        index_col = ((index - 8*index_row) - 1) // 2

        # already selected
        if not self.__select_cube(index_row, index_col):
            self.__unselect_cube(index_row, index_col)
        # change canvas item to selected
        self.__change_bg(index_row, index_col, index)
        # TODO: send letter to Game for word handling

    # endregion EVENTS

    # region SETTERS
    def add_word_to_box(self, word):
        """ Gets a word and adds it to the game's text box """
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

    def __select_cube(self, row, col):
        """changes cube's bg to selected, returns True upon success, False otherwise"""
        if self.__letters[row][col].is_selected():
            return False
        self.__letters[row][col].set_background(True)
        return True

    def __unselect_cube(self, row, col):
        """changes cube's bg to normal"""
        self.__letters[row][col].set_background(False)

    def __change_bg(self, row, col, index):
        """ changes the canvas' item at (index) to cube's background """
        bg_img = self.__letters[row][col].get_background()
        img = PhotoImage(file=bg_img)
        self.__elements["canvas"].itemconfig(index, image=img)
        self.__elements["pics"].append(img)


if __name__ == "__main__":
    lst = [[],[],[],[]]
    for let in ['a','b','c','k']:
        cubbe = Cube.Cube(let)
        lst[0].append(cubbe)

    for let in ['e','f','Qu','k']:
        cubbe = Cube.Cube(let)
        lst[1].append(cubbe)

    for let in ['e','f','g','k']:
        cubbe = Cube.Cube(let)
        lst[2].append(cubbe)

    for let in ['e','f','g','k']:
        cubbe = Cube.Cube(let)
        lst[3].append(cubbe)

    gui = Graphics(lst)
