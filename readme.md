# 📰 News Headline Classification System (NLP + Machine Learning)

## 🚀 Overview

This project is an **end-to-end Natural Language Processing (NLP)** application that classifies news headlines into predefined categories using machine learning techniques.

The project covers the complete workflow, including:

* Data preprocessing
* Feature extraction
* Model training and comparison
* Performance evaluation
* Model deployment using **Streamlit**

Users can enter any news headline and instantly receive:

* Predicted category
* Confidence scores for all classes

---

## 🎯 Objective

* Build a text classification system for news headlines.
* Compare different machine learning models and vectorization techniques.
* Handle real-world text data through NLP preprocessing.
* Deploy the best-performing model as an interactive web application.

---

## 📊 Dataset

**Source:** Kaggle News Category Dataset

**Format:** JSON

### Features Used

* `headline`
* `category`

### Example Categories

* Politics
* Sports
* Technology
* Business
* Entertainment
* World News
* Science

---

## ⚙️ Tech Stack

* **Python 🐍**
* **Pandas**
* **NumPy**
* **NLTK** (Text Preprocessing)
* **Scikit-learn**
* **CountVectorizer (Bag of Words)**
* **TF-IDF Vectorizer**
* **Joblib**
* **Streamlit**

---

# 🧠 Machine Learning Workflow

## 1. Data Preprocessing

The following NLP preprocessing techniques are applied:

* Convert text to lowercase
* Remove special characters and numbers
* Remove stopwords
* Perform lemmatization

---

## 2. Feature Extraction

Two vectorization techniques were explored:

### 🔹 CountVectorizer (Bag of Words)

Converts text into frequency-based vectors.

### 🔹 TF-IDF Vectorizer

Transforms text into weighted feature vectors based on term importance.

---

## 3. Model Training and Comparison

The following machine learning algorithms were evaluated:

| Model               | Description                               |
| ------------------- | ----------------------------------------- |
| Naive Bayes         | Fast probabilistic classifier             |
| Logistic Regression | Linear classifier with strong performance |
| Linear SVM          | Effective for text classification         |
| Random Forest       | Ensemble-based classifier                 |

---

## 4. Model Selection

Models were compared using:

* Accuracy
* Precision
* Recall
* F1-score

The best model was selected based on overall performance.

---

## 🏆 Best Model

| Component    | Selected Method                        |
| ------------ | -------------------------------------- |
| Model        | Logistic Regression / Linear SVM       |
| Vectorizer   | TF-IDF                                 |
| Optimization | Class weighting for imbalance handling |

---

## 📈 Performance

### Accuracy

**≈ 82% – 90%** *(depending on the number of classes)*

### Evaluation Metrics

* Precision
* Recall
* F1-score
* Confusion Matrix

---

# 🖥️ Streamlit Application Features

✅ Enter custom news headlines

✅ Get instant category predictions

✅ View confidence scores for all categories

✅ Try sample headlines for quick testing

✅ Interactive and user-friendly interface

---

# 📂 Project Structure

```text
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
```

---

# 🚀 How to Run the Project

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Run Jupyter Notebooks

Start Jupyter Notebook:

```bash
jupyter notebook
```

Run the notebooks in the following order:

1. `01_data_preprocessing.ipynb`
2. `02_model_comparison.ipynb`
3. `03_final_model_training.ipynb`

---

## 3️⃣ Train the Model (Optional)

```bash
python train.py
```

---

## 4️⃣ Launch the Streamlit App

```bash
streamlit run app.py
```

---

# 🧪 Example Predictions

| Input Headline                 | Predicted Category   |
| ------------------------------ | -------------------- |
| NASA launches new Mars mission | Science / Technology |
| Government passes new tax law  | Politics             |
| Messi scores winning goal      | Sports               |
| Apple releases new iPhone      | Technology           |

---

# 📚 Key Learnings

Through this project, I learned:

* NLP text preprocessing techniques
* Feature extraction using TF-IDF
* Machine learning model comparison
* Handling class imbalance
* Model evaluation using classification metrics
* Building and deploying applications with Streamlit

---

# 🔮 Future Improvements

* Implement deep learning models (**LSTM**, **BERT**)
* Improve class imbalance handling
* Deploy on **Streamlit Cloud** or **Hugging Face Spaces**
* Add real-time news scraping
* Create REST API support using Flask/FastAPI
* Fine-tune transformer models for higher accuracy

---

## ⭐ If you found this project helpful, consider giving it a star!
