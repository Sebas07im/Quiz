import random
import time

operators = ["+", "-", "*"]
min_operand = 2
max_operand = 12
total_problems = 5

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)
    expression = f"{left} {operator} {right}"
    answer = eval(expression)
    return expression, answer

wrong = 0

input("Press enter to start!")
print('______________')

start_time = time.time()

for num in range(total_problems):
    expression, answer = generate_problem()
    while True:
        guess = input(f"Question #{num + 1}: {expression} = ")
        if guess==str(answer):
            break
        wrong += 1
end_time = time.time()
total_time = end_time - start_time

print(f"Good job! You finished in {round(total_time, 1)} seconds!")