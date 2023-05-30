import streamlit as st
from main import quiz_creator
from forms_api import check_quiz_responses

def create_quiz():
    st.title("Audio Quiz Prompt")

    # Create a button to start recording
    if st.button("Start Recording: say the quiz subject and number of questions"):
        # Call your function to record the audio and get the quiz URL
        q = quiz_creator()
        quiz_url = q[0]
        quiz_id = q[1]

        # Display the quiz URL
        st.subheader("Quiz URL")
        st.markdown(f"[Quiz Link]({quiz_url})")
        return quiz_id

def display_responses(quiz_id):
    st.title("Responses")
    # Call your function to display the responses
    s = check_quiz_responses(quiz_id)
    st.write(s)

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Create Quiz", "Display Responses"))

    if page == "Create Quiz":
        quiz_id = create_quiz()
        st.session_state.quiz_id = quiz_id
        print()
    elif page == "Display Responses":
        if "quiz_id" in st.session_state:
            display_responses(st.session_state.quiz_id)
        else:
            st.warning("Please create a quiz first.")

if __name__ == "__main__":
    main()
