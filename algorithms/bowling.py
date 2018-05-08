# 05/07/2018 Polina Jastrzebska
# This is a Python module that implements a Game class scoring a game of bowling.
# If the game is over, run analyze_total() method with your full string of results as an input.
# For incoming results in real time, run analyze_single_result().


import unittest
from unittest import TestCase, mock


class Game():
    """A Class representing a game with two ways of calculating the score."""
    def __init__(self, total=""):
        self.total = ""

    def analyze_single_result(self):
        """Analyzes user's input in REAL TIME and returns the running score."""
        frame = 1
        open_frame = False  # to determine where each frame starts and ends
        allowed_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "x", "X"]  # input validation reference
        while True:
            if frame < 11:
                get_result = (input("Enter result: ")).upper()
                if get_result not in allowed_chars:
                    print("Invalid input. Try again.")
                else:
                    self.total += str(get_result)
                    if frame == 10 and get_result == "X":  # additional throws in the 10th frame
                        get_result1 = (input("Additional throw 1: ")).upper()
                        self.total += str(get_result1)
                        get_result2 = (input("Additional throw 2: ")).upper()
                        self.total += str(get_result2)
                    if frame == 10 and get_result == "/":
                        get_result1 = (input("Additional throw 1: ")).upper()
                        self.total += str(get_result1)
                        frame_change = 1
                    else:
                        if get_result == "X":
                            throw = "strike, at least 10"
                            frame_change = 1
                        elif get_result == "/":
                            throw = "spare, at least 10"
                            frame_change = 1
                            open_frame = False
                        else:
                            if open_frame is False:
                                throw = str(get_result)
                                frame_change = 0
                                open_frame = True
                            else:
                                throw = str(get_result)
                                frame_change = 1
                                open_frame = False
                print("Frame: {}. The value of this throw is: {}, your current total score: is {}".format(frame, throw, self.analyze_total(self.total)))
                frame += frame_change
            else:
                return "Game over. Your total score is: {}.".format(self.analyze_total(self.total))

    def analyze_total(self, current_str):
        """Calculating the score given the entire string of results (either in real time, or when the game is complete."""
        # input validation
        if type(current_str) != str:
            total_result = "Invalid input. String of characters expected."
        else:
            total_result = 0
            open_frame = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

            for index, i in enumerate(current_str):  # accessing the index of every character in a string
                current_index = index
                if current_index < (len(current_str) - 1):
                    next_score = current_str[current_index + 1]
                if current_index < (len(current_str) - 2):
                    second_next_score = current_str[current_index + 2]
                if current_index > 0:
                    previous_score = current_str[current_index - 1]
                single_frame_result = 0

                if i == "/":
                    single_frame_result += 0

                if i == "X":
                    if current_index == (len(current_str) - 3):
                        if next_score == "X" and second_next_score == "X":
                            i = 30
                        elif next_score in open_frame and second_next_score in open_frame:
                            i = 10
                        elif next_score in open_frame and second_next_score == "/":
                            i = 20
                        elif next_score == "X" and second_next_score in open_frame or next_score in open_frame and second_next_score == "X":
                            i = 10
                    elif current_index < (len(current_str) - 3):
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
                    if current_index < (len(current_str) - 2) and next_score == "/":
                        if second_next_score == "X":
                            i = 20
                        else:
                            i = 10 + int(second_next_score)
                    elif current_index == (len(current_str) - 2) and next_score == "/":
                        i = 10
                    elif current_index > 0 and current_index == (len(current_str) - 1) and previous_score == "/":
                        i = 0
                    else:
                        i = int(i)
                    single_frame_result += int(i)

                total_result += single_frame_result

        return total_result


class GameTest(TestCase):

    # input string and expected output
    data = [
        ('XXXXXXXXXXXX', 300),
        ('90909090909090909090', 90),
        ('5/5/5/5/5/5/5/5/5/5/5', 150),
        ('X7/729/XXX236/7/3', 168),
        ('00000000000000000000', 0),
        ('01273/X5/7/345400X70', 113),
        ('X7/90X088/06XXX81', 167),
        (True, "Invalid input. String of characters expected."),  # testing for a different data type
        ]

    def test_analyze_total(self):
        for str_, expected_output in self.data:
            instance = Game()
            result = instance.analyze_total(str_)
            self.assertEqual(result, expected_output)

    @mock.patch('builtins.input')
    def test_analyze_single_result(self, mock_input):
        for str_, expected_output in self.data[:-1]:
            mock_input.side_effect = str_
            instance = Game()
            result = instance.analyze_single_result()
            self.assertEqual(result, "Game over. Your total score is: {}.".format(expected_output))


if __name__ == "__main__":
    unittest.main()
