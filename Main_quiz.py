import times_table_selection
import welcome_message
import question_generator

user_name = welcome_message.welcome_message()
times_table = times_table_selection.times_table_select()
score = 0

print(f"Let's begin {user_name}, you have selected to test your {times_table} times table!")

for _ in range(12):
    num1, num2, answer = question_generator.make_question(times_table)

    user_answer = int(input(f"what is {num1} x {num2}?"))

    if user_answer == answer:
        print("Correct")
        score += 1
    else:
        print(f"Incorrect, The correct answer is {answer}.")

print(f"Congratulations {user_name} you have completed the quiz! Your final score is {score}/12.")