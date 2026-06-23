import streamlit as st
import joblib

from utils import clean_text

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="News Classifier",
    page_icon="📰",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("models/best_model.pkl")
vectorizer = joblib.load("models/best_vectorizer.pkl")

class_names = model.classes_

# ---------------- HEADER ----------------
st.title("📰 News Headline Classification System")
st.markdown("Classify news headlines using NLP + Machine Learning")

st.divider()

# ---------------- SIDEBAR ----------------
st.sidebar.title("📊 Model Info")

st.sidebar.write("**Model Type:**", type(model).__name__)
st.sidebar.write("**Vectorizer:**", type(vectorizer).__name__)

st.sidebar.markdown("---")

st.sidebar.write("**Categories:**")
for c in class_names:
    st.sidebar.write("•", c)

# ---------------- SAMPLE DATA ----------------
samples = [
    "NASA launches new mission to explore Mars surface",
    "Government approves new education reform policy",
    "Messi scores hat-trick in final match of the season",
    "Apple releases new AI-powered iPhone update",
    "Stock markets fall due to global recession fears",
    "Scientists discover water on a distant exoplanet",
    "6 Months Into War, Russian Goods Still Flowing To U.S",
    "Parliament passes controversial new tax bill",
    "India wins cricket world cup in thrilling final"
]

st.sidebar.markdown("---")
st.sidebar.subheader("🧪 Try Samples")

# ---------------- SESSION STATE FIX ----------------
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# When sample clicked → update input text
for i, text in enumerate(samples):
    if st.sidebar.button(text, key=f"sample_{i}"):
        st.session_state.input_text = text

# ---------------- INPUT BOX ----------------
headline = st.text_area(
    "Enter a News Headline:",
    value=st.session_state.input_text,
    height=120
)

# ---------------- PREDICTION ----------------
if st.button("🔍 Predict Category"):

    if headline.strip() == "":
        st.warning("Please enter a headline!")
    else:

        # clean text
        cleaned = clean_text(headline)

        # vectorize
        vec = vectorizer.transform([cleaned])

        # prediction
        prediction = model.predict(vec)[0]

        st.subheader("📌 Prediction Result")
        st.success(f"Predicted Category: **{prediction}**")

        st.markdown("---")
        

        st.markdown("---")


        # # ---------------- CLEANED TEXT ----------------
        # st.subheader("🧹 Preprocessed Text")
        # st.code(cleaned)

# ---------------- FOOTER ----------------
# st.markdown("---")
# st.caption("🚀 NLP Project | TF-IDF / BoW + ML Models | Streamlit App")