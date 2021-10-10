from question import question

question_prompts = [
    "what is my favourite character ?\n (a) rick sanchez\n (b) bojack horesman \n (c) garry\n \n ",
    "what is my favourite type of heavy metal ? \n (a) black metal \n (b) thash \n (c) death metal\n\n",
    "what is my favourite artist ? \n (a) a boogie \n (b) comethazine (c) scarlxrd\n\n"
]

questions = [
    question(question_prompts[0], "b"),
    question(question_prompts[1], "a"),
    question(question_prompts[0], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you have " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
