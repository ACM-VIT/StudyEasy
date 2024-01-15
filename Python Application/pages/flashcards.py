import streamlit as st
def app():
    
    rotating_card_html = """
    <style>
    .card-container {
        perspective: 1000px;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-gap: 20px;
        justify-content: space-around;
    }

    .card {
        width: 250px; /* Adjusted card width */
        height: 200px;
        margin: 10px;
        border-radius: 15px; /* Added border-radius for rounded edges */
        transform-style: preserve-3d;
        transition: transform 0.8s ease-in-out; /* Adjusted transition properties */
        cursor: pointer;
    }

    .card:hover {
        transform: rotatey(180deg);
        transition: transform 0.8s ease-in-out; /* Added transition property to fix flickering */
    }

    .card .card-inner {
        width: 100%;
        height: 100%;
        position: absolute;
        backface-visibility: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .card .front {
        background-color: #3498db;
        border-radius: 15px; /* Added border-radius for rounded edges */
    }

    .card .back {
        background-color: #e74c3c;
        transform: rotateY(180deg);
        border-radius: 15px; /* Added border-radius for rounded edges */
    }
    </style>

    <div class="card-container">
    <div class="card">
        <div class="card-inner front">
        <p>Question 1</p>
        </div>
        <div class="card-inner back">
        <p>Answer</p>
        </div>
    </div>
    <div class="card">
        <div class="card-inner front">
        <p>Question 2</p>
        </div>
        <div class="card-inner back">
        <p>Answer</p>
        </div>
    </div>
    <div class="card">
        <div class="card-inner front">
        <p>Question 3</p>
        </div>
        <div class="card-inner back">
        <p>Answer</p>
        </div>
    </div>
    <div class="card">
        <div class="card-inner front">
        <p>Question 4</p>
        </div>
        <div class="card-inner back">
        <p>Answer</p>
        </div>
    </div>
    <div class="card">
        <div class="card-inner front">
        <p>Question 5</p>
        </div>
        <div class="card-inner back">
        <p>Answer</p>
        </div>
    </div>
    <div class="card">
        <div class="card-inner front">
        <p>Question 6</p>
        </div>
        <div class="card-inner back">
        <p>Answer</p>
        </div>
    </div>
    <div class="card">
        <div class="card-inner front">
        <p>Question 7</p>
        </div>
        <div class="card-inner back">
        <p>Answer</p>
        </div>
    </div>
    <div class="card">
        <div class="card-inner front">
        <p>Question 8</p>
        </div>
        <div class="card-inner back">
        <p>Answer</p>
        </div>
    </div>
    <div class="card">
        <div class="card-inner front">
        <p>Question 9</p>
        </div>
        <div class="card-inner back">
        <p>Answer</p>
        </div>
    </div>
    <div class="card">
        <div class="card-inner front">
        <p>Question 10</p>
        </div>
        <div class="card-inner back">
        <p>Answer</p>
        </div>
    </div>
    <div class="card">
        <div class="card-inner front">
        <p>Question 11</p>
        </div>
        <div class="card-inner back">
        <p>Answer</p>
        </div>
    </div>
    <div class="card">
        <div class="card-inner front">
        <p>Question 12</p>
        </div>
        <div class="card-inner back">
        <p>Answer</p>
        </div>
    </div>

    <!-- Repeat the card structure for additional cards -->
    </div>
    """

    st.title("Flash cards")
    st.markdown(rotating_card_html, unsafe_allow_html=True)

