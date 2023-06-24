from customtkinter import *

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
    print(result)

    return numbers, result