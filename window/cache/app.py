from customtkinter import *
from window.__init__ import text

import statistics

def calculate(arg1):
    words = arg1.split()
    numbers = []
    for word in words:
        try:
            number = float(word)
            numbers.append(number)
        except ValueError:
            pass

    result = statistics.mean(numbers)
    # text.config(text=numbers)
    # text.grid()

    return numbers, result