import random

# KBC Game

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": 1
    },
    {
        "question": "Who is the CEO of Tesla?",
        "options": ["Jeff Bezos", "Elon Musk", "Tim Cook", "Mark Zuckerberg"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Jupiter", "Saturn", "Mars", "Neptune"],
        "answer": 3
    },
    {
        "question": "Which country won the FIFA World Cup 2018?",
        "options": ["Brazil", "Germany", "Argentina", "France"],
        "answer": 4
    }
]

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    answer = int(input("Your answer (enter the option number): "))
    if answer == question["answer"]:
        print("Correct answer!\n")
        return True
    else:
        print("Sorry, wrong answer!\n")
        return False

def play_game():
    print("Welcome to Kaun Banega Crorepati!")
    print("Answer the following questions to win the game.")
    print("You have 4 lifelines: 50-50, Phone-a-Friend, Audience Poll, and Expert Advice.")
    print("Let's begin!\n")

    total_questions = len(questions)
    winnings = [5000, 10000, 25000, 50000]
    lifelines = ["50-50", "Phone-a-Friend", "Audience Poll", "Expert Advice"]
    current_winnings = 0
    lifeline_used = False

    for i, question in enumerate(questions):
        print(f"Question {i+1}/{total_questions}")
        if lifeline_used:
            lifeline_used = False
        else:
            lifeline_index = random.randint(0, len(lifelines) - 1)
        while True:
            if not ask_question(question):
                if lifeline_index < len(lifelines):
                    use_lifeline = input("Sorry, that was the wrong answer! Do you want to use a lifeline? (yes/no): ")
                    if use_lifeline.lower() == "yes":
                        print(f"You chose the '{lifelines[lifeline_index]}' lifeline.")
                        if lifelines[lifeline_index] == "50-50":
                            remaining_options = question["options"][:]
                            remaining_options.pop(question["answer"]-1)
                            option_to_remove = random.choice(remaining_options)
                            question["options"].remove(option_to_remove)
                            lifeline_used = True
                        elif lifelines[lifeline_index] == "Phone-a-Friend":
                            print("Your friend thinks the answer is option", random.randint(1, len(question["options"])), ".")
                        elif lifelines[lifeline_index] == "Audience Poll":
                            correct_percentage = random.randint(70, 100)
                            print(f"The audience thinks that the correct answer is option {question['answer']}, with {correct_percentage}% of the votes.")
                        elif lifelines[lifeline_index] == "Expert Advice":
                            print("Our expert thinks the answer is option", question["answer"], ".")
                        break
                print("Game Over!")
                print(f"You won {current_winnings} rupees.")
                return
            else:
                if i < len(winnings):
                    current_winnings = winnings[i]
                    print(f"Congratulations! You won {current_winnings} rupees!")
                else:
                    print("Congratulations! You answered all the questions correctly and won the game!")
                    return

play_game()
