"""
Utility functions for hangman.
"""

import msvcrt
import sys
import time


class TimeoutExpired(Exception):
    """
    TimeoutExpired is raised when user doesn't input anything until given number of seconds.
    """

    pass


def input_with_timeout(prompt: str, timeout: int, timer=time.monotonic) -> str | None:
    """
    Time limited input function.
    Only works on windows for now.
    """
    sys.stdout.write(prompt)
    sys.stdout.flush()
    endtime = timer() + timeout

    result = []
    while timer() < endtime:
        if msvcrt.kbhit():
            result.append(msvcrt.getwche())
            if result[-1] == "\r":
                return "".join(result[:-1])

        time.sleep(0.04)  # just to yield to other processes/threads

    raise TimeoutExpired


if __name__ == "__main__":
    try:
        answer = input_with_timeout("heya", 5)
    except TimeoutExpired:
        print("welp")
    else:
        print("this you?", answer)
