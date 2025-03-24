import datetime
import sys
import os
import random
import threading
import queue
sys.path.append('./')
from Collective_resources.ascii import DiceBoard

BOARD_WIDTH = 60
BOARD_HEIGHT = 30
TIME_LIMIT = 30
SCORE_CORRECT = +4
SCORE_INCORRECT = -1

def get_input_with_timeout(input_queue, timeout):
    """Runs input() in a separate thread and stops when time is up."""
    def input_thread():
        input_queue.put(input("> ").strip())  # Get user input and store it in the queue

    thread = threading.Thread(target=input_thread, daemon=True)
    thread.start()
    thread.join(timeout)  # Wait for input but stop if timeout is reached

    if thread.is_alive():  # If the input thread is still running after timeout
        return None
    return input_queue.get() if not input_queue.empty() else None


print(" Dice Math ".center(BOARD_WIDTH+2,'*'))
print("""Here are the rules to the game:
    Add up numbers on all the dices shown on screen.
    You have 30 seconds to answer as many as possible.
    You get 4 points for each question.
    You lose 1 for each incorrect one.""")
input("Press enter to begin ...")
score = 0
start_time = datetime.datetime.now()
while True:
    os.system('cls' if os.name=='nt' else 'clear')
    board = DiceBoard()
    lst = [random.randint(1,6) for _ in range(4)]
    for i in board.random_square(BOARD_WIDTH,BOARD_HEIGHT,lst):
        print(i)
    remaining_time = TIME_LIMIT - (datetime.datetime.now() - start_time).total_seconds()
    if remaining_time <= 0:
        break
    print(f"You have {int(remaining_time)} seconds left!")
    
    input_queue = queue.Queue()
    x = get_input_with_timeout(input_queue,remaining_time)

    if x is None:
        print(" TIME UP ".center(BOARD_WIDTH+2))
        break

    try:
        x = int(x)
        if x == sum(lst):
            score += SCORE_CORRECT
        else:
            score += SCORE_INCORRECT
    except ValueError:
        print("Invalid input! You lose 1 point.")
        score += SCORE_INCORRECT

os.system('cls' if os.name=='nt' else 'clear')
print("\nGame Over! Your final score is:", score)
exit(0)