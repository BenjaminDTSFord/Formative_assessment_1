# Times Table Quiz
Code and documentation for Formative Assessment 1. Created by Benjamin Ford.

## Introduction
The Times Table Quiz is designed to be run in a Python terminal to help anyone practise their times tables. The format is a simple quiz, which will ask the user a series of twelve questions based on their preferred times table (1–12). Users can additionally opt to use a random mode, where each question is based on a random times table. The quiz can be repeated as many times as the user needs, provides immediate feedback after each question, and displays a final score at the end.

## User documentation

### Features

- A personalised experience, created by users entering their name.
- Choose to practise a specific times table (1–12).
- Random mode to generate questions from any of the times tables from 1 to 12.
- Immediate feedback given after every question.
- A final score out of twelve displayed at the end of the quiz.

### How to use the code
<img width="1398" height="1196" alt="Screen Recording 2026-06-30 at 17 11 06" src="https://github.com/user-attachments/assets/f3272c01-8b56-43da-88f5-e7567780d372" />

**Figure 1**: An animated GIF showing the code running. It demonstrates how to interact with the code to complete the quiz.

### Written Instructions
1. Download or clone the repository.
2. Keep all Python files in the same folder.
3. Open a Python interpreter and run the program using the Python file "Main_quiz.py".
4. When the program is running, you will be prompted in the terminal to enter your name.
5. Select a times table between **1 and 12** or enter **R** for random times tables.
6. Answer each multiplication question as it appears and receive immediate feedback.
7. After 12 questions, the quiz will finish and your final score will be shown.

## Technical Instructions

To execute the files, download or clone the repository and run the module "Main_quiz.py" in your preferred Python interpreter.

### Language

**Python version**: 3.13.9

### Libraries

**random**

The `random` module was used for two purposes. The first is for when the user selects random mode, to be tested on random times tables, and the second is to provide the number for the second half of the multiplication equation. In both cases, `random` generates a random integer between the values of 1 and 12 to be used within the multiplication equation.

### Files to run the code

- Main_quiz.py
- question_generator.py
- times_table_selection.py
- welcome_message.py

## Project Design

### Module Overview

**Main_quiz.py**

This is the main module that controls the program flow. It runs the quiz, checks answers, and calculates the score.

The script initially imports the modules question_generator, times_table_selection, and welcome_message to improve the reusability of the components.

```
import times_table_selection
import welcome_message
import question_generator
```

The program then begins by setting variables which collect the user's name and their times table choice, and sets the score to 0.

```
user_name = welcome_message.welcome_message()
times_table = times_table_selection.times_table_select()
score = 0
```

A confirmation message states the user's name and their selected times table choice.

```
print(f"Let's begin {user_name}, you have selected to test your {times_table} times table!")
```

A loop is then executed that runs 12 times. The `make_question(times_table)` function is called to generate the multiplication questions using the variable times_table. The user is prompted to answer the question. An `if` statement is used to validate the user's answer and provide immediate feedback after each answer. At the end of the loop, a final congratulatory message appears, informing the user of their score out of 12.

```
for _ in range(12):
    num1, num2, answer = question_generator.make_question(times_table)

    user_answer = int(input(f"what is {num1} x {num2}?"))

    if user_answer == answer:
        print("Correct")
        score += 1
    else:
        print(f"Incorrect, The correct answer is {answer}.")

print(f"Congratulations {user_name} you have completed the quiz! your final score is {score}/12.")
```

**question_generator.py**

This module generates the multiplication questions and their answers using the inputs provided by the user from the times_table_selection.py module.

The script imports the `random` module to allow random numbers to be generated for the multiplication questions.

```
import random
```

The `make_question(times_table)` function accepts the user's selected times table as a parameter. An `if` statement checks whether the user selected the random option (`"R"`). If they did, a random times table between 1 and 12 is generated. Otherwise, the user's selected times table is assigned to `num1`.

```
def make_question(times_table):

    if times_table == "R":
        num1 = random.randint(1, 12)
    else:
        num1 = times_table
```

A second random number between 0 and 12 is then generated and stored in the variable `num2`. The correct answer is calculated by multiplying `num1` and `num2`.

```
num2 = random.randint(0, 12)
answer = num1 * num2
```

The function returns the two numbers and the correct answer to the `Main_quiz.py` module, where they are used to display the question, validate the user's answer, and calculate the score.

```
return num1, num2, answer
```

**times_table_selection.py**

Prompts the user for the times table they would like to be quizzed on (1–12 or random) and validates that their input matches the correct values.

The function uses a `while True` loop to repeatedly prompt the user until a valid input is entered.

An `if` statement then validates the user's input. If the user enters "R", the function returns "R" to Main_quiz.py. If the user enters a number between 1 and 12, the function returns their chosen number as an integer to Main_quiz.py. If the user enters anything else, they will be prompted to try entering a value again.

```
        if times_table_choice == "R":
            return "R"
    
        elif times_table_choice.isdigit():
            times_table_choice = int(times_table_choice)

            if times_table_choice in range(1, 13):
                return times_table_choice
```

**welcome_message.py**

This displays the welcome message and prompts the user for their name to personalise their experience.

An initial welcome message is printed to greet the user.

```
    print("Welcome to the times table quiz")
    print("Are you ready to test your knowledge!")
```
The user is then prompted to enter their name, and their input is returned to Main_quiz.py.

```
    user_name = input("What is your name?")

    return user_name
```
### Future improvements

Potential enhancements include:
- Making the quiz timed.
- Giving the option to be tested sequentially from 1 to 12 rather than randomly.
- A graphical user interface.
- Exception handling for blank answers.
