import random

operators ={"+","-","/","*"}
min_operand = 3
max_operand = 12
total_problems = 10


def generate_problem():
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)
    
    eper = str(left) + " " + operator + " " +str(right)
    answer = eval(exper)
    return expr,answer
for i in range(total_problems):
    



    