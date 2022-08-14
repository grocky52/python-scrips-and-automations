
import time
import random

class executionTimer:
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time

timer = executionTimer()
my_list = [random.randint(1, 888989) for num in range(1,1000000) if num % 2 == 0]
print(f'finish time {timer.duration()} seconds')
