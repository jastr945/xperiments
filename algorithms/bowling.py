# This is a Python module that implements a Game class scoring a game of bowling

class Game():
    """A Class representing a game with two ways of calculating the score"""
    def __init__(self, result_string):
        self.result_string = result_string

    def get_score(self):
        """Calculating the score given the entire string of results (assuming the game is finished)"""
        # input validation
        if len(self.result_string) < 12 or len(self.result_string) > 21:
            result = "Invalid input. The string should contain between 12 and 21 characters."
        if type(self.result_string)!=str:
            result = "Invalid input. Please enter the final score as a string (eg.'X7/729/XXX236/7/3')"

        total_result = 0
        open_frame = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for index, i in enumerate(self.result_string): # getting the index of every character in a string
            current_index = index
            if current_index <= (len(self.result_string) - 2):
                next_score = self.result_string[current_index + 1]
            if current_index <= (len(self.result_string) - 3):
                second_next_score = self.result_string[current_index + 2]
            if current_index > 0:
                previous_score = self.result_string[current_index - 1]

            single_frame_result = 0

            if i == "/":
                single_frame_result += 0

            if i == "X":
                if current_index < (len(self.result_string) - 3):
                    if next_score == "X" and second_next_score == "X":
                        i = 30
                    if next_score == "X" and second_next_score in open_frame:
                        i = (20 + int(second_next_score))
                    if next_score in open_frame and second_next_score == "X":
                        i = (int(next_score) + 20)
                    if next_score in open_frame and second_next_score == "/":
                        i = 20
                    if next_score in open_frame and second_next_score in open_frame:
                        i = 10 + int(next_score) + int(second_next_score)
                if current_index == (len(self.result_string) - 2):
                    if next_score == "X":
                        i = 20
                    else:
                        i = 10 + int(next_score)
                if current_index == (len(self.result_string) - 1):
                    i = 10
                single_frame_result += int(i)

            if i in open_frame:
                if current_index <= (len(self.result_string) - 3) and next_score == "/":
                    if second_next_score == "X":
                        i = 20
                    else:
                        i = 10 + int(second_next_score)
                if current_index == (len(self.result_string) - 1) and previous_score == "/":
                    i = int(i)
                i = int(i)
                single_frame_result += int(i)

            total_result += single_frame_result
            # print(single_frame_result, total_result)


        return total_result


# g = Game("XXXXXXXXXXXX") # 300
# print(g.get_score())

g = Game("90909090909090909090") # 90 works
print(g.get_score())

#
# g = Game("5/5/5/5/5/5/5/5/5/5/5") # 150
# print(g.get_score())
#
# g = Game("X7/729/XXX236/7/3") # 168
# print(g.get_score())
#
# g = Game("00000000000000000000") # 0 works
# print(g.get_score())
# #
# g = Game('01273/X5/7/345400X70') # 113 works
# print(g.get_score())
#
# g = Game('X7/90X088/06XXX81') # 167 works
# print(g.get_score())
