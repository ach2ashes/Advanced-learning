import re
import openai
openai.api_key = "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"
def make_quiz(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant.That creates multi choice questions quizzes for university teachers"},
            {"role": "user", "content": "make a quiz about" +prompt+ ", include answers ,all questions will have three (3) choices, the format should be in the following format:'1.question\na)choice1 (1)\nb)choice2 (2)\n....\nanswer: 1'"},
        ]
    )
    return response['choices'][0]['message']['content']
def return_questions(response):         
    regex = r"(\d+)\.\s(.*\?)\s*a\)\s(.*\s\(\d+\))\s*b\)\s(.*\s\(\d+\))\s*c\)\s(.*\s\(\d+\))\s*Answer:\s(\d+)"

    matches = re.findall(regex, response)

    questions = []

    for match in matches:

        question = match[1]
        choice_a = match[2]
        choice_b = match[3]
        choice_c = match[4]
        answer = match[5]

        question_data = {
            'question': question,
            'correct_answer': None,
            'choices': []
        }

        choices = [choice_a, choice_b, choice_c]
        question_data['choices'] = choices
        question_data['correct_answer'] = choices[int(answer) - 1]

        questions.append(question_data)

    return questions


