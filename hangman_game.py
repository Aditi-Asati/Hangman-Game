# Hangman Game

import random
import time
from threading import Event
import concurrent.futures
from pynput.keyboard import Key, Controller


class Hangman:
    """
    Randomly chooses a fruit from the fruits list and decides
    the number of attempts based on the length of the fruit
    """

    def __init__(self, fruits_list: list) -> None:

        self.fruit = random.choice(fruits_list)
        self.attempts = 2 + len(self.fruit)

    def positionView(self, guess: str, fruit: str) -> bool:
        """
        Shows the location of the letter if its present in the fruit name
        """
        guess = guess.lower()
        fruit = fruit.lower()

        show = ["X"] * len(fruit)
        flag = False
        if fruit.count(guess) > 1:
            for i in range(len(fruit)):
                if fruit.find(guess, i, i + 1) == i:
                    show[i] = guess
            print(f"You guessed the right letter!\n{show}")

        elif fruit.count(guess) == 1:
            a = fruit.find(guess)
            show[a] = guess
            print(f"You guessed the right letter!\n{show}")

        else:
            flag = True
            print("Oops! The guessed letter is wrong! Better luck next time.")

        return flag

    def playGame(self, attempts: int, fruit: str):

        i = 0
        while i < attempts:

            @staticmethod
            def taking_input() -> str:

                guess = input("Guess the letter:")

                return guess

            @staticmethod
            def timer(event):

                for _ in range(5):
                    time.sleep(1)
                    if event.is_set():
                        return
                else:
                    keyboard = Controller()
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print("\nYou are disqualified!")
                    quit()

            event = Event()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                f1 = executor.submit(timer, event)
                f2 = executor.submit(taking_input)

                try:
                    if len(f2.result()) == 1 and f2.result().isalpha() == True:
                        event.set()
                        print("Pleasee show em")
                        self.positionView(taking_input(), fruit)
                        if self.positionView(taking_input(), fruit):
                            i += 1
                    else:
                        quit()
                except Exception as e:
                    print(e)
            i += 1


print("Welcome to the Hangman Game!!\n\n********\nYou have to guess a fruit name!\n")
print("Rules of the game are as follows:\n")
print(
    "1. When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over."
)
print("2. For convenience, we have given length of word to be guessed + 2 chances")
print(
    "3. The chances are decreased by one only if player's guess is WRONG. If the guess is right, player's chance is not reduced"
)
print("4. If you dont guess in 5 secs, you will be disqualified from the game!")
fruits_list = [
    "Apple",
    "Avocado",
    "Apricots",
    "Banana",
    "Blackberries",
    "Blackcurrant",
    "Breadfruit",
    "Blueberries",
    "Carambola",
    "Cherries",
    "Cranberries",
    "CustardApple",
    "Grapes",
    "Guava",
    "HoneydewMelon",
    "Jackfruit",
    "Javaplum",
    "Kivifruit",
    "Lemon",
    "Lychee",
    "Mango",
    "Mulberries",
    "Orange",
    "Papaya",
    "Peaches",
    "Pear",
    "PassionFruit",
    "Pineapple",
    "Dragonfruit",
    "Pomegranate",
    "Rasberries",
    "Sapodilla",
    "Roseapple",
    "Strawberries",
    "Tamarind",
    "Watermelon",
]
player = Hangman(fruits_list)
player.playGame(player.attempts, player.fruit)
