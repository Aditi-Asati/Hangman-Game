"""
Rewrite of hangman_game.py
"""

import random


def get_fruits() -> list[str]:
    """
    Returns a list of fruit names.
    """
    with open("./fruits.txt", encoding="utf-8") as fruits:
        content = fruits.read().split()
        return content


class Hangman:
    """
    Base game class.
    """

    def __init__(self) -> None:
        self.fruit = random.choice(get_fruits())

        # positions_to_show is a list of indices of string self.fruit
        # which are going to be showed as hint, while rest of the
        # indices will be filled with underscores
        positions_to_show = self.decide_positions_to_show(self.fruit)

        # running a list comprehension which basically
        # includes indices of self.fruit which are in positions_to_show
        # and replaces rest of the characters with _
        self.fruit_with_blanks = [
            self.fruit[i] if i in positions_to_show else "_"
            for i in range(0, len(self.fruit))
        ]

		# determining the first _, i.e., the first position to guess
        self.position = self.fruit_with_blanks.index("_")
        self.chances = len(self.fruit)

    @staticmethod
    def decide_positions_to_show(fruit: str) -> list[int]:
        """
        Returns a list of indices to show.
        """
        length = len(fruit)
        number_of_positions = round(0.5 * length)

        if number_of_positions == length:
            number_of_positions -= 1

        indices = []
        for _ in range(number_of_positions):
            # length-1 cuz randint is inclusive
            idx = random.randint(0, length - 1)

			# while loop to ensure non duplicate index
            while idx in indices:
                idx = random.randint(0, length - 1)

            indices.append(idx)

        return indices

    def guess_next_char(self):
        """
        Interface for letting user guess next empty character.
        """
        print(" ".join(self.fruit_with_blanks))
        guess = input(f"Guess next({self.position + 1}th) character: ")
        if guess == self.fruit[self.position]:
            print("Correct guess!")
            
            # updating self.fruit_with_blanks
            self.fruit_with_blanks[self.position] = self.fruit[self.position]

            try:
                self.position = self.fruit_with_blanks.index("_")
            # passing except here because when game is finished,
            # there are no `_` present if self.fruit_with_blanks
            # and hence index method returns an error
            except Exception:
                pass

        else:
            print("Incorrect!")

        self.chances -= 1
        print(f"Remaining chances: {self.chances}")
        print("\n------------------------------\n")

    def play(self):
        """
        Main game loop.
        """
        print("Welcome to the Hangman game.")
        print(f"Total number of chances to guess the fruit name: {self.chances}.")
        print("\n-----------------------------------------\n")

        # run until there is an `_` present and chances are left
        while "_" in self.fruit_with_blanks and self.chances > 0:
            self.guess_next_char()

        if self.chances > 0:
            print("You won the game!")
        else:
            print("You lost the game!")

        print(f"The fruit name was `{self.fruit}`.")


if __name__ == "__main__":
    game = Hangman()
    game.play()
