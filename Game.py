import boggle_board_randomizer

FILENAME = 'boggle_dict.txt'
MATRIX_SIZE = 4
INITIAL_SCORE = 0
TIME = 0


class Game:

    def __init__(self):
        self.matrix = boggle_board_randomizer.randomize_board()
        self.score = INITIAL_SCORE
        self.time = TIME
        self.all_words = {}
        self.wrong_words = []
        self.correct_words = []
        self.current_message = ''

    def get_matrix(self):
        return self.matrix

    def get_score(self):
        return self.score

    def get_time(self):
        return self.time

    def get_all_words(self):
        return self.all_words

    def get_wrong_words(self):
        return self.wrong_words

    def get_correct_words(self):
        return self.correct_words

    def get_current_message(self):
        return self.current_message

    def set_score(self, new_score):
        self.score = new_score

    def set_time(self, new_time):
        self.time = new_time

    def set_all_words(self):
        file = open(FILENAME, 'r')
        words_dict = {}
        for word in file:
            word = word.replace('\n', '')
            if word[0] not in words_dict:
                words_dict[word[0]] = [word]
            else:
                words_dict[word[0]].append(word)
        self.all_words = words_dict

    def update_wrong_words(self, wrong_word):
        self.wrong_words.append(wrong_word)

    def update_correct_words(self, correct_word):
        self.correct_words.append(correct_word)

    def was_word_checked(self, word):
        if word in self.wrong_words or word in self.correct_words:
            return True
        return False

    def is_word_in_dict(self, word):
        if word[0] in self.all_words:
            if word in self.all_words[word[0]]:
                return True
        return False

    def set_current_message(self, new_message):
        self.current_message = new_message
