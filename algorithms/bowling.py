# This is a Python module that implements a Game class scoring a game of bowling
import unittest


class Game():
    """A Class representing a game with two ways of calculating the score"""
    def __init__(self, result_string):
        self.result_string = result_string

    def get_score(self):
        """Calculating the score given the entire string of results (assuming the game is finished)"""
        # input validation
        if type(self.result_string) != str:
            total_result = "Invalid input. String of characters expected."
        elif len(self.result_string) < 12 or len(self.result_string) > 21:
            total_result = "Invalid input. The string should contain between 12 and 21 characters."
        else:
            total_result = 0
            open_frame = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for index, i in enumerate(self.result_string): # getting the index of every character in a string
                if i != "X" and i != "/" and i not in open_frame:
                    total_result = "Invalid input. The string should only contain 'X', '/' and 0-9."
                else:
                    current_index = index
                    if current_index < (len(self.result_string) - 1):
                        next_score = self.result_string[current_index + 1]
                    if current_index < (len(self.result_string) - 2):
                        second_next_score = self.result_string[current_index + 2]
                    if current_index > 0:
                        previous_score = self.result_string[current_index - 1]
                    single_frame_result = 0
                    if i == "/":
                        single_frame_result += 0
                    if i == "X":
                        if current_index == (len(self.result_string) - 3):
                            if next_score == "X" and second_next_score == "X":
                                i = 30
                            elif next_score in open_frame and second_next_score in open_frame:
                                i = 10
                            elif next_score in open_frame and second_next_score == "/":
                                i = 20
                            elif next_score == "X" and second_next_score in open_frame or next_score in open_frame and second_next_score == "X":
                                i = 10
                        elif current_index < (len(self.result_string) - 3):
                            if next_score == "X" and second_next_score == "X":
                                i = 30
                            elif next_score == "X" and second_next_score in open_frame or next_score in open_frame and second_next_score == "X":
                                i = (20 + int(second_next_score))
                            elif next_score in open_frame and second_next_score == "/":
                                i = 20
                            elif next_score in open_frame and second_next_score in open_frame:
                                i = 10 + int(next_score) + int(second_next_score)
                        else:
                            i = 0
                        single_frame_result += int(i)
                    if i in open_frame:
                        if current_index < (len(self.result_string) - 2) and next_score == "/":
                            if second_next_score == "X":
                                i = 20
                            else:
                                i = 10 + int(second_next_score)
                        elif current_index == (len(self.result_string) - 2) and next_score == "/":
                            i = 10
                        elif current_index == (len(self.result_string) - 1) and previous_score == "/":
                            i = 0
                        else:
                            i = int(i)
                        single_frame_result += int(i)
                    total_result += single_frame_result
        return total_result


class GameTest(unittest.TestCase):
    # input string and expected output
    data = [
        ('XXXXXXXXXXXX', 300),
        ('90909090909090909090', 90),
        ('5/5/5/5/5/5/5/5/5/5/5', 150),
        ('X7/729/XXX236/7/3', 168),
        ('00000000000000000000', 0),
        ('01273/X5/7/345400X70', 113),
        ('X7/90X088/06XXX81', 167),
        ('5464', "Invalid input. The string should contain between 12 and 21 characters."),
        (True, "Invalid input. String of characters expected.") # testing for another data type
        ]

    def test_multiple_results(self):
        for str_, expected_output in self.data:
            instance = Game(str_)
            result1 = instance.get_score()
            self.assertEqual(result1, expected_output)


if __name__ == "__main__":
    unittest.main()
