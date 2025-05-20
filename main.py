# importing tasks as modules
from functions.fibonacci_func import fibo
from functions import salaries_func


text = """There once were 128 ships that put to 1 sea
          The names of those ships were Billies O'Tea
          1000 winds blew up, 30 bows dipped down
          Oh blow, 60 bully boys, blow"""


gen = salaries_func.generator_numbers(text)

# calling fibonacci
print(f'fibonacci: {fibo(15)}')

try:
    print(f'sum of the profits: {salaries_func.sum_profit(salaries_func.generator_numbers, text)}')
    for _ in range(5):
        print(next(gen))
except StopIteration:
    print('Loop range is too big.')
