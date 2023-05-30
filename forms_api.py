from googleapiclient.discovery import build
from google.oauth2 import service_account

def create_quiz(title,questions):
    credentials = service_account.Credentials.from_service_account_file(
        'quiz-from-f39965d84569.json',
        scopes=['https://www.googleapis.com/auth/forms.body']
    )

    # Build the Google Forms API client
    service = build('forms', 'v1', credentials=credentials)
    NEW_FORM = {
        "info": {
            "title": title,
        }
    }

    NEW_QUESTIONS = {
        "requests": [ {
            "updateSettings": {
                "settings": {
                    "quizSettings": {
                        "isQuiz": True
                    }
                },
                "updateMask": "quizSettings.isQuiz"
            }
        }]
    }



    for i, question in enumerate(questions):
        # Create the question item
        question_item = {
            "title": question["question"],
            "questionItem": {
                "question": {
                    "required": True,
                    "grading":{"correctAnswers":{"answers":[{"value":question["correct_answer"]}]},},
                    "choiceQuestion": {
                        "type": "RADIO",
                        "options": [
                            {"value": choice} for choice in question["choices"]
                        ],
                        "shuffle": True
                    }
                }
            }
        }

        # Add the question item to the batch update request
        NEW_QUESTIONS["requests"].append({
            "createItem": {
                "item": question_item,
                "location": {
                    "index": i
                }
            }
        })
                # Add a question about the name of the respondent
    name_question = {
        "title": "Name",
        "questionItem": {
            "question": {
                "required": True,
                "textQuestion": {'paragraph':False}
              
            }

        }
    }

    # Add the name question to the batch update request
    NEW_QUESTIONS["requests"].append({
        "createItem": {
            "item": name_question,
            "location": {
                "index": 0  # Place the name question at the beginning
            }
        }
    })

    # Create the form
    result = service.forms().create(body=NEW_FORM).execute()

    # Add the questions to the form
    question_setting = service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTIONS).execute()

    # Print the form URL
    form_id = result['formId']
    form_url = f'https://docs.google.com/forms/d/{form_id}/viewform'
    print("Quiz Form URL:", form_url)
    return form_url,form_id
def check_quiz_responses(form_id):
    credentials = service_account.Credentials.from_service_account_file(
        'quiz-from-f39965d84569.json',
        scopes=['https://www.googleapis.com/auth/forms.body','https://www.googleapis.com/auth/forms.responses.readonly']
    )

    # Build the Google Forms API client
    service = build('forms', 'v1', credentials=credentials)
    # Get the form responses
    response = service.forms().get(formId=form_id).execute()
    # Get the list of responses for the form
    form_responses = service.forms().responses().list(
        formId=form_id
    ).execute()

    if 'responses' in form_responses:
        responses = form_responses['responses']
        for response in responses:
            answers = response['answers']
            points = 0
            for question_id, answer in answers.items():
                grade = answer['grade']
                try:
                    if grade["correct"]==True:
                        points += 1
                except:
                    pass
            response["Total points"] = points
        return form_responses
    else:
        return None
    
