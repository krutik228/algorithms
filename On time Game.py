import time
from random import randint

def on_time_game():
    # target = randint(3, 7)
    target = 3
    input(f'Press Enter to play, you target is {target} seconds')
    timer_start = time.time()
    input('Press Enter to stop')
    timer_stop = round(time.time() - timer_start, 2)
    if timer_stop == target:
        print(timer_stop, 'you won!!')
    elif timer_stop < target:
        print(f"{round(target - timer_stop, 2)} too fast")
    else:
        print(f"{round(timer_stop - target, 2)} too slow")

if __name__ == '__main__':
    on_time_game()