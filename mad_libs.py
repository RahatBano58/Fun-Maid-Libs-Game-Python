import streamlit as st
import random

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        font-size: 38px;
        color: #230bb0;
        font-weight: bold;
        text-align: center;
        margin-top: 50px;
        margin-bottom: 20px;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
        text-transform: uppercase;
        line-height: 1.4;
    }
    .sidebar-header {
        font-size: 25px;
        color: #5b0fb8;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .madlib {
        font-size: 24px;
        color: #777;
        background-color: #f4f4f4;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    .footer {
        font-size: 20px;
        color: #4a0db5;
        text-align: center;
        margin-top: 50px;
        margin-bottom: 20px;
        font-style: italic;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
        letter-spacing: 1px;
        word-spacing: 2px;
        text-transform: uppercase;
        line-height: 1.4;
    }
    </style>
    """, unsafe_allow_html=True
)

# Streamlit App Title with Custom CSS
st.markdown('<h1 class="title">🎭 Fun Mad Libs Game!</h1>', unsafe_allow_html=True)

# Sidebar for User Inputs
st.sidebar.markdown('<h2 class="sidebar-header">Fill in the Blanks ✍️</h2>', unsafe_allow_html=True)

# Taking User Inputs
adj = st.sidebar.text_input("Enter an Adjective:", "innovative")
verb1 = st.sidebar.text_input("Enter a Verb:", "code")
verb2 = st.sidebar.text_input("Enter another Verb:", "develop")
famous_person = st.sidebar.text_input("Enter a Famous Person:", "Ada Lovelace")

# Fun Sentences to Make it More Interesting
madlib_templates = [
    f"The future of AI is truly {adj}! Every time I {verb1}, I feel like I'm contributing to something revolutionary. Just like {famous_person}, we are pushing the boundaries of what technology can {verb2}.",
    f"AI is transforming the world in {adj} ways! When I {verb1}, it feels like I’m part of a greater mission, much like how {famous_person} paved the way for modern computing by helping us {verb2} the unimaginable.",
    f"Coding in the realm of AI is incredibly {adj}. Each time I {verb1}, it’s like I’m building the future. With visionaries like {famous_person} as inspiration, I strive to {verb2} new solutions that shape tomorrow."
]


# Button to Generate Mad Libs
if st.button("Generate Mad Lib 🎭"):
    selected_madlib = random.choice(madlib_templates)
    st.subheader("Here's Your Mad Lib! 🎉")
    st.markdown(f'<p class="madlib">{selected_madlib}</p>', unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">Made with ❤️ by Rahat Bano</p>', unsafe_allow_html=True)
