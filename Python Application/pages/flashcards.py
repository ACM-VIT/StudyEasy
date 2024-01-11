import streamlit as st

def app():
    st.title('Flashcards')
    st.write('This is the Flashcards Section')

    # Example flashcard data (you can replace this with your actual content)
    # flashcards = [
    #     {"question": "Question 1", "answer": "Answer 1"},
    #     {"question": "Question 2", "answer": "Answer 2"},
    #     {"question": "Question 3", "answer": "Answer 3"}
    # ]

    # # Number of columns for the layout
    # num_columns = 3
    # rows = [flashcards[i:i + num_columns] for i in range(0, len(flashcards), num_columns)]

    # for row in rows:
    #     cols = st.columns(len(row))
    #     for idx, col in enumerate(cols):
    #         with col:
    #             flashcard = row[idx]
    #             st.markdown(f"### {flashcard['question']}")
    #             st.write(flashcard['answer'])
    #             st.button("Flip", key=f"btn{idx}")
    # Mock dictionary with question-answer pairs
    flashcards = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
        {"question": "What is the chemical symbol for gold?", "answer": "Au"},
        # Add more flashcards as needed
    ]

    # Function to show answer popup
    # def show_answer(answer):
    #     st.experimental_show(f"Answer: {answer}")

    # Function to display a flashcard
    def display_flashcard(question, answer):
        with st.container():
            st.markdown(f"### {question}")
            if st.button("Show Answer", key=question):
                show_answer(answer)

    # Arrange flashcards in rows and columns
    num_columns = 3
    rows = [flashcards[i:i + num_columns] for i in range(0, len(flashcards), num_columns)]

    for row in rows:
        cols = st.columns(len(row))
        for idx, col in enumerate(cols):
            with col:
                flashcard = row[idx]
                # Apply custom styling if needed
                st.markdown(
                    f"<div style='background-color:#f0f2f6;padding:10px;border-radius:10px;'>",
                    unsafe_allow_html=True
                )
                display_flashcard(flashcard["question"], flashcard["answer"])
                st.markdown("</div>", unsafe_allow_html=True)