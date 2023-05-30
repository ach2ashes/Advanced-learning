from chatgpt import *
from transcribe import *
from forms_api import * 
from record_audio import *

def quiz_creator() : 
    prompt = transcribe()
    print(prompt)
    quiz = make_quiz(prompt)
    print(quiz)
    quiz_data = return_questions(quiz)
    print(quiz_data)
    return create_quiz("quiz",quiz_data)
