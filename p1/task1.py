from math import lcm

from templates import get_username, get_answer
from generator import generate_numbers

user_name = get_username()
print("Find the smallest common multiple of given numbers.")
flag = True
while flag:
    numbers = generate_numbers(length=3, is_task_1=True)
    print("Question: ", numbers[0], numbers[1], numbers[2], "\nYour answer:")
    answer = lcm(numbers[0], numbers[1], numbers[2])
    user_answer = int(input())
    flag = get_answer(answer, user_answer)
