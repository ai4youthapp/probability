import streamlit as st

# -------------------- PAGE SETTINGS --------------------
st.set_page_config(page_title="Probability Quiz", page_icon="🎲")

st.title("🎯 Probability Quiz — Marbles Edition")
st.write("Answer the following questions to test your understanding of probability terms!")

# -------------------- SESSION STATE --------------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_no" not in st.session_state:
    st.session_state.q_no = 0
if "responses" not in st.session_state:
    st.session_state.responses = []  # store user answers and results

# -------------------- QUIZ QUESTIONS --------------------
questions = [
    {"question": "If you select a marble without looking, how likely is it that you will pick a black one?",
     "image": "images/certain.png", "answer": "certain"},
    {"question": "If you select a marble without looking, how likely is it that you will pick a black one?",
     "image": "images/impossible.png", "answer": "impossible"},
    {"question": "If you select a marble without looking, how likely is it that you will pick a black one?",
     "image": "images/likely.png", "answer": "likely"},
    {"question": "If you select a marble without looking, how likely is it that you will pick a black one?",
     "image": "images/probable.png", "answer": "probable"},
    {"question": "If you select a marble without looking, how likely is it that you will pick a black one?",
     "image": "images/equal.png", "answer": "equal chance"}
]

# -------------------- QUIZ LOGIC --------------------
q_no = st.session_state.q_no
total_qs = len(questions)

if q_no < total_qs:
    q = questions[q_no]
    st.image(q["image"], width=400)
    st.subheader(f"Question {q_no + 1} of {total_qs}")
    st.write(q["question"])

    st.progress((q_no + 1) / total_qs)

    options = ["certain", "likely", "probable", "unlikely", "impossible", "equal chance"]
    answer = st.radio("Choose your answer:", options, index=None, horizontal=True)

    if st.button("Submit Answer"):
        if answer:
            correct = (answer.lower() == q["answer"].lower())
            if correct:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect. The correct answer is **{q['answer']}**.")

            # Save the response
            st.session_state.responses.append({
                "question": q["question"],
                "your_answer": answer,
                "correct_answer": q["answer"],
                "result": "Correct ✅" if correct else "Wrong ❌"
            })

            st.session_state.q_no += 1
            st.rerun()
        else:
            st.warning("Please select an answer before submitting.")
else:
    # -------------------- FINAL SCORE --------------------
    st.balloons()
    st.success(f"🏁 Quiz Completed! Your final score: **{st.session_state.score} / {total_qs}**")

    # --- Show Wrong Answers ---
    wrong_answers = [r for r in st.session_state.responses if r["result"].startswith("Wrong")]
    if wrong_answers:
        st.markdown("### ❌ Review Your Mistakes")
        for i, r in enumerate(wrong_answers, 1):
            st.write(f"**Q{i}.** {r['question']}")
            st.write(f"Your answer: ❌ *{r['your_answer']}*")
            st.write(f"Correct answer: ✅ **{r['correct_answer']}**")
            st.divider()
    else:
        st.markdown("🎉 Amazing! You got everything correct!")

    # --- Restart Option ---
    if st.button("Restart Quiz"):
        st.session_state.q_no = 0
        st.session_state.score = 0
        st.session_state.responses = []
        st.rerun()
