import random

def make_question(times_table):

    if times_table == "R":
        num1 = random.randint(1,12)
    else:
        num1 = times_table
    
    num2 = random.randint(0,12)
    answer = num1 * num2

    return num1, num2, answer