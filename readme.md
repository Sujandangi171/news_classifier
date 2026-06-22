📰 News Headline Classification System (NLP + Machine Learning)
🚀 Overview

This project is an end-to-end Natural Language Processing (NLP) system that classifies news headlines into predefined categories using machine learning. It includes full pipeline development — from data preprocessing and model training to evaluation and deployment using a Streamlit web application.

The system allows users to input any news headline and instantly receive a predicted category along with confidence scores.

🎯 Objective
Build a text classification system for news headlines
Compare different ML models and vectorization techniques
Handle real-world text data using NLP preprocessing
Deploy the best-performing model as a web application
📊 Dataset
Source: Kaggle News Category Dataset
Format: JSON
Fields used:
headline
category
Example categories:
Politics
Sports
Technology
Business
Entertainment
World News
Science
⚙️ Tech Stack
Python 🐍
Pandas / NumPy
NLTK (text preprocessing)
Scikit-learn (ML models)
TF-IDF / Bag of Words
Streamlit (web app)
Joblib (model saving)
🧠 Machine Learning Workflow
1. Data Preprocessing
Lowercasing text
Removing special characters and numbers
Stopword removal
Lemmatization
2. Feature Extraction
CountVectorizer (Bag of Words)
TF-IDF Vectorizer
3. Model Training & Comparison

Models tested:

Naive Bayes
Logistic Regression
Linear SVM
Random Forest
4. Model Selection

The best model is selected based on:

Accuracy
F1-score
Precision / Recall
5. Deployment

Final model is deployed using Streamlit for real-time predictions.

🏆 Best Model
Model: Logistic Regression / Linear SVM
Vectorizer: TF-IDF
Optimization: Class weighting for imbalance handling
📈 Performance
Accuracy: ~82%–90% (depending on class setup)
Evaluation metrics:
Precision
Recall
F1-score
Confusion Matrix
🖥️ Streamlit App Features
Enter custom news headlines
Get instant category prediction
View confidence scores for all classes
Sample headlines for quick testing
Clean interactive UI
📂 Project Structure
news_classifier/
│
├── data/
│   ├── News_Category_Dataset.json
│   ├── train.csv
│   └── test.csv
│
├── models/
│   ├── best_model.pkl
│   └── best_vectorizer.pkl
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_model_comparison.ipynb
│   └── 03_final_model_training.ipynb
│
├── utils.py
├── app.py
├── train.py
├── requirements.txt
├── .gitignore
└── README.md
🚀 How to Run This Project
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Run preprocessing & training notebooks

Open Jupyter Notebook:

jupyter notebook

Run:

01_data_preprocessing.ipynb
02_model_comparison.ipynb
03_final_model_training.ipynb
3️⃣ Train model (optional script)
python train.py
4️⃣ Run Streamlit app
streamlit run app.py
🧪 Example Predictions
Input Headline	Predicted Category
NASA launches new Mars mission	Science / Tech
Government passes new tax law	Politics
Messi scores winning goal	Sports
Apple releases new iPhone	Technology
📌 Key Learnings
NLP text preprocessing pipeline
Feature extraction using TF-IDF
Model comparison and evaluation
Handling class imbalance
Deployment using Streamlit
⚠️ Future Improvements
Add deep learning models (LSTM / BERT)
Improve handling of class imbalance
Deploy on cloud (Streamlit Cloud / HuggingFace Spaces)
Add real-time news scraping