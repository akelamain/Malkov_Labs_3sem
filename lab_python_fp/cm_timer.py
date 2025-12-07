from contextlib import contextmanager
import time

class cm_timer_1():
    def __init__(self, name="Блок"):
        self.name = name
    
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        end = time.perf_counter()
        elapsed = end - self.start
        print(f"Программа завершилась за {elapsed} секунд")

@contextmanager
def cm_timer_2():
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f"Программа завершилась за {end - start} секунд")

with cm_timer_2():
    time.sleep(5.5)

with cm_timer_2():
    time.sleep(5.5)