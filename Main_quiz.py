import timestable_selection
import welcome_message
import question_generator

user_name = welcome_message.welcome_message()
times_table = (timestable_selection.timestable_select())

print(f"Lets Begin {user_name}, you have selected to test your {times_table} times table!")

score = 0

for questions in range (12):
    num1, num2, answer = question_generator.make_question(times_table)

    user_answer = int(input(f"what is {num1} x {num2}?"))

    if user_answer == answer:
        print("correct")
        score += 1
    else:
        print(f"incorrect, The correct answer is {answer}.")

print(f"Congrtulations {user_name} you have completed the quiz! your final score is {score}/12.")