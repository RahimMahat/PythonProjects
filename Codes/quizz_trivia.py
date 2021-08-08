#!/usr/bin/env python3
import requests
import html


link_open_trivia_db = "https://opentdb.com/api_config.php"

parameters = {
    "amount": 10,
    "type": "boolean"
}
opentrivia_db_api_url = "https://opentdb.com/api.php"


question_bank = []


def get_questions():
    global question_bank
    response = requests.get(opentrivia_db_api_url, params=parameters)
    response.raise_for_status()
    data = response.json()
    question_data = data["results"]

    for question in question_data:
        question_text = question["question"]
        correct_ans = question["correct_answer"]
        question_bank.append(
            {"Question": question_text, "Answer": correct_ans})


def play():
    # first of all getting question and filling our question bank
    get_questions()
    global question_bank
    i = 0
    score = 0
    while i < len(question_bank):
        # from using html.unescape we will get the text in human readable format
        Question = html.unescape(question_bank[i]["Question"])
        Answer = question_bank[i]["Answer"]
        print(f"Q {i+1}. {Question}\n\n")
        # print(Answer)
        ans = input("Enter your answer(True/False): ")
        if ans == Answer:
            print("\nThat is the correct answer", end="\t\t\t\t")
            score += 1
        else:
            print("\nThat is wrong answer", end="\t\t\t\t")

        print(f"Score: {score}")

        i += 1

    print(f"\n\nYour final score is: {score}\n\n")


if __name__ == '__main__':
    play()
