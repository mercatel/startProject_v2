from functools import wraps
from time import time


class DurationFunc:
    def __init__(self, text=''):
        self.text = text

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            end = time()
            print(f'{self.text} - {round(end - start, 3)}')
            return result

        return wrapper
