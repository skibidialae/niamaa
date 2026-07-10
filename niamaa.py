import streamlit as st
import random
from datetime import datetime

# --- 1. GLOBAL STATE FOR NAVIGATION ---
if "current_page" not in st.session_state:
    st.session_state.current_page = "🎂 Birthday message"

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Where to next, Birthday Girl?")
    
    chosen_page = st.radio(
        "Go to ⋆˚࿔",
        ["🎂 Birthday message", "🎮 Quiz"],
        index=0 if st.session_state.current_page == "🎂 Birthday message" else 1
    )
    st.session_state.current_page = chosen_page
    
    st.markdown("---")
    st.write(f"Today: {datetime.now().strftime('%B %d, %Y')}")

# --- 3. 🎂 BIRTHDAY PAGE ---
if st.session_state.current_page == "🎂 Birthday message":
    st.title("⋆.˚Happy Birthday Niamaa ⋆.˚")

    # Creates a lopsided grid: 1/3 width for the image, 2/3 width for the text greeting
    img_col, text_col = st.columns([1, 2])

    with img_col:
        # Adds vertical spacing to push the picture down slightly for that lopsided feel
        st.write("## ")
        try:
            st.image("IMG_3086 (1).jpg", use_container_width=True)
        except Exception:
            # Dual-path safety fallback check for the Downloads folder
            st.image(r"C:\Users\PC\Downloads\IMG_3086 (1).jpg", use_container_width=True)

    with text_col:
        st.subheader("To the Birthday Princess ≽^• ˕ • ྀི≼")
        st.write("""
Enjoy this little gift from me :)
        """)
        st.markdown("𓆝 ⋆.")

    with st.expander("°‧ 𓆝 Open your birthday letter!! 𓆞 ·｡"):
        # Triggers a burst of celebratory balloons when she clicks open the letter!
        st.balloons()
        
        st.write("""
Happy Birthday lovee ଳଳ

I guess it's pretty hard to put all my love for you into such small words, but not as pretty as youuu (and hopefully not as hard).

I've wanted to make you something special this year despite the cruel distance that separates us, so I made this little website!!

You're the best friend I've always wanted, and I'm forever grateful to have such an amazing person in my life. Thank you for always caring about me, listening to me, making me laugh, and constantly reassuring me whenever I need it.

You deserve all the love and happiness in the world, and I hope this year brings you everything you've been wishing for.

Enjoy your special day angel.

PS: I LOVE YOU SO MUCH!! ଳ
        """)

# --- 4. 🎮 QUIZ PAGE ---
elif st.session_state.current_page == "🎮 Quiz":
    st.title("✮⋆˙ Let's get to know Niamaa")

    questions = {
        "⊹₊˚‧︵‿₊୨Niama୧₊‿︵‧˚₊⊹": [
            {
                "q": "Who is the most amazing, beautiful and smart person of all time ?",
                "options": ["squeezie", "Niama", "pipi"],
                "answer": "Niama",
                "correct_msg": "good job yippee!",
                "wrong_msg": "HOW DARE YOU PICK SOMETHING ELSE"
            },
            {
                "q": "Who is Niama’s biggest fan ?",
                "options": ["You", "Alae", "squeezie"],
                "answer": "Alae",
                "correct_msg": "yay good job hehe",
                "wrong_msg": "ALAE IS YOUR BIGGEST SUPPORTER HOW DARE U"
            },
            {
                "q": "How old is the princess turning ?",
                "options": ["squeezie", "17", "67"],
                "answer": "17",
                "correct_msg": "HOLYY SOMEONE IS OLD",
                "wrong_msg": "you're right technically"
            }
        ],
        "Cats ₍^. .^₎Ⳋ": [
            {
                "q": "What's Niama's favorite type of cat?",
                "options": ["a pitbull that once chased her", "alae miaw", "orange cats"],
                "answer": "alae miaw",
                "correct_msg": "thats rightt you're doing miawesome",
                "wrong_msg": "HOW DARE YOU CHEAT ON ME"
            },
            {
                "q": "Is Niama secretly a cat?",
                "options": ["scientists are still investigating", "absolutely", "no"],
                "answer": "absolutely",
                "correct_msg": "i knew it hihi",
                "wrong_msg": "YOU DONT HIDE THE TRUTH FROM ME"
            },
            {
                "q": "What's Niama's nickname when she turns into a cat?",
                "options": ["mine", "nini", "NIAMIAW"],
                "answer": "NIAMIAW",
                "correct_msg": "GOOD JOBBB !!",
                "wrong_msg": "you're technically right butt no <3"
            },
        ]
    }

    if "score" not in st.session_state: st.session_state.score = 0
    if "streak" not in st.session_state: st.session_state.streak = 0
    if "current_q_idx" not in st.session_state: st.session_state.current_q_idx = 0

    category = st.selectbox("Category ଳ:", list(questions.keys()))
    category_questions = questions[category]
    
    idx = st.session_state.current_q_idx % len(category_questions)
    current_question = category_questions[idx]

    if "active_choices" not in st.session_state or st.session_state.get("last_q") != current_question["q"]:
        st.session_state.active_choices = random.sample(current_question["options"], len(current_question["options"]))
        st.session_state.last_q = current_question["q"]

    with st.form(key="quiz_form"):
        st.subheader(current_question["q"])
        choice = st.radio("Your answer ଳ:", st.session_state.active_choices)
        submit_button = st.form_submit_button(label="Submit Answer")

    if submit_button:
        if choice == current_question["answer"]:
            st.session_state.score += 1
            st.session_state.streak += 1
            st.success(f"ദ്ദി ˉ͈̀꒳ˉ͈́ ) {current_question['correct_msg']}")
            st.info(f"🔥 Streak: {st.session_state.streak}")
            
            # Triggers a massive confetti shower if she gets a perfect clean streak of 3!
            if st.session_state.streak % 3 == 0:
                st.snow()
        else:
            st.session_state.streak = 0
            st.error(current_question["wrong_msg"])
            st.warning(f"The answer was: {current_question['answer']}")

    if st.button("Next Question ➡️"):
        st.session_state.current_q_idx += 1
        st.rerun()

    # --- UPDATED INTERACTIVE SIDEBAR DISPLAY ---
    st.sidebar.markdown("---")
    
    if st.session_state.streak == 0:
        cat_mood = "( ू• 𖥦 •ू )"
        cat_status = "*NIAMIAW is sleeping... start a streak to wake her up!*"
    elif 1 <= st.session_state.streak < 3:
        cat_mood = "(=^･ω･^=)"
        cat_status = "*She's waking up! Keep going!*"
    elif 3 <= st.session_state.streak < 6:
        cat_mood = "(๑•͈ᴗ•͈)ᓂ-==͟͟͞ ♡"
        cat_status = "*WOWWW madame patate princesse is super proud of you!*"
    else:
        cat_mood = "≽^• ˕ • ྀི≼ "
        cat_status = "*YAYYYY PERFECT STREAK!!*"

    st.sidebar.subheader(cat_mood)
    st.sidebar.markdown(cat_status)
    st.sidebar.markdown("---")

    st.sidebar.write(f"**Score:** {st.session_state.score}")
    st.sidebar.write(f"**Streak:** {st.session_state.streak} 🔥")

    if st.sidebar.button("Reset Game"):
        st.session_state.score = 0
        st.session_state.streak = 0
        st.session_state.current_q_idx = 0
        st.rerun()

# --- 5. GLOBAL FOOTER ---
st.markdown("---")
st.caption("Built with love for Niamaa by Alae /ᐠ. .ᐟ\ Ⳋ")